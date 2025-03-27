import os
from Script.Utils import JsonUtil


class Anime:

    def __init__(self, name:str = "", maxepisodes:int = 0, status:str = "", Season:str = ""):
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
        self.Season:str = Season
        self.SerieName:str = ""
        self.Score:float = 0
        self.MyAnimeListLink:str = ""
        self.WatchLink:str = ""
        self.Path = ""    
    
    def CurrentEpisodeStatus(self) -> str:
        if (self.MaxEpisodes > 0):
            return f"{self.Episode}/{self.MaxEpisodes}"
        
        return f"{self.Episode}/Undefined"
        
    def DirectoryPath(self) -> str:
        return f"./Data/AnimeData/{JsonUtil.TrueName(self.Name)}.json"
        
    def GetData(self, Name:str) -> dict:
        return JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")["Anime"]
    
    def UpdateStatus(self):
        
        """
        Updates the anime status based on the current episode and max episodes.

        If the episode is greater than 0 and the current status is not "Dropped", it will update the status accordingly.
        If the episode is equal to the max episodes, it will set the status to "Completed".
        If the episode is less than 0, it will set the status to "Error".
        If the episode is 0 and the max episodes is 0, it will set the status to "PlanToWatch".
        """
        if (self.Episode > 0 and not self.CurrentStatus == "Dropped"):
            if (self.MaxEpisodes >= 0):
                if (self.CurrentStatus == "Completed"):
                    if (self.MaxEpisodes < self.Episode):
                        self.MaxEpisodes = self.Episode
                    else:
                        self.Episode = self.MaxEpisodes
                elif (self.Episode == self.MaxEpisodes):
                    self.CurrentStatus = "Completed"
            else:
                self.MaxEpisodes = 0
                if (self.Episode > 0):
                    self.CurrentStatus = "Watching"
                else:
                    self.Episode = 0
                    self.CurrentStatus = "PlanToWatch"
        elif (self.Episode < 0):
            self.CurrentStatus = "Error"

    
    def StoreData(self, Create:bool = False, UpdateStatus:bool = True):
        
        """
        Stores the anime data to the json file.

        Args:
            Create (bool, optional): If True, creates a new json file if it doesn't exist. Defaults to False.

        Side Effects:
            - Updates the "Status" attribute of the "Anime" object.
            - Updates the "Data" attribute of the "Anime" object.
            - If Create is False, updates the existing json file with the new data.
            - If Create is True, creates a new json file with the new data if it doesn't exist.
        """

        if (UpdateStatus):
            self.UpdateStatus()
        Data:dict = self.AnimeData()
        Path:str = self.DirectoryPath()
        if (not Create):
            if (os.path.exists(Path)):
                JsonUtil.UpdateJson(Data, Path)
            else:
                print(f"Store directory not found: {Path = }")
        else:
            if (self.Name != ""):
                JsonUtil.CreateJson(Data, Path)
            else:
                print(f"StoreData anime {self.Name} not found")
    
    def UpdateData(self, Name:str, UpdateStatus:bool = True):
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("UpdateData anime not found")
        
        try:
            Info:dict = self.GetData(Name)
            self.Name = Info["Name"]
            self.EpisodeStatus = Info["EpisodeStatus"]
            self.CurrentStatus = Info["Status"]
            self.Season = Info["Season"]
            self.MaxEpisodes = Info["MaxEpisodes"]
            self.Episode = Info["Episode"]
            self.SerieName = Info["SerieName"]
            self.MyAnimeListLink = Info["MyAnimeListLink"]
            self.WatchLink = Info["WatchLink"] 
            self.Score = Info["Score"]
            self.Path = self.DirectoryPath()
            if (UpdateStatus):
                self.UpdateStatus()
        except Exception:
            raise Exception("UpdateData anime error")
    
    
  
    def AnimeData(self) -> dict[str, dict]:
        return {
            "Anime": {
                "Name": JsonUtil.CursedStoreName(self.Name),
                "EpisodeStatus": self.CurrentEpisodeStatus(),
                "Status": self.CurrentStatus,
                "Season": self.Season,
                "MaxEpisodes": self.MaxEpisodes,
                "Episode": self.Episode,
                "SerieName": JsonUtil.CursedStoreName(self.SerieName),
                "MyAnimeListLink": self.MyAnimeListLink,
                "WatchLink": self.WatchLink,
                "Score": self.Score
            }
        }