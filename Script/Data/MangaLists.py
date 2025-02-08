import os
from Script.Utils import JsonUtils
JsonUtil = JsonUtils()
class MangaLists:
    def MangaList(self) -> list[str]:
        """
        Retrieves the list of all manga stored in the database.

        Returns:
            list[str]: A list of strings containing the names of all manga in the database.
        """
        
        if (os.path.exists("./Data/MangaList.json")):
            return JsonUtil.LoadJson("./Data/MangaList.json")
        else:
            return []
    def MangaStatusList(self) -> dict[str, list[str]]:
        
        """
        Retrieves the dictionary of all manga status lists stored in the database.

        Returns:
            dict[str, list[str]]: A dictionary of lists containing the names of all manga in each status list in the database.
        """
        
        if (os.path.exists("./Data/MangaStatusList.json")):
            return JsonUtil.LoadJson("./Data/MangaStatusList.json")
        else:
            print("MangaStatusList manga not found")
            return {}
    
    def MangaCurrentStatusList(self, Status:str) -> list[str]:
        
        """
        Retrieves the list of manga in a specific status list from the database.

        Args:
            Status (str): The status list to retrieve.

        Returns:
            list[str]: A list containing the names of all manga in the specified status list, or an empty list if the status list does not exist.
        """

        if (os.path.exists("./Data/MangaStatusList.json")):
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/MangaStatusList.json")
            Info:list[str] = StatusList[Status]
            return Info
        else:
            print("MangaCurrentStatusList manga not found") 
            return []
    
    def OnGoingList(self) -> list[str]:
        if (os.path.exists("./Data/MangaStatusList.json")):
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/MangaStatusList.json")
            return StatusList["Reading"] + StatusList["PlanToRead"]
        else:
            print("MangaStatusList manga not found")
            return []
        
    def CurrentStatusTypeList(self):
        return ["Reading", "PlanToRead", "Completed", "Dropped"]

    def FavoriteMangaList(self) -> list[str]:
        if (os.path.exists("./Data/FavoriteMangaList.json")):
            return JsonUtil.LoadJson("./Data/FavoriteMangaList.json")
        else:
            return []

GetMangaList = MangaLists()