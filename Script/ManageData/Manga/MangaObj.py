import os
from Script.ManageData.Manga.MangaLists import GetMangaList
from Script.Utils import JsonUtil
from PIL import ImageTk


class Manga:
    def __init__(self, Name:str = "", Chapter:int = 0, Status:str = ""):
        self.Name:str = Name
        self.Status:str = Status
        self.Chapter:int = Chapter
        self.LeastTimeUpdated:str = ""
        self.Score:float = 0
        self.Path:str = ""
        self.Photo:ImageTk.PhotoImage

    def DirectoryPath(self) -> str:
        path:str = f"./Data/MangaData/{JsonUtil.TrueName(self.Name)}.json"
        return path
    
    def GetData(self, Name:str) -> dict[str, str]:
        Data:dict[str, dict[str, str]] = JsonUtil.LoadJson(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")
        if (not Data["Manga"]):
            raise Exception("Maanga GetData manga not found")
        return Data["Manga"]
    
    def UpdateStatus(self):
        if (self.Chapter > 0):
            if (self.Status != "Completed" and self.Status != "Dropped"):
                self.Status = "Reading"
        elif (self.Chapter == 0):
            self.Status = "PlanToRead"
        else:
            self.Status = "Error"
    

    def MangaData(self) -> dict[str, dict]:
        return {
            "Manga" : {
                "Name": JsonUtil.CursedStoreName(self.Name),
                "Chapter": self.Chapter,
                "Status": self.Status,
                "LeastTimeUpdated": self.LeastTimeUpdated,
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
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("UpdateData manga not found")
            
        try:
            Info:dict = self.GetData(Name)

            for key in Info:
                if (not Info[key]):
                    raise Exception(f"UpdateData {key} manga not found")

            self.Name = Name
            self.Chapter = Info["Chapter"]
            self.Status = Info["Status"]
            self.LeastTimeUpdated = Info["LeastTimeUpdated"]
            self.Score = Info["Score"]
            self.Path = self.DirectoryPath()
            if (UpdateStatus):
                self.UpdateStatus()
        except Exception:
            raise Exception("UpdateData manga error")