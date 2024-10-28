from tkinter import ttk
from Script.Utils import JsonUtil
import os
import time
from Script.Managers.CustomTypes.CustomEntry import CustomEntry
import webbrowser as web
from Script.GUI_Index import *
from Script.Data.MangaLists import GetMangaList

class Manga:
    def __init__(self, Name:str = "", Chapters:int = 0, Status:str = ""):
        self.Name:str = Name
        self.Status:str = Status
        self.Chapters:int = Chapters
        self.LeastTimeUpdated:str = ""
        self.MangaLink:str = ""
        self.Score:float = 0
        self.Path:str = ""

    def DirectoryPath(self) -> str:
        return f"./Data/MangaData/{JsonUtil.TrueName(self.Name)}.json"
    
    def GetData(self, Name:str) -> dict:
        return JsonUtil.LoadJson(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")["Manga"]
    
    def UpdateStatus(self):
        if (self.Chapters > 0):
            if (self.Status != "Completed" and self.Status != "Dropped"):
                self.Status = "Reading"
        elif (self.Chapters == 0):
            self.Status = "PlanToRead"
        else:
            self.Status = "Error"
    
    

    def MangaData(self) -> dict:
        return {
            "Manga" : {
                "Name": JsonUtil.CursedStoreName(self.Name),
                "Chapters": self.Chapters,
                "Status": self.Status,
                "LeastTimeUpdated": self.LeastTimeUpdated,
                "MangaLink": self.MangaLink,
                "Score": self.Score
                }
            }
            
    
    def StoreData(self, Create:bool = False, UpdateStatus:bool = True):
        
        """
        Stores the manga data to the json file.

        Args:
            Create (bool, optional): If True, creates a new json file if it doesn't exist. Defaults to False.

        Side Effects:
            - Updates the "Status" attribute of the "Manga" object.
            - Updates the "Data" attribute of the "Manga" object.
            - If Create is False, updates the existing json file with the new data.
            - If Create is True, creates a new json file with the new data if it doesn't exist.
        """
        if (UpdateStatus):
            self.UpdateStatus()
        Data:dict = self.MangaData()
        Path:str = self.DirectoryPath()
        if (not Create):
            if (os.path.exists(Path)):
                JsonUtil.UpdateJson(Data, Path)
            else:
                print("Store directory not found")
        else:
            if (self.Name != ""):
                JsonUtil.CreateJson(Data, Path)
            else:
                print("StoreData manga name not found")
    
    def UpdateData(self, Name:str, UpdateStatus:bool = True):
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Info:dict = self.GetData(Name)
            self.Name = Info["Name"]
            self.Chapters = Info["Chapters"]
            self.Status = Info["Status"]
            self.LeastTimeUpdated = Info["LeastTimeUpdated"]
            self.MangaLink = Info["MangaLink"]
            self.Score = Info["Score"]
            self.Path = self.DirectoryPath()
            if (UpdateStatus):
                self.UpdateStatus()
        else:
            print("UpdateData manga not found")




class Watcha:
    def __init__(self):
        self.selected:Manga = Manga()

    def SelectManga(self, Name:str) -> Manga:
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)
            return self.selected
        else:
            print("SelectManga manga not found")
            return self.selected
    
    def UpdateStatusList(self, Selected:Manga, UpdateStatus:bool = True):
        Status:dict[str, list[str]] = GetMangaList.MangaStatusList()
        Name = Selected.Name
        if (UpdateStatus):
            Selected.UpdateStatus()
        SelectedList:list[str] = Status[Selected.Status]
        for status in Status:
            if (status != Selected.Status):
                if (Name in Status[status]):
                    Status[status].remove(Name)
        if (Name in SelectedList):
            return
        else:
            SelectedList.append(Name)

        JsonUtil.UpdateJson(Status, f"./Data/MangaStatusList.json")
        
    
    #Set
    

    def AddManga(self, Name:str, Chapters:int, Status:str):
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
   
        
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            os.remove(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")
        else:
            print("RemoveManga manga not found")
    
    def SetCurrentStatus(self, Name:str, Status:str):
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
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
        else:
            print("SetCurrentStatus manga not found")

    def AddLink(self, Name:str, Link:str):
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)
            self.selected.MangaLink = Link
            self.selected.StoreData()
        else:
            print("AddLink manga not found")

    def EditFavorite(self, Name:str, Add:bool = True):
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
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
        else:
            print("EditFavorite manga not found")     

    def EditChapters(self, Name:str, Set:bool = False, Chapters:int = 0):
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name, False)
            if (Set):
                self.selected.Chapters = Chapters
            else:
                self.selected.Chapters += 1
            self.selected.LeastTimeUpdated = time.strftime("%d/%m/%Y")
            self.UpdateStatusList(self.selected)
            self.selected.StoreData()
            
        else:
            print("EditChapters manga not found")
    
    def ChangeScore(self, Name:str, Score:float):
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)
            self.selected.Score = Score
            self.selected.StoreData(UpdateStatus = False)
        else:
            print("EditScore manga not found")


    #Get


    def GetStatus(self, Name:str) -> dict:
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
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
        else:
            print("GetStatus manga not found")
            return {}

    def GetCurrentStatus(self, currentStatus:str = "") -> list[str] | dict[str, list[str]]:
        if (os.path.exists(f"./Data/MangaStatusList.json")):        
            if (currentStatus == ""):
                CurrentStatusList:dict[str, list[str]] = GetMangaList.MangaStatusList()
                return CurrentStatusList
            else:
                StatusList:list[str] = GetMangaList.MangaCurrentStatusList(currentStatus)
                return StatusList
        else:
            print("GetCurrentStatus manga not found")
            return {}

    def OpenLink(self, Name:str):
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)
            if (self.selected.MangaLink != ""):
                web.open(self.selected.MangaLink)
            else:
                print("OpenLink manga not found")
        else:
            print("OpenLink manga not found")    
    
