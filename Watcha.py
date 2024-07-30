import time
import json
import os


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
        self.DataBase:dict = self.Data()
        self.Nota = 0
    
    def CurrentEpisodeStatus(self):
        return f"{self.Episode}/{self.MaxEpisodes}"
    
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
        Anime:dict = self.DataBase.get("Anime")
        self.Name = Anime.get("Name")
        self.EpisodeStatus = Anime.get("EpisodesStatus")
        self.CurrentStatus = Anime.get("Status")
        self.Temporada = Anime.get("Temporada") 
        self.MaxEpisodes = Anime.get("MaxEpisodes")
        self.Episode = Anime.get("Episode")
        self.SerieName = Anime.get("SerieName")
        self.Nota = Anime.get("Nota") 
    
    
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
                "Nota": self.Nota
            }
        }
    def Data(self):
        return self.AnimeData
    

class Watcha:

    def __init__(self):
        self.selected:Anime = Anime("", 0, "", "")
        self.SerieList:list = json.load(open("./Data/ListedSeries.json"))
        self.NameList:list = json.load(open("./Data/ListedAnimes.json"))
        self.SerieListData:dict = json.load(open("./Data/StatusList.json"))
        self.Anime:Anime = self.GetAnime("")
    
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
    
    
    def UpdateStatusList(self):
        CompletedList:list = []
        DroppedList:list = []
        PlanToWatchList:list = []
        WatchingList:list = []
        for anime in self.NameList:                       
            if (anime.CurrentStatus == "Watching"):
                WatchingList.append(anime)
            elif (anime.CurrentStatus == "Completed"):
                CompletedList.append(anime)
            elif (anime.CurrentStatus == "PlanToWatch"):
                PlanToWatchList.append(anime)
            elif (anime.CurrentStatus == "Dropped"):
                DroppedList.append(anime)
        Lists:dict = {
            "CompletedList": CompletedList,
            "DroppedList": DroppedList,
            "PlanToWatchList": PlanToWatchList,
            "WatchingList": WatchingList
        }
        json.dump(Lists, open("./Data/StatusList.json", "w"))

    def GetStatusList(self, Type:str):
        return self.SerieListData.get(f"{Type}List")
    
    def PrintStatusList(self, Type:str):
        Listed:list = self.SerieListData.get(f"{Type}List")
        print(Listed)
    
    def GetAnime(self, name):
        self.UpdateData(name)
        return self.selected 

    def UpdateData(self, name):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            self.selected.DataBase = json.load(open(f"./Data/AnimeData/{name}.json"))
            self.selected.ConvertData()
            self.UpdateStatusList()
        else:
            print("UpdateData not found")

    
    def GetStatus(self, name):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            self.UpdateData(name)
            print(self.PrintData())
            #del self.selected
            time.sleep(10)            
        else:
            print("Anime data not found")

    def AddEpisode(self, name, set = False, setEp = 0):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            self.UpdateData(name)
            if (set):
                self.selected.Episode = setEp
            else:
                self.selected.Episode += 1
            self.selected.UpdateStatus()            
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{name}.json", "w"))
        else:
            print("AddEpisode not found")

    def Dropped(self, name):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            self.selected = json.load(open(f"./Data/AnimeData/{name}.json"))
            self.selected.CurrentStatus = "Dropped"
        else:
            print("Dropped not found")
    def SetNota(self, name, nota):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            self.selected = json.load(open(f"./Data/AnimeData/{name}.json"))
            self.selected.Nota = nota
            json.dump(self.selected, open(f"./Data/AnimeData/{name}.json", "w"))
    
    def Remove(self, name):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            os.remove(f"./Data/AnimeData/{name}.json")
        else:
            print("Remove not found")

    def SetNewAnime(self, name, maxpisodes, currentstatus, temp, seriename = ""):
        NewAnime = Anime(name, maxpisodes, currentstatus, temp)        
        if (not seriename == ""):
            if (os.path.exists(f"./Data/SerieData/{seriename}.json")):
                self.SerieList.append(name)
                json.dump(self.SerieList, open(f"./Data/SerieData/{seriename}.json", "w"))
            else:
                json.dump([], open(f"./Data/SerieData/{seriename}.json", "w"))
            if (not os.path.exists(f"./Data/ListedSeries.json")):
                json.dump([], open(f"./Data/ListedSeries.json", "w"))
            if (os.path.exists(f"./Data/ListedAnimes.json") and not seriename == ""):
                List:list = json.load(open(f"./Data/ListedSeries.json"))
                List.append(seriename)
                json.dump(List, open(f"./Data/ListedSeries.json", "w"))
            NewAnime.SerieName = seriename
        json.dump(NewAnime.Data(), open(f"./Data/AnimeData/{name}.json", "w"))
        
        if (os.path.exists(f"./Data/ListedAnimes.json")):
            List:list = json.load(open(f"./Data/ListedAnimes.json"))
            List.append(name)
            json.dump(List, open(f"./Data/ListedAnimes.json", "w"))
        else:
            json.dump([], open(f"./Data/ListedAnimes.json", "w"))
    def AddToSerie(self, seriename, animename):
        if (os.path.exists(f"./Data/SerieData/{seriename}.json") and os.path.exists(f"./Data/AnimeData/{animename}.json")):
            List:list = json.load(open(f"./Data/SerieData/{seriename}.json"))
            List.append(animename)
            json.dump(List, open(f"./Data/SerieData/{seriename}.json", "w"))
        else:
            print("AddToSerie not found")




