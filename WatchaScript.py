import time
import json
import os , sys
sys.path.append(os.getcwd())
import tkinter as tk
import webbrowser as web



class Anime:

    def __init__(self, name:str, maxepisodes:int, status:str, temp:str):
        self.Name:str = name
        if (status == "PlanToWatch"):
            self.Episode:int = 0
        elif (status == "Completed"):
            self.Episode:int = maxepisodes
        else:
            self.Episode:int = 1
        self.MaxEpisodes:int = maxepisodes
        self.EpisodeStatus:str = self.CurrentEpisodeStatus()
        self.CurrentStatus:str = status
        self.Temporada:str = temp
        self.SerieName:str = ""
        self.Nota:float = 0
        self.MyAnimeListLink:str = ""
        self.DataBase:dict = self.Data()        
    
    def CurrentEpisodeStatus(self):
        if (self.Episode > 0):
            return f"{self.Episode}/{self.MaxEpisodes}"
        else:
            return f"{self.Episode}/Undefined"
    
    def UpdateStatus(self):
        if (self.Episode > 0 and not self.CurrentStatus == "Dropped"):
            if (self.Episode >= self.MaxEpisodes):
                self.Episode = self.MaxEpisodes
                self.CurrentStatus = "Completed"
            elif (self.Episode < self.MaxEpisodes):
                self.CurrentStatus = "Watching"
        elif (self.Episode == 0):
            self.CurrentStatus = "PlanToWatch"
        elif (self.Episode < 0):
            self.CurrentStatus = "Error"

    
    def ConvertData(self):
        Anime:dict = self.DataBase.get("Anime") # type: ignore
        self.Name = Anime.get("Name") # type: ignore
        self.EpisodeStatus = Anime.get("EpisodesStatus") # type: ignore
        self.CurrentStatus = Anime.get("Status") # type: ignore
        self.Temporada = Anime.get("Temporada") # type: ignore 
        self.MaxEpisodes = Anime.get("MaxEpisodes") # type: ignore
        self.Episode = Anime.get("Episode") # type: ignore
        self.SerieName = Anime.get("SerieName") # type: ignore
        self.MyAnimeListLink = Anime.get("MyAnimeListLink") # type: ignore
        self.Nota = Anime.get("Nota") # type: ignore 
    
    
    @property
    def AnimeData(self):
        return {
            "Anime": {
                "Name": self.Name,
                "EpisodesStatus": self.CurrentEpisodeStatus(),
                "Status": self.CurrentStatus,
                "Temporada": self.Temporada,
                "MaxEpisodes": self.MaxEpisodes,
                "Episode": self.Episode,
                "SerieName": self.SerieName,
                "MyAnimeListLink": self.MyAnimeListLink,
                "Nota": self.Nota
            }
        }
    def Data(self):
        return self.AnimeData
    

