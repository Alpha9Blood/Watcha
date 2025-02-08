import os
from Script.Utils import JsonUtil
from Script.ManageData.Anime.AnimeObj import Anime
class SeasonsManager():

    def __init__(self) -> None:
        self.SeasonsOrder:list[str] = ["Winter", "Spring", "Summer", "Fall"]

    def GetSeasonYear(self, season:str) -> int:
        return int(season.split("_")[1])
    
    def GetSeasonName(self, season:str) -> str:
        return season.split("_")[0]
    
    def ReturnSeasons(self) -> list[str]:
        return self.SeasonsOrder
    
    def ReturnSeasonsYears(self) -> list[str]:
        if (os.path.exists("./Data/SeasonsLinks.json")):
            Info:dict = JsonUtil.LoadJson("./Data/SeasonsLinks.json")
            return list(Info.keys())
        else:
            raise Exception("ReturnSeasonsYears path not found")
    
    def __RemoveFromSeason(self, SelectedAnime:dict[str, str]):
        if (os.path.exists(f"./Data/Seasons/{SelectedAnime["Season"]}.json")):
            Season:list[str] = JsonUtil.LoadJson(f"./Data/Seasons/{SelectedAnime["Season"]}.json")
            Season.remove(SelectedAnime["Name"])
            JsonUtil.UpdateJson(Season, f"./Data/Seasons/{SelectedAnime["Season"]}.json")
        else:
            raise Exception("__RemoveFromSeason season not found")
        
    def __AddToSeason(self, SelectedAnime:dict[str, str]):
        if (os.path.exists(f"./Data/Seasons/{SelectedAnime['Season']}.json")):
            Season:list[str] = JsonUtil.LoadJson(f"./Data/Seasons/{SelectedAnime['Season']}.json")
            Season.append(SelectedAnime["Name"])
            JsonUtil.UpdateJson(Season, f"./Data/Seasons/{SelectedAnime['Season']}.json")
        else:
            raise Exception("__AddToSeason season not found")

    def __UpdateSeasonsOrder(self):
        SeasonsLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/SeasonsLinks.json")
        NewOrder:list[str] = []

        for Year in SeasonsLinks:
            SelectedYear:dict[str, str] = SeasonsLinks[Year]
            for SelectedSeason in SelectedYear:
                NewOrder.append(SelectedSeason)
        
        if (os.path.exists(f"./Data/ListedAnimeSeasons.json")):
            JsonUtil.UpdateJson(NewOrder, f"./Data/ListedAnimeSeasons.json")
        else:
            JsonUtil.CreateJson(NewOrder, f"./Data/ListedAnimeSeasons.json")
                
        
        JsonUtil.UpdateJson(NewOrder, "./Data/ListedAnimeSeasons.json")
    
    def __ClearEmptySeasons(self):
        SeasonList:list[str] = JsonUtil.LoadJson("./Data/ListedAnimeSeasons.json")
        SeasonLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/SeasonsLinks.json")

        for Season in SeasonList:
            SelectedSeason:list[str] = JsonUtil.LoadJson(f"./Data/Seasons/{Season}.json")
            if (len(SelectedSeason) == 0):
                os.remove(f"./Data/Seasons/{Season}.json")
                SeasonLinks[str(SeasonManager.GetSeasonYear(Season))].pop(Season)

                if (len(SeasonLinks[str(SeasonManager.GetSeasonYear(Season))]) == 0):
                    SeasonLinks.pop(str(SeasonManager.GetSeasonYear(Season)))

                SeasonList.remove(Season)

        JsonUtil.UpdateJson(SeasonList, "./Data/ListedAnimeSeasons.json")
        JsonUtil.UpdateJson(SeasonLinks, "./Data/SeasonsLinks.json")
    
    def CheckSeasonlink(self, NewAnime:Anime):
        if (os.path.exists(f"./Data/SeasonsLinks.json")):
            SeasonLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson(f"./Data/SeasonsLinks.json")
            if (str(SeasonManager.GetSeasonYear(NewAnime.Season)) in SeasonLinks):
                if (SeasonManager.GetSeasonName(NewAnime.Season) in SeasonLinks[str(SeasonManager.GetSeasonYear(NewAnime.Season))]):
                    pass
                else:
                    SeasonLinks[str(SeasonManager.GetSeasonYear(NewAnime.Season))].update({NewAnime.Season: ""})
                    JsonUtil.UpdateJson(SeasonLinks, f"./Data/SeasonsLinks.json")
            else:
                SeasonLinks.update({str(SeasonManager.GetSeasonYear(NewAnime.Season)): {NewAnime.Season: ""}})
                JsonUtil.UpdateJson(SeasonLinks, f"./Data/SeasonsLinks.json")
        else:
            SeasonLinks:dict[str, dict[str, str]] = {str(SeasonManager.GetSeasonYear(NewAnime.Season)): {NewAnime.Season: ""}}
            JsonUtil.CreateJson(SeasonLinks, f"./Data/SeasonsLinks.json")

    def UpdateSeasonLinks(self):
        SeasonsLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/SeasonsLinks.json")
        SortedSeasonsLinks:dict[str, dict[str, str]] = {}
        ListedSeasonsYears:list[int] = []
        ListedSeasons:list[dict[str, str]] = []

        SelectedYear:dict[str, str] = {}
        SelectedSeason:str = ""


        for Year in SeasonsLinks:
            ListedSeasonsYears.append(int(Year))
            for Season in self.SeasonsOrder:
                SelectedSeason = f"{Season}_{Year}"
                SelectedYear = SeasonsLinks[Year]
                if (SelectedSeason in SelectedYear):
                    ListedSeasons.append({SelectedSeason: SelectedYear[SelectedSeason]})

        ListedSeasonsYears = sorted(ListedSeasonsYears)

        for Year in ListedSeasonsYears:
            SortedSeasonsLinks.update({str(Year): {}})
            
            SelectedYear = SeasonsLinks[str(Year)]
            for Season in self.SeasonsOrder:
                SelectedSeason = f"{Season}_{Year}"
                if (SelectedSeason in SelectedYear):
                    SortedSeasonsLinks[str(Year)].update({SelectedSeason: SelectedYear[SelectedSeason]})
        


        
        JsonUtil.UpdateJson(SortedSeasonsLinks, "./Data/SeasonsLinks.json")
        self.__UpdateSeasonsOrder()

    def AddSeasonLinks(self, season:str):
        Link:str = f"https://myanimelist.net/anime/season/{self.GetSeasonYear(season)}/{self.GetSeasonName(season).lower()}"
        if (os.path.exists("./Data/SeasonsLinks.json")):
            SeasonsLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/SeasonsLinks.json")
            
            if (SeasonsLinks[str(self.GetSeasonYear(season))]):
                SelectedYear:dict[str, str] = SeasonsLinks[str(self.GetSeasonYear(season))]
                SelectedYear[season] = Link
            else:
                SeasonsLinks.update({str(self.GetSeasonYear(season)): {season: Link}})
                
            JsonUtil.UpdateJson(SeasonsLinks, "./Data/SeasonsLinks.json")
            self.UpdateSeasonLinks()
        else:
            SeasonsLinks = {str(self.GetSeasonYear(season)): {season: Link}}
            JsonUtil.CreateJson(SeasonsLinks, "./Data/SeasonsLinks.json")

    
    def EditAnimeSeason(self, Name:str, NewSeason:str):
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            SelectedAnime:dict[str, dict[str, str]] = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            Selected:dict[str,str] = SelectedAnime["Anime"]
            
            self.__RemoveFromSeason(Selected)
            
            Selected["Season"] = NewSeason

            self.__AddToSeason(Selected)

            JsonUtil.UpdateJson(SelectedAnime, f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
        else:
            raise Exception("EditAnimeSeason not found")
        
        self.__ClearEmptySeasons()
        self.UpdateSeasonLinks()

        

SeasonManager = SeasonsManager()