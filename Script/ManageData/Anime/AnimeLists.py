import os
from Script.Utils import JsonUtil

class AnimeLists:
    def AnimeList(self) -> list[str]:
        """
        Retrieves the list of all anime stored in the database.

        Returns:
            list[str]: A list of strings containing the names of all anime in the database.
        """
        
        if (not os.path.exists("./Data/ListedAnimes.json")):
            raise Exception(f"AnimeList: Path not found: ./Data/ListedAnimes.json")
    
        return JsonUtil.LoadJson("./Data/ListedAnimes.json")[::-1]

    def DaysList(self) -> list[str]:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def AnimeStatusList(self) -> dict[str, list[str]]:
        
        """
        Retrieves the dictionary of all anime status lists stored in the database.

        Returns:
            dict[str, list[str]]: A dictionary of lists containing the names of all anime in each status list in the database.
        """
        
        if (not os.path.exists("./Data/AnimeStatusList.json")):
            raise Exception("AnimeStatusList: Path not found: ./Data/AnimeStatusList.json")
    
        return JsonUtil.LoadJson("./Data/AnimeStatusList.json")
    
    def GetSeason(self, Season:str) -> list[str]:
        if (not os.path.exists(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")):
            raise Exception(f"GetSeason: Path not found: ./Data/Seasons/{JsonUtil.TrueName(Season)}.json")
    
        return JsonUtil.LoadJson(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")
    
    def AnimeCurrentStatusList(self, Status:str) -> list[str]:
        
        """
        Retrieves the list of anime in a specific status list from the database.

        Args:
            Status (str): The status list to retrieve.

        Returns:
            list[str]: A list containing the names of all anime in the specified status list, or an empty list if the status list does not exist.
        """

        if (not os.path.exists("./Data/AnimeStatusList.json")):
            raise Exception("AnimeCurrentStatusList: Path not found: ./Data/AnimeStatusList.json") 
        
        StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/AnimeStatusList.json")

        if (Status not in StatusList.keys()):
            raise Exception("AnimeCurrentStatusList: status not found")

        Info:list[str] = StatusList[Status]
        return Info
        
    def OnGoingList(self) -> list[str]:
        if (not os.path.exists("./Data/AnimeStatusList.json")):
            raise Exception("AnimeStatusList: path not found: ./Data/AnimeStatusList.json")
        
        StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/AnimeStatusList.json")
        return (StatusList["PlanToWatch"] + StatusList["Watching"])[::-1]
    
    def CurrentStatusTypeList(self) -> list[str]:
        return ["PlanToWatch", "Watching", "Completed", "Dropped"]

    def SerieList(self) -> list[str]:
        if (not os.path.exists("./Data/ListedSeries.json")):
            raise Exception("SerieList: path not found: ./Data/ListedSeries.json")
        
        return JsonUtil.LoadJson("./Data/ListedSeries.json")[::-1]

    def FavoriteAnimeList(self) -> list[str]:
        if (not os.path.exists("./Data/FavoriteAnimeList.json")):
            raise Exception("FavoriteAnimeList: path not found: ./Data/FavoriteAnimeList.json")
        
        return JsonUtil.LoadJson("./Data/FavoriteAnimeList.json")
      
    def GetListedSeasons(self) -> list[str]:
        if (not os.path.exists("./Data/ListedAnimeSeasons.json")):
            raise Exception("GetListedSeasons: path not found: ./Data/ListedAnimeSeasons.json")
        
        return JsonUtil.LoadJson("./Data/ListedAnimeSeasons.json")
        
    def HasMAL_LinkList(self) -> list[str]:
        if (not os.path.exists("./Data/AnimeLinks.json")):
            print("HasWatchLinkList: path not found: ./Data/AnimeLinks.json")
            return []
        
        AnimeLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/AnimeLinks.json")
        if (not AnimeLinks["MyAnimeListLinks"]):
            raise Exception("HasWatchLinkList: MyAnimeListLinks found: ./Data/AnimeLinks.json")
        
        return list(AnimeLinks["MyAnimeListLinks"].keys())
    
    def HasWatchLinkList(self) -> list[str]:
        if (not os.path.exists("./Data/AnimeLinks.json")):
            print("HasWatchLinkList: path not found: ./Data/AnimeLinks.json")
            return []
        
        AnimeLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/AnimeLinks.json")
        if (not AnimeLinks["WatchLinks"]):
            raise Exception("HasWatchLinkList: WatchLinks found: ./Data/AnimeLinks.json")
            
        return list(AnimeLinks["WatchLinks"].keys())

GetAnimeList = AnimeLists()