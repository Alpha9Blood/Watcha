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
        self.Nota:int = 0
        self.DataBase:dict = self.Data()        
    
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
        self.NameList:list = json.load(open("./Data/ListedAnimes.json"))
        self.SerieListData:dict = json.load(open("./Data/StatusList.json"))
    
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
        Listed:list = self.SerieListData.get(f"{Type}List")
        print(Listed)
    

    def UpdateBaseData(self, name):
        if (name.count(":") > 0):
            TrueName:str = name.replace(":", "_")
        else:
            TrueName = name
        if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
            self.selected.DataBase = json.load(open(f"./Data/AnimeData/{TrueName}.json"))
            self.selected.ConvertData()
        else:
            print("UpdateData not found")

    def UpdateStatusList(self):
        CompletedList:list = []
        DroppedList:list = []
        PlanToWatchList:list = []
        WatchingList:list = []

        for anime in self.NameList: 
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
        json.dump(Lists, open("./Data/StatusList.json", "w"))

    def UpdateData(self, name):     
        self.UpdateStatusList()
        self.UpdateBaseData(name)
        
    
    def GetAnime(self, name):
        self.UpdateBaseData(name)
        return self.selected 

    
    def GetStatus(self, name):
        if  (name.count(":") > 0):
            TrueName:str = name.replace(":", "_")
        else:
            TrueName = name
        if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
            self.UpdateData(name)
            print(self.PrintData())
            time.sleep(10)            
        else:
            print("Anime data not found")

    def AddEpisode(self, name, set:bool = False, setEp = 0):
        if  (name.count(":") > 0):
            TrueName:str = name.replace(":", "_")
        else:
            TrueName = name
        if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
            self.UpdateData(name)
            if (set):
                self.selected.Episode = setEp
            else:
                self.selected.Episode += 1
            self.selected.UpdateStatus()            
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{TrueName}.json", "w"))
        else:
            print("AddEpisode not found")

    def Dropped(self, name):
        if  (name.count(":") > 0):
            TrueName:str = name.replace(":", "_")
        else:
            TrueName = name
        if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
            self.GetAnime(name).CurrentStatus = "Dropped"
            self.UpdateData(name)
        else:
            print("Dropped not found")

    def SetNota(self, name, nota):
        if  (name.count(":") > 0):
            TrueName:str = name.replace(":", "_")
        else:
            TrueName = name
        if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
            self.UpdateData(name)
            self.selected.Nota = nota
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{TrueName}.json", "w"))
    
    def Remove(self, name):
        self.UpdateData(name)
        ListedSeason:list = json.load(open(f"./Data/Season/{self.selected.Temporada}.json"))
        ListedSeason.remove(name)
        json.dump(ListedSeason, open(f"./Data/Season/{self.selected.Temporada}.json", "w"))
        if  (name.count(":") > 0):
            TrueName:str = name.replace(":", "_")
        else:
            TrueName = name
        if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
            os.remove(f"./Data/AnimeData/{TrueName}.json")
        else:
            print("Remove not found")

    def SetNewAnime(self, name:str, maxpisodes:int, currentstatus:str, temp:str, seriename:str = ""):
        NewAnime = Anime(name, maxpisodes, currentstatus, temp)

        if (not seriename == ""):
            
            if (os.path.exists(f"./Data/ListedSeries.json")):
                SerieList:list = json.load(open(f"./Data/ListedSeries.json"))
                if (SerieList.count(seriename) == 0):   
                    SerieList.append(seriename)
                    json.dump(SerieList, open(f"./Data/ListedSeries.json", "w"))
            else:
                json.dump([seriename], open(f"./Data/ListedSeries.json", "w"))

            if (os.path.exists(f"./Data/SerieData/{seriename}.json")):
                SerieDataList:list = json.load(open(f"./Data/SerieData/{seriename}.json"))
                if (SerieDataList.count(name) == 0):
                    SerieDataList.append(name)
                    json.dump(SerieDataList, open(f"./Data/SerieData/{seriename}.json", "w"))
            else:
                json.dump([name], open(f"./Data/SerieData/{seriename}.json", "w"))
            NewAnime.SerieName = seriename
        
        if (os.path.exists(f"./Data/Seasons/{NewAnime.Temporada}.json")):
            SeasonList:list = json.load(open(f"./Data/Seasons/{NewAnime.Temporada}.json"))
            if (SeasonList.count(NewAnime.Name) == 0):
                SeasonList.append(NewAnime.Name)
                json.dump(SeasonList, open(f"./Data/Seasons/{NewAnime.Temporada}.json", "w"))
        else:
            SeasonList:list = []
            SeasonList.append(NewAnime.Name)
            json.dump(SeasonList, open(f"./Data/Seasons/{NewAnime.Temporada}.json", "w"))
        
        if (os.path.exists(f"./Data/ListedAnimes.json")):
            AnimeList:list = json.load(open(f"./Data/ListedAnimes.json"))
            if (AnimeList.count(name) == 0):
                AnimeList.append(name)
                json.dump(AnimeList, open(f"./Data/ListedAnimes.json", "w"))
        else:
            AnimeList:list = []
            AnimeList.append(name)
            json.dump(AnimeList, open(f"./Data/ListedAnimes.json", "w"))

        if (name.count(":") > 0):
            TrueName:str = name.replace(":", "_")
        else:
            TrueName = name  
        json.dump(NewAnime.Data(), open(f"./Data/AnimeData/{TrueName}.json", "w"))


    def PrintSeason(self, seasonid):
        List:list = json.load(open(f"./Data/Seasons/{seasonid}.json"))
        print(f"{seasonid}", List)
        time.sleep(30)


    def AddToSerie(self, seriename, animename):
        if  (animename.count(":") > 0):
            TrueName:str = animename.replace(":", "_")
        else:
            TrueName = animename
        if (os.path.exists(f"./Data/SerieData/{seriename}.json") and os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
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
                "Temporada": "",
                "Serie": ""
            }
            json.dump(Default, open("./Info/AddAnimeInfo.json", "w"))
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
        Serie:str = Info.get("Serie")
        Watch.SetNewAnime(Name, MaxEpisodes, Status, Temp, Serie)

        self.ResetInfo.ResetAdd()

    def UpdateNota(self):
        Info:dict = json.load(open("./Info/SetNotaInfo.json")) 
        name = Info.get("Name")
        nota = Info.get("Nota")
        Watch.SetNota(name, nota)


    def GetAnimeStatus(self):
        Name:str = json.load(open("./Info/GetStatusName.json"))
        Finded:bool = False
    
        for i in range(self.NameList.__len__()):
            Selected:str = self.NameList[i]
            if (Selected.count(":") > 0):
                TrueName:str = Selected.replace(":", "_")
            else:
                TrueName = Selected  
            if (not Finded and Selected.count(Name) > 0):
                if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
                    Watch.GetStatus(TrueName)
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
    
    def PrintSeason(self):
        Info:dict = json.load(open("./Info/PrintSeasonInfo.json"))
        seasonid:str = Info.get("SeasonId")
        Watch.PrintSeason(seasonid)
        Default:dict = {
            "SeasonId": ""
        }
        json.dump(Default, open(f"./Info/PrintSeasonInfo.json", "w"))
    
    def PrintStatusList(self):
        Info:dict = json.load(open("./Info/GetCurrentStatus.json"))
        Status:dict = json.load(open("./Data/StatusList.json"))
        Selected:list = Status.get(f"{Info}")
        print(Selected)
        json.dump([], open(f"./Info/GetCurrentStatus.json", "w"))
        time.sleep(30)
        

    def RemoveAnime(self):
        Name:str = json.load(open("./Info/RemoveName.json"))
        Watch.Remove(Name)
        self.NameList.remove(Name)        
        self.SerieList.remove(Watch.GetAnime(Name).SerieName)
        json.dump(self.SerieList, open(f"./Data/ListedSeries.json", "w"))
        json.dump(self.NameList, open(f"./Data/ListedAnimes.json", "w"))
    
    def DroppedAnime(self):
        Name:str = json.load(open("./Info/DroppedName.json"))
        Watch.Dropped(Name)
        json.dump("", open(f"./Info/DroppedName.json", "w"))        

    def AddEpisode(self):
        Info:dict = json.load(open("./Info/AddEpisodeInfo.json"))
        Name:str = Info.get("Name")
        IsSetEp:bool = Info.get("IsSetEp")
        Ep:int = Info.get("Ep")

        Finded:bool = False
    
        for i in range(self.NameList.__len__()):
            Selected:str = self.NameList[i]
            if (Selected.count(":") > 0):
                TrueName:str = Selected.replace(":", "_")
            else:
                TrueName = Selected 
            if (not Finded and Selected.count(Name) > 0):
                if (os.path.exists(f"./Data/AnimeData/{TrueName}.json")):
                    Watch.AddEpisode(Selected, IsSetEp, Ep)
                    self.ResetInfo.ResetAddEpisode()                   
                    Finded = True
                else:
                    print("AddEpisode path not found")
           
        
Run = ExecuteFunctions()



class Test:
    
    def Reset(self):
        Pato:list = []
        json.dump(Pato, open(f"./Data/ListedAnimes.json", "w"))
        json.dump(Pato, open(f"./Data/ListedSeries.json", "w"))
        json.dump(Pato, open(f"./Data/SerieData/Bartender.json", "w"))
        json.dump(Pato, open(f"./Data/Seasons/Spring_04_2024.json", "w"))
    
    
testa = Test()
""" testa.Reset() """