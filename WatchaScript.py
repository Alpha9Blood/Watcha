import time
import json
import os , sys
sys.path.append(os.getcwd())
import tkinter as tk



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
        Listed:list = self.SerieListData.get(f"{Type}List")
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
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            print(self.PrintData())
            time.sleep(10)            
        else:
            print("Anime data not found")

    def AddEpisode(self, name, set:bool = False, setEp = 0):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            
            self.UpdateData(name)
            print(self.selected.CurrentEpisodeStatus())
            if (set):
                self.selected.Episode = setEp
            else:
                self.selected.Episode += 1
            print(self.selected.CurrentEpisodeStatus())
            self.selected.UpdateStatus()            
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"))
        else:
            print("AddEpisode not found")

    def Dropped(self, name):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            self.selected.CurrentStatus = "Dropped"
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"))
        else:
            print("Dropped not found")

    def SetNota(self, name:str, nota:float):
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(name)}.json")):
            self.UpdateData(name)
            self.selected.Nota = nota
            json.dump(self.selected.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"))
        else:
            print("SetNota not found")
    
    def Remove(self, name):
        self.UpdateData(name)
        ListedSeason:list = json.load(open(f"./Data/Seasons/{self.selected.Temporada}.json"))
        ListedSeason.remove(name)
        json.dump(ListedSeason, open(f"./Data/Seasons/{self.selected.Temporada}.json", "w"))

        if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")):
            List:list = json.load(open(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json"))
            List.remove(name)
            json.dump(List, open(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json", "w"))
            if (List.count(name) == 0):
                os.remove(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")
        else:
            print("RemoveSerieData not found")

        StatusList:dict = json.load(open("./Data/StatusList.json"))
        StatusList[f"{self.selected.CurrentStatus}"].remove(name)
        json.dump(StatusList, open("./Data/StatusList.json", "w"))

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
                    json.dump(SerieList, open(f"./Data/ListedSeries.json", "w"))
            else:
                json.dump([seriename], open(f"./Data/ListedSeries.json", "w"))
            
            if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json")):
                SerieDataList:list = json.load(open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json"))
                if (SerieDataList.count(name) == 0):
                    SerieDataList.append(name)
                    json.dump(SerieDataList, open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json", "w"))
            else:
                json.dump([name], open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json", "w"))
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
        json.dump(NewAnime.Data(), open(f"./Data/AnimeData/{self.TrueName(name)}.json", "w"))
        self.UpdateData(name)


    def PrintSeason(self, seasonid):
        List:list = json.load(open(f"./Data/Seasons/{seasonid}.json"))
        print(f"{seasonid}", List)
        time.sleep(30)


    def AddToSerie(self, seriename, animename):
        if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json") and os.path.exists(f"./Data/AnimeData/{self.TrueName(animename)}.json")):
            List:list = json.load(open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json"))
            List.append(animename)
            json.dump(List, open(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json", "w"))
        else:
            print("AddToSerie not found")




Watch = Watcha()

class ExecuteFunctions:
    
    
    def __init__(self, Janela):
        self.NameList:list = json.load(open("./Data/ListedAnimes.json"))
        self.SerieList:list = json.load(open("./Data/ListedSeries.json"))
        self.Gui = Janela
        self.ButList:list[tk.Button] = self.Gui.ButList
        self.TextList:list[tk.Label] = self.Gui.TextList
        self.EntryList:list[tk.Entry] = self.Gui.EntryList

    def ClearEntry(self , index:tk.Entry):
        index.delete(0, 'end')


    def Add(self):
        Name:str = self.EntryList[0].get()
        if (len(self.EntryList[1].get()) > 0):
            MaxEpisodes:int = int(self.EntryList[1].get())
        else:
            MaxEpisodes:int = 0
        Status:str = self.EntryList[2].get()
        Temp:str = self.EntryList[3].get()
        Serie:str = self.EntryList[4].get()

        def AddIsComplete():
            if (len(Name) > 0 and len(Status) > 0 and len(Temp) > 0):
                return True
            else:
                return False
            
        if (AddIsComplete()):
            Watch.SetNewAnime(Name, MaxEpisodes, Status, Temp, Serie)
            for i in range(5):
                self.EntryList[i].delete(0, 'end')
        else:
            print("AddInfo is not completed")
        
        

    def UpdateNota(self):
        name = self.EntryList[8].get()
        nota = float(self.EntryList[9].get())
        if (len(name) > 0):
            Watch.SetNota(name, nota)
            self.ClearEntry(self.EntryList[8])
            self.ClearEntry(self.EntryList[9])      

    def GetAnimeStatus(self):
        Name:str = json.load(open("./Info/GetStatusName.json"))
        Finded:bool = False
    
        for i in range(self.NameList.__len__()):
            Selected:str = self.NameList[i]
            if (not Finded and Selected.count(Name) > 0):
                if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                    Watch.GetStatus(Watch.TrueName(Selected))
                    json.dump("", open("./Info/GetGeralStatusName.json", "w"))
                    Finded = True
                else:
                    print("GetAnimeStatus path not found")
    
    def PrintAnimeList(self):
        print(self.NameList)
        time.sleep(30)

    def PrintSerieList(self):
        print(self.SerieList)
        time.sleep(30)

    def PrintSerie(self):
        Name:str = ""
        if (os.path.exists(f"./Info/{Name}.json")):
            Info:dict = json.load(open(f"./Info/{Name}.json"))
            print(f"Animes from Serie: {Info}")
            time.sleep(30)
        else:
            print("PrintSerie path not found")
    
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
        Name:str = self.EntryList[5].get()
        if (self.NameList.count(Name) > 0):
            self.NameList.remove(Name)        
            self.SerieList.remove(Watch.GetAnime(Name).SerieName)
            Watch.Remove(Name)       
            json.dump(self.SerieList, open(f"./Data/ListedSeries.json", "w"))
            json.dump(self.NameList, open(f"./Data/ListedAnimes.json", "w"))
            self.ClearEntry(self.EntryList[5])
        else:
            print("AnimeRemove not found")
    
    def DropAnime(self):
        Name:str = self.EntryList[10].get()
        Watch.Dropped(Name)
        self.ClearEntry(self.EntryList[10])

    def SetEpisode(self):
        Name:str = self.EntryList[6].get()
        SetEP = self.EntryList[7].get()

        Finded:bool = False
        if (len(SetEP) > 0):
            for i in range(self.NameList.__len__()):
                Selected:str = self.NameList[i]
                if (not Finded and Selected.count(Name) > 0):
                    if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                        Watch.AddEpisode(Selected, True, int(SetEP))
                        Finded = True
                        self.ClearEntry(self.EntryList[6])
                        self.ClearEntry(self.EntryList[7])
                    else:
                        print("AddEpisode path not found")
    
    def AddEppisode(self):
        Name:str = self.EntryList[6].get()
        Finded:bool = False
    
        for i in range(self.NameList.__len__()):
            Selected:str = self.NameList[i]
            if (not Finded and Selected.count(Name) > 0):
                if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                    Watch.AddEpisode(Selected)
                    Finded = True
                    self.ClearEntry(self.EntryList[6])
                else:
                    print("AddEpisode path not found")

    def RemoveLeastAdded(self):
        Name:str = self.NameList[::-1][0]
        self.NameList.remove(Name)        
        self.SerieList.remove(Watch.GetAnime(Name).SerieName)
        Watch.Remove(Name) 
        json.dump(self.SerieList, open(f"./Data/ListedSeries.json", "w"))
        json.dump(self.NameList, open(f"./Data/ListedAnimes.json", "w"))
    



class Test:
    
    def Reset(self):
        Pato:list = []
        json.dump(Pato, open(f"./Data/ListedAnimes.json", "w"))
        json.dump(Pato, open(f"./Data/ListedSeries.json", "w"))
        json.dump(Pato, open(f"./Data/SerieData/Bartender.json", "w"))
        json.dump(Pato, open(f"./Data/Seasons/Spring_04_2024.json", "w"))
    
    
testa = Test()
""" testa.Reset() """