Watch = Watcha()




class MangaExecute:
    def __init__(self):    
        self.SetEntryIndex = MangaSet.EntryIndex
        self.GetEntryIndex = MangaGet.EntryIndex

    def GuiInit(self, Gui):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = Gui

    #Tools

    def GetEntry(self, index:int) -> str:
        """
        Retrieves the text from the entry field at the given index in the GUI.

        Args:
            index (int): The index of the entry field to retrieve the text from.

        Returns:
            str: The text from the entry field at the given index.
        """
        EntryList:list[CustomEntry] = self.Gui.EntryList
        return EntryList[index].get()
    
    def ClearEntry(self, Index:int = -1, IndexList:list = []):
        EntryList:list[CustomEntry] = self.Gui.EntryList
        """
        Clears the entry fields in the GUI.

        Args:
            Index (int): The index of the entry field to clear. Defaults to -1.
            IndexList (list): A list of indices of entry fields to clear. Defaults to an empty list.

        """
        if (Index > -1):
            EntryList[Index].delete(0, 'end')
        if (IndexList != []):
            for i in IndexList:
                Entry:ttk.Combobox = EntryList[i]
                Entry.delete(0, 'end')
    
    def FindName(self, Name:str) -> str:
        List:list[str] = GetMangaList.MangaList()
        Result:str = ""
        for i in range(len(List)):
            Selected:str = List[i]
            if (Name.lower() in Selected.lower()):
                Result = Selected
                return Result
        
        if (Result == ""):
            print("FindName manga not found")
        return Result


    #Set


    def AddNewManga(self):
        Name:str = self.GetEntry(self.SetEntryIndex.AddNewManga.Name)
        
        if (Name != ""):
            Cap:str = self.GetEntry(self.SetEntryIndex.AddNewManga.Chapters)
            Chapters:int = 0
            if (Cap != ""):
                try:
                    Chapters = int(Cap)
                    if (Chapters < 0):
                        Chapters = 0
                except ValueError:
                    print("AddNewManga Chapters must be a integer number")
                    return

            Status:str = self.GetEntry(self.SetEntryIndex.AddNewManga.Status)

            NameList:list[str] = GetMangaList.MangaList()

            if (Name not in NameList):
                Watch.AddManga(Name, Chapters, Status)
                self.ClearEntry(self.SetEntryIndex.AddNewManga.Name)
                self.ClearEntry(self.SetEntryIndex.AddNewManga.Chapters)
                self.ClearEntry(self.SetEntryIndex.AddNewManga.Status)
            else:
                print("AddNewManga manga already exists")
        else:
            print("AddNewManga manga name is empty")
    
    def DeleteManga(self):
        Name:str = self.GetEntry(self.SetEntryIndex.DeleteManga.Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Watch.RemoveManga(Name)
            self.ClearEntry(self.SetEntryIndex.DeleteManga.Name)
        else:
            print("DeleteManga manga name is empty")
    

    def SetLink(self):
        Name:str = self.GetEntry(self.SetEntryIndex.SetLink.Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Link:str = self.GetEntry(self.SetEntryIndex.SetLink.Link)
            if (Link != ""):
                Watch.AddLink(Name, Link)
                self.ClearEntry(self.SetEntryIndex.SetLink.Name)
                self.ClearEntry(self.SetEntryIndex.SetLink.Link)
            else:
                print("SetLink manga link is empty")
        else:
            print("AddLink manga not found")

    def EditFavorite(self, Add:bool):
        Name:str = self.GetEntry(self.SetEntryIndex.EditFavorites.Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            if (Add):
                Watch.EditFavorite(Name)
                self.ClearEntry(self.SetEntryIndex.EditFavorites.Name)
            else:
                Watch.EditFavorite(Name, Add)
                self.ClearEntry(self.SetEntryIndex.EditFavorites.Name)
        else:
            print("EditFavorite manga not found")
    
    def AddFavorite(self):
        self.EditFavorite(True)

    def DeleteFavorite(self):
        self.EditFavorite(False)
    
    def UpdateChapters(self, Set:bool):
        Name:str = self.GetEntry(self.SetEntryIndex.UpdateChapters.Name)
        Name = self.FindName(Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):      
            if (Set):
                Cap:str = self.GetEntry(self.SetEntryIndex.UpdateChapters.Chapters)
                if (Cap != ""):
                    try:
                        Chapters:int = int(Cap)
                        if (Chapters >= 0):
                            Watch.EditChapters(Name, Set, Chapters)
                            self.ClearEntry(self.SetEntryIndex.UpdateChapters.Name)
                            self.ClearEntry(self.SetEntryIndex.UpdateChapters.Chapters)
                        else:
                            print("UpdateChapters chapters must be a positive number")
                    except ValueError:
                        print("UpdateChapters Chapters must be a integer number")       
                else:
                    print("UpdateChapters chapters is empty")                    
            else:
                Watch.EditChapters(Name)
                self.ClearEntry(self.SetEntryIndex.UpdateChapters.Name)     
        else:
            print("SetChapters manga not found")

    def SetChapters(self):
        self.UpdateChapters(True)

    def AddChapters(self):
        self.UpdateChapters(False)
    
    def SetStatus(self):
        Name:str = self.GetEntry(self.SetEntryIndex.SetStatus.Name)

        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Status:str = self.GetEntry(self.SetEntryIndex.SetStatus.Status)

            StatusList:list[str] = GetMangaList.CurrentStatusTypeList()
            if (Status in StatusList):       
                    Watch.SetCurrentStatus(Name, Status)
                    self.ClearEntry(self.SetEntryIndex.SetStatus.Name)
                    self.ClearEntry(self.SetEntryIndex.SetStatus.Status)
            else:
                print("SetStatus status not found")
        else:
            print("SetStatus manga name not found")
    
    def EditScore(self):
        Name:str = self.GetEntry(self.SetEntryIndex.EditScore.Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Scor:str = self.GetEntry(self.SetEntryIndex.EditScore.Score)

            if (Scor != ""):
                try:
                    Score:float = float(Scor)
                    if (Score >= 0 and Score <= 10):
                        Watch.ChangeScore(Name, Score)
                        self.ClearEntry(self.SetEntryIndex.EditScore.Name)
                        self.ClearEntry(self.SetEntryIndex.EditScore.Score)
                    else:
                        print("EditScore Score must be between 0 and 10")
                except ValueError:
                    print("EditScore Score must be a integer number")
            else:
                print("EditScore Score is empty")  
        else:
            print("EditScore manga name not found")          

    
    #Get


    def PrintManga(self):
        Name:str = self.GetEntry(self.GetEntryIndex.PrintManga.Name)
        Name = self.FindName(Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            
            self.Gui.Texto.PrintDisplay(Watch.GetStatus(Name))
            self.ClearEntry(self.GetEntryIndex.PrintManga.Name)
        else:
            print("PrintManga manga not found")

    def PrintCurrentStatus(self):
        Status:str = self.GetEntry(self.GetEntryIndex.PrintCurrentStatus.Status)
        if (os.path.exists(f"./Data/MangaStatusList.json")):
            
            if (Status == ""):
                self.Gui.Texto.PrintDisplay(Watch.GetCurrentStatus(Status))
                self.ClearEntry(self.GetEntryIndex.PrintCurrentStatus.Status)
            else:
                StatusList:list[str] = ["Reading", "PlanToRead", "Completed", "Dropped"]
                if (Status in StatusList):
                    Info:dict = JsonUtil.LoadJson(f"./Data/MangaStatusList.json")[Status]
                    NewInfo:list[str] = []
                    for i in range(len(Info)):
                        SelectedManga:Manga = Watch.SelectManga(Info[i])
                        NewInfo.append(SelectedManga.Name)
                        NewInfo.append(f"Chapters:{SelectedManga.Chapters}, Updated:{SelectedManga.LeastTimeUpdated}")

                    self.Gui.Texto.PrintDisplay(NewInfo)
                    self.ClearEntry(self.GetEntryIndex.PrintCurrentStatus.Status)
                else:
                    print("PrintCurrentStatus status not found")
        else:
            print("MangaStatusList not found")

    def OpenLink(self):
        Name:str = self.GetEntry(self.GetEntryIndex.OpenLink.Name)
        Name = self.FindName(Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in GetMangaList.MangaList()):
                SelectedManga:Manga = Watch.SelectManga(Name)
                if (SelectedManga.MangaLink != ""):
                    web.open(SelectedManga.MangaLink)
                    self.ClearEntry(self.GetEntryIndex.OpenLink.Name)
                else:
                    print("OpenLink manga link is empty")
            else:
                print("OpenLink manga not found in mangalist")
        else:
            print("OpenLink manga not found")

    def PrintFavorites(self):
        if (os.path.exists(f"./Data/FavoriteMangaList.json")):
            self.Gui.Texto.PrintDisplay(JsonUtil.LoadJson(f"./Data/FavoriteMangaList.json"))
        else:
            print("PrintFavorites favorites not found")