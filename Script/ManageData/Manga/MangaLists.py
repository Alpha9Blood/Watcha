import os
from Script.Utils import JsonUtil

class MangaLists:
    def MangaList(self) -> list[str]:
        """
        Retrieves the list of all manga stored in the database.

        Returns:
            list[str]: A list of strings containing the names of all masnga in the database.
        """
        
        if (os.path.exists("./Data/MangaList.json")):
            return JsonUtil.LoadJson("./Data/MangaList.json")[::-1]
        else:
            raise Exception("MangaList: Path not found: ./Data/MangaList.json")
        

    def CurrentStatusTypeList(self):
        return ["Reading", "PlanToRead", "Completed", "Dropped"]
    
    def MangaStatusList(self) -> dict[str, list[str]]:
        
        """
        Retrieves the dictionary of all manga status lists stored in the database.

        Returns:
            dict[str, list[str]]: A dictionary of lists containing the names of all manga in each status list in the database.
        """
        
        if (os.path.exists("./Data/MangaStatusList.json")):
            return JsonUtil.LoadJson("./Data/MangaStatusList.json")
        else:
            raise Exception("MangaStatusList manga not found")
    
    def MangaCurrentStatusList(self, Status:str) -> list[str]:
        
        """
        Retrieves the list of manga in a specific status list from the database.

        Args:
            Status (str): The status list to retrieve.

        Returns:
            list[str]: A list containing the names of all manga in the specified status list, or an empty list if the status list does not exist.
        """

        if (os.path.exists("./Data/MangaStatusList.json")):
            if (Status not in self.CurrentStatusTypeList()):
                raise Exception("MangaCurrentStatusList: status not found")
            
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/MangaStatusList.json")
            Info:list[str] = StatusList[Status]
            return Info
        else:
            raise Exception("MangaCurrentStatusList: manga not found: ./Data/MangaStatusList.json") 
    
    def OnGoingList(self) -> list[str]:
        if (os.path.exists("./Data/MangaStatusList.json")):
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/MangaStatusList.json")
            return StatusList["Reading"] + StatusList["PlanToRead"]
        else:
            raise Exception("MangaStatusList: manga not found: ./Data/MangaStatusList.json")

    def FavoriteMangaList(self) -> list[str]:
        if (os.path.exists("./Data/FavoriteMangaList.json")):
            return JsonUtil.LoadJson("./Data/FavoriteMangaList.json")
        else:
            raise Exception("FavoriteMangaList: manga not found: ./Data/FavoriteMangaList.json")
    
    def HasMAL_LinkList(self) -> list[str]:
        Selected:str = ""
        AnimeList:list[str] = self.MangaList()
        List:list[str] = []
        for i in AnimeList:
            try:
                Selected = JsonUtil.LoadJson(f"./Data/MangaData/{JsonUtil.TrueName(i)}.json")["Manga"]["MyAnimeListLink"]
                if (Selected != ""):
                    List.append(i)
            except:
                raise Exception(f"HasMAL_LinkList: manga not found: ./Data/MangaData/{JsonUtil.TrueName(i)}.json or wrong format")
        return List
    
    def HasMangaLinkList(self) -> list[str]:
        Selected:str = ""
        AnimeList:list[str] = self.MangaList()
        List:list[str] = []
        for i in AnimeList:
            try:
                Selected = JsonUtil.LoadJson(f"./Data/MangaData/{JsonUtil.TrueName(i)}.json")["Manga"]["MangaLink"]
                if (Selected != ""):
                    List.append(i)
            except:
                raise Exception(f"HasMangaLinkList: manga not found: ./Data/MangaData/{JsonUtil.TrueName(i)}.json or wrong format")
        return List

GetMangaList = MangaLists()