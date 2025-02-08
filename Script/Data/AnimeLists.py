import os
from Script.Utils import JsonUtils
JsonUtil = JsonUtils()

class AnimeLists:
    def AnimeList(self) -> list[str]:
        """
        Retrieves the list of all anime stored in the database.

        Returns:
            list[str]: A list of strings containing the names of all anime in the database.
        """
        
        if (os.path.exists("./Data/ListedAnimes.json")):
            return JsonUtil.LoadJson("./Data/ListedAnimes.json")
        else:
            print("AnimeList anime not found")
            return []
    
    def AnimeStatusList(self) -> dict[str, list[str]]:
        
        """
        Retrieves the dictionary of all anime status lists stored in the database.

        Returns:
            dict[str, list[str]]: A dictionary of lists containing the names of all anime in each status list in the database.
        """
        
        if (os.path.exists("./Data/AnimeStatusList.json")):
            return JsonUtil.LoadJson("./Data/AnimeStatusList.json")
        else:
            print("AnimeStatusList anime not found")
            return {}
    
    def GetSeason(self, Season:str) -> list[str]:
        if (os.path.exists(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")):
            return JsonUtil.LoadJson(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")
        else:
            print("GetSeason anime not found")
            return []
    
    def AnimeCurrentStatusList(self, Status:str) -> list[str]:
        
        """
        Retrieves the list of anime in a specific status list from the database.

        Args:
            Status (str): The status list to retrieve.

        Returns:
            list[str]: A list containing the names of all anime in the specified status list, or an empty list if the status list does not exist.
        """

        if (os.path.exists("./Data/AnimeStatusList.json")):
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/AnimeStatusList.json")
            Info:list[str] = StatusList[Status]
            return Info
        else:
            print("AnimeCurrentStatusList anime not found") 
            return []
        
    def OnGoingList(self) -> list[str]:
        if (os.path.exists("./Data/AnimeStatusList.json")):
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/AnimeStatusList.json")
            return StatusList["Watching"] + StatusList["PlanToWatch"]
        else:
            print("AnimeStatusList anime not found")
            return []
    
    def CurrentStatusTypeList(self) -> list[str]:
        return ["PlanToWatch", "Watching", "Completed", "Dropped"]

    def SerieList(self) -> list[str]:
        if (os.path.exists("./Data/ListedSeries.json")):
            return JsonUtil.LoadJson("./Data/ListedSeries.json")
        else:
            print("SerieList anime not found")
            return []

    def FavoriteAnimeList(self) -> list[str]:
        if (os.path.exists("./Data/FavoriteAnimeList.json")):
            return JsonUtil.LoadJson("./Data/FavoriteAnimeList.json")
        else:
            print("FavoriteAnimeList anime not found")
            return []
      
    def GetListedSeasons(self) -> list[str]:
        if (os.path.exists("./Data/ListedAnimeSeasons.json")):
            return JsonUtil.LoadJson("./Data/ListedAnimeSeasons.json")
        else:
            print("GetListedSeasons anime not found")
            return []
    
    def DaysList(self) -> list[str]:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

GetAnimeList = AnimeLists()