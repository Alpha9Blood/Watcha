import os
import time
import webbrowser as web
from Script.ManageData.Manga.MangaObj import Manga
from Script.Utils import JsonUtil
from Script.ManageData.Manga.MangaLists import GetMangaList


class MangaWatcha:
    def __init__(self):
        self.selected:Manga = Manga()

    def SelectManga(self, Name:str) -> Manga:
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("SelectManga manga not found")
        
        self.selected.UpdateData(Name)
        return self.selected
    
    def UpdateStatusList(self, Selected:Manga, UpdateStatus:bool = True):
        Name = Selected.Name
        Status:dict[str, list[str]] = GetMangaList.MangaStatusList()
        
        
        if (UpdateStatus):
            Selected.UpdateStatus()

        SelectedList:list[str] = Status[Selected.Status]
        if (Name in SelectedList):
            return
        else:
            SelectedList.append(Name)

        for status in Status:
            if (status != Selected.Status):
                if (Name in Status[status]):
                    Status[status].remove(Name)
        
        JsonUtil.UpdateJson(Status, f"./Data/MangaStatusList.json")
        
    
    #Set
    

    def AddManga(self, Name:str, Chapters:int, Status:str):

        if (Status not in GetMangaList.CurrentStatusTypeList()):
            raise Exception(f"AddManga status not found: {Status}")
        
        NewManga:Manga = Manga(Name, Chapters, Status)

        if (os.path.exists("./Data/MangaList.json")):
            MangaListInfo:list = GetMangaList.MangaList()
            MangaListInfo.append(NewManga.Name)
            JsonUtil.UpdateJson(MangaListInfo, "./Data/MangaList.json")
        else:
            MangaListInfo:list = [NewManga.Name]
            JsonUtil.CreateJson(MangaListInfo, "./Data/MangaList.json")

        if (os.path.exists("./Data/MangaStatusList.json")):
            MangaStatusListInfo:dict[str, list[str]] = GetMangaList.MangaStatusList()
            Info:list[str] = MangaStatusListInfo[Status]
            Info.append(NewManga.Name)
            JsonUtil.UpdateJson(MangaStatusListInfo, "./Data/MangaStatusList.json")
        else:
            MangaStatusListInfo:dict[str, list[str]] = {"Reading": [], "Completed": [], "PlanToRead": [], "Dropped": []}
            Info:list[str] = MangaStatusListInfo[Status]
            Info.append(NewManga.Name)
            JsonUtil.CreateJson(MangaStatusListInfo, "./Data/MangaStatusList.json")
        
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            NewManga.LeastTimeUpdated = time.strftime("%d/%m/%Y")
            NewManga.StoreData(True)
        else:
            print("AddManga manga already exists")
    
    def UpdateMyAnimeListLink(self, Name:str, Link:str):
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception(f"UpdateMyAnimeListLink: Manga {Name} path not found")
        
        if ("?" in Link):
            Link = Link.split("?")[0]
        self.selected.UpdateData(Name, False)
        self.selected.MyAnimeListLink = Link
        self.selected.StoreData()

        
    def RemoveManga(self, Name:str):             
        if (os.path.exists("./Data/MangaList.json")):
            MangaListInfo:list[str] = GetMangaList.MangaList()
            if (Name in MangaListInfo):
                MangaListInfo.remove(Name)
                JsonUtil.UpdateJson(MangaListInfo, "./Data/MangaList.json")
        
        if (os.path.exists("./Data/MangaStatusList.json")):
            self.selected.UpdateData(Name)
            MangaStatusListInfo:dict[str, list[str]] = GetMangaList.MangaStatusList()
            Info:list[str] = MangaStatusListInfo[self.selected.Status]
            if (Name in Info):
                Info.remove(Name)
                JsonUtil.UpdateJson(MangaStatusListInfo, "./Data/MangaStatusList.json")
            else:
                print("RemoveManga manga not found in the list")
        
        if (os.path.exists("./Data/FavoriteMangaList.json")):
            MangaListInfo:list[str] = GetMangaList.FavoriteMangaList()
            if (Name in MangaListInfo):
                MangaListInfo.remove(Name)
                JsonUtil.UpdateJson(MangaListInfo, "./Data/FavoriteMangaList.json")

        if (os.path.exists(f"./Data/MangaImages/{JsonUtil.TrueName(Name)}.png")):
            os.remove(f"./Data/MangaImages/{JsonUtil.TrueName(Name)}.png")
        
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            os.remove(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")
        else:
            print("RemoveManga manga not found")

        
    
    def SetCurrentStatus(self, Name:str, Status:str):
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("SetCurrentStatus manga not found")
        
        StatusList:list[str] = GetMangaList.CurrentStatusTypeList()
        if (Status not in StatusList):
            raise Exception("SetCurrentStatus status not found")
        
        self.selected.UpdateData(Name, False)
        self.selected.Status = Status
        self.selected.StoreData(UpdateStatus = False)

        if (os.path.exists("./Data/MangaStatusList.json")):
            self.selected.Status = Status
            self.UpdateStatusList(self.selected, False)
            self.selected.StoreData(UpdateStatus = False)
        else:
            MangaStatusListInfo:dict[str, list[str]] = {"Reading": [], "Completed": [], "PlanToRead": [], "Dropped": []}
            Info:list[str] = MangaStatusListInfo[Status]
            Info.append(Name)
            JsonUtil.CreateJson(MangaStatusListInfo, "./Data/MangaStatusList.json")

    def AddLink(self, Name:str, Link:str):
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("AddLink manga not found")
        
        self.selected.UpdateData(Name)
        self.selected.MangaLink = Link
        self.selected.StoreData()

    def EditFavorite(self, Name:str, Add:bool = True):
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("EditFavorite manga not found")     
        
        if (os.path.exists("./Data/FavoriteMangaList.json")):
            if (Add):
                MangaListInfo:list[str] = GetMangaList.FavoriteMangaList()
                MangaListInfo.append(Name)
                JsonUtil.UpdateJson(MangaListInfo, "./Data/FavoriteMangaList.json")
            else:
                MangaListInfo:list[str] = GetMangaList.FavoriteMangaList()
                if (Name in MangaListInfo):
                    MangaListInfo.remove(Name)
                    JsonUtil.UpdateJson(MangaListInfo, "./Data/FavoriteMangaList.json")
                else:
                    print("EditFavorite manga not found in the list")
        else:
            if (Add):
                MangaListInfo:list[str] = [Name]
                JsonUtil.CreateJson(MangaListInfo, "./Data/FavoriteMangaList.json")
            else:
                print("EditFavorite manga not found")

    def EditChapters(self, Name:str, Set:bool = False, Chapters:str = ""):
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("EditChapters manga not found")
        
        self.selected.UpdateData(Name, False)
        
        if (Set):
            try:
                ChaptersI = int(Chapters)
                if (ChaptersI < 0):
                    ChaptersI = 0
                self.selected.Chapters = ChaptersI
            except:
                raise ValueError("EditChapters Chapters must be a integer number")
        else:
            self.selected.Chapters += 1
        
        self.selected.LeastTimeUpdated = time.strftime("%d/%m/%Y")
        self.UpdateStatusList(self.selected)
        self.selected.StoreData()
    
    def EditScore(self, Name:str, Score:str):
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("EditScore manga not found")
        
        if (Score == ""):
            raise Exception("EditScore Score is empty")
        try:
            ScoreF = float(Score)
        except ValueError:
            raise ValueError(f"EditScore: {Score = } needs to be a number")
        
        self.selected.UpdateData(Name)
        self.selected.Score = ScoreF
        self.selected.StoreData(UpdateStatus = False)


    #Get


    def GetStatus(self, Name:str) -> dict:
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("GetStatus manga not found")
        
        Info:dict = JsonUtil.LoadJson(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")["Manga"]
        
        PrintInfo:dict[str, str] = {
            "Name": Info["Name"],
            "Chapters": Info["Chapters"],
            "Status": Info["Status"],
            "LeastTimeUpdated": Info["LeastTimeUpdated"],
            "Score": Info["Score"]
        }

        Score:float = float(PrintInfo["Score"])
        if (Score == 0):
            PrintInfo["Score"] = "N/A"
        return PrintInfo

    def GetCurrentStatus(self, currentStatus:str = "") -> list[str] | dict[str, list[str]]:
        if (not os.path.exists(f"./Data/MangaStatusList.json")):        
            raise Exception("GetCurrentStatus manga not found")
        
        if (currentStatus == ""):
            CurrentStatusList:dict[str, list[str]] = GetMangaList.MangaStatusList()
            return CurrentStatusList
        else:
            StatusList:list[str] = GetMangaList.MangaCurrentStatusList(currentStatus)
            return StatusList

    def OpenLink(self, Name:str):
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("OpenLink manga not found")    
        
        self.selected.UpdateData(Name)
        if (self.selected.MangaLink == ""):
            raise Exception("OpenLink manga not found")
        
        web.open(self.selected.MangaLink)
    
Watch = MangaWatcha()