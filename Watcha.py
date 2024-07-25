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
    
    
    @property
    def AnimeData(self):
        return {
            "Anime": {
                "Name": self.Name,
                "EpisodesStatus": self.CurrentEpisodeStatus(),
                "Status": self.CurrentStatus,
                "Temporada": self.Temporada,
                "MaxEpisodes": self.MaxEpisodes,
                "Episode": self.Episode
            }
        }
    def Data(self):
        return self.AnimeData
    

class Watcha:

    def __init__(self):
        self.selected:Anime = Anime("", 0, "", "")
    
    def PrintData(self):
        return {
            "Anime": {
                "Name": self.selected.Name,
                "Episodes": self.selected.CurrentEpisodeStatus(),
                "Status": self.selected.CurrentStatus,
                "Temporada": self.selected.Temporada
            }
        }
    
    def UpdateData(self, name):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            self.selected.DataBase = json.load(open(f"./Data/AnimeData/{name}.json"))
            self.selected.ConvertData()
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
    
    def Remove(self, name):
        if (os.path.exists(f"./Data/AnimeData/{name}.json")):
            os.remove(f"./Data/AnimeData/{name}.json")
        else:
            print("Remove not found")

    def SetNewAnime(self, name, maxpisodes, currentstatus, temp):
        NewAnime = Anime(name, maxpisodes, currentstatus, temp)
        json.dump(NewAnime.Data(), open(f"./Data/AnimeData/{name}.json", "w"))
        if (os.path.exists(f"./Data/ListedAnimes.json")):
            List:list = json.load(open(f"./Data/ListedAnimes.json"))
            List.append(name)
            json.dump(List, open(f"./Data/ListedAnimes.json", "w"))
        else:
            json.dump([], open(f"./Data/ListedAnimes.json", "w"))


Watch = Watcha()

class ExecuteFunctions:
    

    def __init__(self):
        self.NameList:list = json.load(open("./Data/ListedAnimes.json"))         

    def Reset(self):
            Default:dict = {
                "Name": "",
                "Name": "",
                "MaxEpisodes": 0,
                "Status": "",
                "Temporada": ""
            }
            json.dump(Default, open("./AddInfo.json", "w"))
    def Add(self):
        Info:dict = json.load(open("./AddInfo.json"))
        Name:str = Info.get("Name")
        MaxEpisodes:int = Info.get("MaxEpisodes")
        Status:str = Info.get("Status")
        Temp:str = Info.get("Temporada")
        Watch.SetNewAnime(Name, MaxEpisodes, Status, Temp)
        self.Reset()


    def GetAnimeStatus(self):
        Name:str = json.load(open("./GetStatusName.json"))
        Finded:bool = False
    
        for i in range(self.NameList.__len__()):
            Selected:str = self.NameList[i]
            if (not Finded and Selected.count(Name) > -1):
                print(Selected)
                if (os.path.exists(f"./Data/AnimeData/{Selected}.json")):
                    Watch.GetStatus(Selected)
                    json.dump("", open("./GetStatusName.json", "w"))
                    Finded = True
                else:
                    print("GetAnimeStatus path not found")
    
    def PrintAnimeList(self):
        print(self.NameList)
        time.sleep(30)

    def RemoveAnime(self):
        Name:str = json.load(open("./RemoveName.json"))
        Watch.Remove(Name)
        self.NameList.remove(Name)
        json.dump(self.NameList, open(f"./Data/ListedAnimes.json", "w"))
        
Run = ExecuteFunctions()