Watch = Watcha()

class ExecuteFunctions:
    

    def __init__(self):
        self.NameList:list = json.load(open("./Data/ListedAnimes.json"))
        self.SerieList:list = json.load(open("./Data/ListedSeries.json"))

    class Reset:         

        def ResetAdd(self):
            Default:dict = {
                "Name": "",
                "MaxEpisodes": 0,
                "Status": "",
                "Temporada": ""
            }
            json.dump(Default, open("./Info/AddInfo.json", "w"))
        def ResetAddEpisode(self):
            Default:dict = {
                "Name": "",
                "IsSetEp": False,
                "Ep": 0
            }
            json.dump(Default, open("./Info/AddEpisodeInfo.json", "w"))
    
    ResetInfo = Reset()

    def Add(self):
        Info:dict = json.load(open("./Info/AddAnimeInfo.json"))
        Name:str = Info.get("Name")
        MaxEpisodes:int = Info.get("MaxEpisodes")
        Status:str = Info.get("Status")
        Temp:str = Info.get("Temporada")
        Watch.SetNewAnime(Name, MaxEpisodes, Status, Temp)
        self.ResetInfo.ResetAdd()


    def GetAnimeStatus(self):
        Name:str = json.load(open("./Info/GetStatusName.json"))
        Finded:bool = False
    
        for i in range(self.NameList.__len__()):
            Selected:str = self.NameList[i]
            if (not Finded and Selected.count(Name) > -1):
                if (os.path.exists(f"./Data/AnimeData/{Selected}.json")):
                    Watch.GetStatus(Selected)
                    json.dump("", open("./Info/GetStatusName.json", "w"))
                    Finded = True
                else:
                    print("GetAnimeStatus path not found")
    
    def PrintAnimeList(self):
        print(self.NameList)
        time.sleep(30)

    def PrintSerieList(self):
        print(self.SerieList)
        time.sleep(30)

    def RemoveAnime(self):
        Name:str = json.load(open("./Info/RemoveName.json"))
        Watch.Remove(Name)
        self.NameList.remove(Name)        
        self.SerieList.remove(Watch.GetAnime(Name).SerieName)
        json.dump(self.NameList, open(f"./Data/ListedAnimes.json", "w"))

    def AddEpisode(self):
        Info:dict = json.load(open("./Info/AddEpisodeInfo.json"))
        Name:str = Info.get("Name")
        IsSetEp:bool = Info.get("IsSetEp")
        Ep:int = Info.get("Ep")

        Finded:bool = False
    
        for i in range(self.NameList.__len__()):
            Selected:str = self.NameList[i]
            if (not Finded and Selected.count(Name) > - 1):
                if (os.path.exists(f"./Data/AnimeData/{Selected}.json")):
                    Watch.AddEpisode(Selected, IsSetEp, Ep)
                    self.ResetInfo.ResetAddEpisode() 
                    Finded = True
                else:
                    print("AddEpisode path not found")
           
        
Run = ExecuteFunctions()
