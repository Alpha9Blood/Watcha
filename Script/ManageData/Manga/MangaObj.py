import os
from Script.Utils import JsonUtil
from PIL import ImageTk


class Manga:
    def __init__(self, Name:str = "", Chapters:int = 0, Status:str = ""):
        self.Name:str = Name
        self.Status:str = Status
        self.Chapters:int = Chapters
        self.LeastTimeUpdated:str = ""
        self.MyAnimeListLink:str = ""
        self.MangaLink:str = ""
        self.Score:float = 0
        self.Path:str = ""
        self.Photo:ImageTk.PhotoImage

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
                "MyAnimeListLink": self.MyAnimeListLink,
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
            self.MyAnimeListLink = Info["MyAnimeListLink"]
            self.MangaLink = Info["MangaLink"]
            self.Score = Info["Score"]
            self.Path = self.DirectoryPath()
            if (UpdateStatus):
                self.UpdateStatus()
        else:
            print("UpdateData manga not found")