class Watcha:

    def __init__(self):
        self.selected:Anime = Anime("", 0, "", "")
        self.SerieListData:dict = json.load(open("./Data/StatusList.json"))
    
    def NameList(self):
        Names:list = json.load(open("./Data/ListedAnimes.json"))
        return Names
    
    def TrueName(self, Name:str):
        if  (Name.count(":") > 0):
            return Name.replace(":", "_")
        else:
            return Name
        
    
    def TrueSerieName(self, SerieName:str):
        if (SerieName.count(":") > 0):
            return SerieName.replace(":", "_")
        else:
            return SerieName


    def PrintData(self):
        return {
            "Anime": {
                "Name": self.selected.Name,
                "Episodes": self.selected.CurrentEpisodeStatus(),
                "Status": self.selected.CurrentStatus,
                "Temporada": self.selected.Temporada,
                "SerieName": self.selected.SerieName,
                "Nota": self.selected.Nota
            }
        }
    
    


    def GetStatusList(self, Type:str):
        return self.SerieListData.get(f"{Type}List")
    
    def PrintStatusList(self, Type:str):
        Listed:list = self.SerieListData.get(f"{Type}List") # type: ignore
        print(Listed)
    

    def UpdateBaseData(self, name):

        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.selected.DataBase = json.load(open(f"./Data/AnimeData/{self.TrueName(name)}.json"))
            self.selected.ConvertData()
        else:
            print("UpdateData not found")

    def UpdateStatusList(self):
        CompletedList:list = []
        DroppedList:list = []
        PlanToWatchList:list = []
        WatchingList:list = []

        for anime in self.NameList(): 
            self.UpdateBaseData(anime)
            SelectedStatus:str = self.selected.CurrentStatus
            SelectedName:str = self.selected.Name                    
            if (SelectedStatus == "Watching" and WatchingList.count(SelectedName) == 0):
                WatchingList.append(SelectedName)
            elif (SelectedStatus == "Completed" and CompletedList.count(SelectedName) == 0):
                CompletedList.append(SelectedName)
                if (WatchingList.count(SelectedName) > 0):
                    WatchingList.remove(SelectedName)
            elif (SelectedStatus == "PlanToWatch" and PlanToWatchList.count(SelectedName) == 0):
                PlanToWatchList.append(SelectedName)
            elif (SelectedStatus == "Dropped" and DroppedList.count(SelectedName) == 0):
                DroppedList.append(SelectedName)
                if (WatchingList.count(SelectedName) > 0):
                    WatchingList.remove(SelectedName)

        Lists:dict = {
            "Completed": CompletedList,
            "Dropped": DroppedList,
            "PlanToWatch": PlanToWatchList,
            "Watching": WatchingList
        }
        json.dump(Lists, open("./Data/StatusList.json", "w"), indent=4)

    def UpdateData(self, name):     
        self.UpdateStatusList()
        self.UpdateBaseData(name)
        
    
    def GetAnime(self, name):
        self.UpdateBaseData(name)
        return self.selected 

    
    def GetStatus(self, name):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            return self.PrintData()         
        else:
            print("Anime data not found")

    def UpdateEpisode(self, name, set:bool = False, setEp = 0):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            if (set):
                self.selected.Episode = setEp
            else:
                self.selected.Episode += 1
            self.selected.UpdateStatus()            
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"), indent=4)
        else:
            print("UpdateEpisode not found")

    def Dropped(self, name):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            self.selected.CurrentStatus = "Dropped"
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"), indent=4)
        else:
            print("Dropped not found")

    def SetNota(self, name:str, nota:float):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            self.selected.Nota = nota
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"), indent=4)
        else:
            print("SetNota not found")
    
    def Remove(self, name):
        self.UpdateData(name)
        ListedSeason:list = json.load(open(f"./Data/Seasons/{self.selected.Temporada}.json"))
        ListedSeason.remove(name)
        json.dump(ListedSeason, open(f"./Data/Seasons/{self.selected.Temporada}.json", "w"), indent=4)

        if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")):
            List:list = json.load(open(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json"))
            List.remove(name)
            json.dump(List, open(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json", "w"), indent=4)
            if (List.count(name) == 0):
                os.remove(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")
        else:
            print("RemoveSerieData not found")

        StatusList:dict = json.load(open("./Data/StatusList.json"))
        StatusList[f"{self.selected.CurrentStatus}"].remove(name)
        json.dump(StatusList, open("./Data/StatusList.json", "w"), indent=4)

        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            os.remove(f"./Data/AnimeData/{self.TrueName(name)}.json")
        else:
            print("RemoveAnime not found")

    def SetNewAnime(self, name:str, maxpisodes:int, currentstatus:str, temp:str, seriename:str = ""):
        NewAnime = Anime(name, maxpisodes, currentstatus, temp)

        if (not seriename == ""):
            
            if (os.path.exists(f"./Data/ListedSeries.json")):
                SerieList:list = json.load(open(f"./Data/ListedSeries.json"))
                if (SerieList.count(seriename) == 0):   
                    SerieList.append(seriename)
                    json.dump(SerieList, open(f"./Data/ListedSeries.json", "w"), indent=4)
            else:
                json.dump([seriename], open(f"./Data/ListedSeries.json", "w"), indent=4)
            
            if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json")):
                SerieDataList:list = json.load(open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json"))
                if (SerieDataList.count(name) == 0):
                    SerieDataList.append(name)
                    json.dump(SerieDataList, open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json", "w"), indent=4)
            else:
                json.dump([name], open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json", "w"), indent=4)
            NewAnime.SerieName = seriename
        
        if (os.path.exists(f"./Data/Seasons/{NewAnime.Temporada}.json")):
            SeasonList:list = json.load(open(f"./Data/Seasons/{NewAnime.Temporada}.json"))
            if (SeasonList.count(NewAnime.Name) == 0):
                SeasonList.append(NewAnime.Name)
                json.dump(SeasonList, open(f"./Data/Seasons/{NewAnime.Temporada}.json", "w"), indent=4)
        else:
            SeasonList:list = []
            SeasonList.append(NewAnime.Name)
            json.dump(SeasonList, open(f"./Data/Seasons/{NewAnime.Temporada}.json", "w"), indent=4)
        
        if (os.path.exists(f"./Data/ListedAnimes.json")):
            AnimeList:list = json.load(open(f"./Data/ListedAnimes.json"))
            if (AnimeList.count(name) == 0):
                AnimeList.append(name)
                json.dump(AnimeList, open(f"./Data/ListedAnimes.json", "w"), indent=4)
        else:
            AnimeList:list = []
            AnimeList.append(name)
            json.dump(AnimeList, open(f"./Data/ListedAnimes.json", "w"), indent=4)
        json.dump(NewAnime.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"), indent=4)
        self.UpdateData(name)

    def UpdateMyAnimeListLink(self, name, link):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            self.selected.MyAnimeListLink = link
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"), indent=4)
        else:
            print("UpdateMyAnimeListLink not found")


    def PrintSeason(self, seasonid):
        List:list = json.load(open(f"./Data/Seasons/{seasonid}.json"))
        return (f"{seasonid}", List)

    def AddToSerie(self, seriename, animename):
        if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json") and os.path.exists(f"./Data/AnimeData/{self.TrueName(animename)}.json")):
            List:list = json.load(open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json"))
            List.append(animename)
            json.dump(List, open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json", "w"), indent=4)
        else:
            print("AddToSerie not found")




Watch = Watcha()

class ExecuteFunctions:
    
    
    def __init__(self, Janela):
        self.Gui = Janela
        

    #Tools
    def ClearEntry(self, index:int):
        self.EntryList()[index].delete(0, 'end')

    def GetEntry(self, index:int):
        return self.EntryList()[index].get()
         
    def ButList(self):
        But:list[tk.Button] = self.Gui.ButList
        return But

    def TextList(self):
        Text:list[tk.Label] = self.Gui.TextList
        return Text

    def EntryList(self):
        Entry:list[tk.Entry] = self.Gui.EntryList
        return Entry
    
    def NameList(self):
        Name:list = json.load(open("./Data/ListedAnimes.json"))
        return Name
    
    def SerieList(self):
        Serie:list = json.load(open("./Data/ListedSeries.json"))
        return Serie


    #ExecFuncs


    #Set

    
    def RemoveLeastAdded(self):
        
        Namelist = self.NameList()
        SerieList = self.SerieList()
        Name:str = Namelist[::-1][0]
        
        Namelist.remove(Name)        
        SerieList.remove(Watch.GetAnime(Name).SerieName)
        Watch.Remove(Name) 
        json.dump(SerieList, open(f"./Data/ListedSeries.json", "w"), indent=4)
        json.dump(Namelist, open(f"./Data/ListedAnimes.json", "w"), indent=4)


    def Add(self):
        Name:str = self.GetEntry(0)
        if (len(self.GetEntry(1)) > 0):
            MaxEpisodes:int = int(self.GetEntry(1))
        else:
            MaxEpisodes:int = 0
        Status:str = self.GetEntry(2)
        Temp:str = self.GetEntry(3)
        Serie:str = self.GetEntry(4)

        def AddIsComplete():
            if (len(Name) > 0 and len(Status) > 0 and len(Temp) > 0):
                return True
            else:
                return False
            
        if (AddIsComplete()):
            Watch.SetNewAnime(Name, MaxEpisodes, Status, Temp, Serie)
            for i in range(5):
                self.ClearEntry(i)
        else:
            print("AddInfo is not completed")
    
    def RemoveAnime(self):
        Name:str = self.GetEntry(5)
        Namelist = self.NameList()
        SerieList = self.SerieList()
        if (Namelist.count(Name) > 0):
            Namelist.remove(Name)        
            SerieList.remove(Watch.GetAnime(Name).SerieName)
            Watch.Remove(Name)
            json.dump(Namelist, open(f"./Data/ListedAnimes.json", "w"), indent=4)       
            json.dump(SerieList, open(f"./Data/ListedSeries.json", "w"), indent=4)
            self.ClearEntry(5)
        else:
            print("AnimeRemove not found")

    def AddEppisode(self):
        Name:str = self.GetEntry(6)
        Finded:bool = False
        NameList = self.NameList()
        for i in range(NameList.__len__()):
            Selected:str = NameList[i]
            if (not Finded and Selected.count(Name) > 0):
                if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                    Watch.UpdateEpisode(Selected)
                    Finded = True
                    self.ClearEntry(6)
                else:
                    print("AddEpisode path not found") 

    def SetEpisode(self):
        Name:str = self.GetEntry(6)
        SetEP = self.GetEntry(7)

        Finded:bool = False
        NameList = self.NameList()
        if (len(SetEP) > 0):
            for i in range(NameList.__len__()):
                Selected:str = NameList[i]
                if (not Finded and Selected.count(Name) > 0):
                    if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                        Watch.UpdateEpisode(Selected, True, int(SetEP))
                        Finded = True
                        self.ClearEntry(6)
                        self.ClearEntry(7)
                    else:
                        print("SetEpisode path not found")
    
    def UpdateNota(self):
        name = self.GetEntry(8)
        nota = float(self.GetEntry(9))
        if (len(name) > 0):
            Watch.SetNota(name, nota)
            self.ClearEntry(8)
            self.ClearEntry(9)     

    def DropAnime(self):
        Name:str = self.GetEntry(10)
        Watch.Dropped(Name)
        self.ClearEntry(10)

    def AddMyAnimeListLink(self):
        Name = self.GetEntry(11)
        Link = self.GetEntry(12)
        Watch.UpdateMyAnimeListLink(Name, Link)
        self.ClearEntry(11)
        self.ClearEntry(12)


    #Get

    def OpenMyAnimeList(self):
        web.open("https://myanimelist.net")

    def PrintAnimeList(self):
        self.Gui.Texto.PrintDisplay(self.NameList())        

    def PrintSerieList(self):
        self.Gui.Texto.PrintDisplay(self.SerieList())

    
    def GetAnimeStatus(self):
        Name:str = self.GetEntry(0)
        Finded:bool = False
        NameList = self.NameList()
        for i in range(NameList.__len__()):
            Selected:str = NameList[i]
            if (not Finded and Selected.count(Name) > 0):
                if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                    self.Gui.Texto.PrintDisplay(Watch.GetStatus(Selected))
                    Finded = True
                    self.ClearEntry(0)
                else:
                    print("GetAnimeStatus path not found")
    
    def PrintSeason(self):
        SeasonID:str = self.GetEntry(1)
        self.Gui.Texto.PrintDisplay(Watch.PrintSeason(SeasonID))
        self.ClearEntry(1)
    
    def PrintStatusList(self):
        Info:str = self.GetEntry(2)
        Status:dict = json.load(open("./Data/StatusList.json"))
        Selected:list = Status.get(f"{Info}") # type: ignore
        self.Gui.Texto.PrintDisplay(Selected)
        self.ClearEntry(2)

    def OpenLink(self):
        Name:str = self.GetEntry(3)
        if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Name)}.json")):
            link = Watch.GetAnime(Name).MyAnimeListLink
            web.open(link)
            self.ClearEntry(3)
        else:
            print("OpenLink path not found")

    def PrintSerie(self):
        Name:str = self.GetEntry(4)
        if (os.path.exists(f"./Data/SerieData/{Name}.json")):
            Info:dict = json.load(open(f"./Data/SerieData/{Name}.json"))
            self.Gui.Texto.PrintDisplay(Info)
            self.ClearEntry(4)
        else:
            print("PrintSerie path not found")
    
    