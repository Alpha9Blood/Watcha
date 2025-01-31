import os
import webbrowser as web
from Script.ManageData.Anime.AnimeObj import Anime
from Script.Managers.CustomTypes.CustomEntry import CustomEntry
from Script.GUI_Index import AnimeI
from Script.Utils import JsonUtil
from Script.ManageData.Anime.ManageSeasons import SeasonManager
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.ManageData.Anime.AnimeWatcha import Watch
from Script.ManageData.Anime.ManageSeries import SerieManager

class AnimeExecute:
    
    
    def __init__(self):
        self.AnimeIndex = AnimeI()
    
    def GuiInit(self, Janela):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = Janela
    
    
    #Tools
    def __ClearEntry(self, Index:int = -1, IndexList:list[int] = []):           
        """
        Clears the entry fields in the GUI.

        Args:
            Index (int): The index of the entry field to clear. Defaults to -1.
            IndexList (list): A list of indices of entry fields to clear. Defaults to an empty list.

        """
        
        EntryList:list[CustomEntry] = self.Gui.EntryList
        if (Index > -1):
            EntryList[Index].delete(0, 'end')
        if (IndexList != []):
            for i in IndexList:
                EntryList[i].delete(0, 'end')

    def __GetEntry(self, index:int) -> str:
        EntryList:list[CustomEntry] = self.Gui.EntryList
        return EntryList[index].get()
        
    def __FindName(self, Name:str, Serie:bool = False, CustomData:list[str] = []) -> str:
        """
        Finds an anime by name in the list of anime stored in the "./Data/ListedAnimes.json" file.

        Args:
            Name (str): The name of the anime to search for.

        Returns:
            str: The name of the anime found, or an empty string if not found.

        Notes:
            This function is case-insensitive.
        """
        if (Name == ""):
            raise Exception("__FindName: name is empty")
        
        Name = Name.lower()

        if (not CustomData):
            AnimeList:list[str] = GetAnimeList.AnimeList()
        else:
            AnimeList:list[str] = CustomData

        if (Serie):
            List:list[str] = GetAnimeList.SerieList()
        else:
            List:list[str] = AnimeList

        for var in List:
            if (Name in var.lower()):
                Name = var
                return Name
        
        raise Exception("__FindName: anime not found: " + Name)

    #ExecFuncs


    #Set

    
    

    def Add(self):
        Name:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.Name)
        if (Name != ""):
            MaxEpisode:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.MaxEp)
            if (MaxEpisode != ""):
                try:
                    MaxEpisodeI = int(MaxEpisode)
                    if (MaxEpisodeI < 0):
                        MaxEpisodeI = 0
                except ValueError:
                    print("AddAnime: MaxEpisode must be an integer:" + MaxEpisode)
                    return
            else:
                MaxEpisodeI = 0
            
            Status:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.Status)

            SeasonName:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.SeasonName)
            if (SeasonName not in SeasonManager.SeasonsOrder):
                raise Exception("AddAnime: invalid season")
            
            SeasonYear:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.SeasonYear)
            if (not SeasonYear.isdigit()):
                raise ValueError("AddAnime: SeasonYear must be a integer number: " + SeasonYear)
            
            Season:str = f"{SeasonName}_{SeasonYear}"
            
            Serie:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.Serie)

            def AddIsComplete() -> bool:
                if (MaxEpisodeI >= 0 and Status != ""):
                    return True
                else:
                    return False
            
            NameList:list[str] = GetAnimeList.AnimeList()
            if (Name not in NameList):
                if (AddIsComplete()):
                    Watch.SetNewAnime(Name, MaxEpisodeI, Status, Season, Serie)
                    Entrys:list[int] = [
                        self.AnimeIndex.AddAnime.EntryIndex.Name,
                        self.AnimeIndex.AddAnime.EntryIndex.MaxEp,
                        self.AnimeIndex.AddAnime.EntryIndex.Status,
                        self.AnimeIndex.AddAnime.EntryIndex.SeasonName,
                        self.AnimeIndex.AddAnime.EntryIndex.SeasonYear,
                        self.AnimeIndex.AddAnime.EntryIndex.Serie
                        ]
                    self.__ClearEntry(IndexList = Entrys)
                else:
                    raise Exception("AddAnime: MaxEpisode < 0 or Status is empty")
            else:
                raise Exception(f"AddAnime: Anime already exists:" + Name)
        else:
            raise Exception("AddAnime: Anime name is empty")
    
    def RemoveAnime(self):
        Name:str = self.__GetEntry(self.AnimeIndex.DeleteAnime.EntryIndex.Name)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.Remove(Name)
            self.__ClearEntry(self.AnimeIndex.DeleteAnime.EntryIndex.Name)
        else:
            print("AnimeRemove not found")
    
    def RemoveLeastAdded(self):   
        Namelist = GetAnimeList.AnimeList()
        if (Namelist == []):
            print("RemoveLeastAdded AnimeList is empty")
            return
        Name:str = Namelist[::-1][0]
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.Remove(Name)
        else:
            print("RemoveLeastAdded anime not found")

    def AddEppisode(self):
        Name:str = self.__GetEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)
        OnGoingList:list[str] = GetAnimeList.OnGoingList()
        Name = self.__FindName(Name, CustomData = OnGoingList)
        
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.UpdateEpisode(Name)
            self.__ClearEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)
        else:
            print("AddEpisode path not found")

    def SetEpisode(self):
        Name:str = self.__GetEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)
        
        OnGoingList:list[str] = GetAnimeList.OnGoingList()
        Name = self.__FindName(Name, CustomData = OnGoingList)

        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Episode:str = self.__GetEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Ep)

            Watch.UpdateEpisode(Name, True, Episode)
            self.__ClearEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)
            self.__ClearEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Ep)
        else:
            print("SetEpisode path not found")
    
    def EditAnimeInfo(self):
        Name:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Name)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Status:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Status)
            Score:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Score)
            MaxEp:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.MaxEp)
            Serie:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Serie)

            #TODO: Test ordem status
            if (Score != ""):
                Watch.SetScore(Name, Score)
                self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.Score)
            
            if (MaxEp != ""):
                Watch.EditMaxEp(Name, MaxEp)
                self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.MaxEp)

            if (Serie != ""):
                SerieManager.EditAnimeSerie(Name, Serie)
                self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.Serie)
            
            if (Status != ""):
                Watch.SetCurrentStatus(Name, Status)
                self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.Status)
        else:
            print(f"EditAnimeInfo anime not found: {Name}")


    def AddMyAnimeListLink(self):
        Name = self.__GetEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name)
        Link = self.__GetEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Link)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.UpdateMyAnimeListLink(Name, Link)
            self.Gui.ImageExtractor.StoreExtractedImage(Name, Link)
            self.__ClearEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name)
            self.__ClearEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Link)
        else:
            raise Exception(f"AddMyAnimeListLink not found: Name:{Name}, Path:./Data/MangaData/{JsonUtil.TrueName(Name)}.json")


    def AddToCalendar(self):
        Name = self.__GetEntry(self.AnimeIndex.AddToCallendar.EntryIndex.Name)
        Day = self.__GetEntry(self.AnimeIndex.AddToCallendar.EntryIndex.Day)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.CreateCalendar(Name, Day)
            self.__ClearEntry(self.AnimeIndex.AddToCallendar.EntryIndex.Name)
        else:
            print("AddToCalendar not found")

    def SetWatchLink(self):
        Name = self.__GetEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Name)
        Link = self.__GetEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Link)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.AddWatchLink(Name, Link)
            self.__ClearEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Name)
            self.__ClearEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Link)
        else:
            print("SetWatchLink path not found")
              


    #Get

    def OpenMALHomePage(self):
        web.open("https://myanimelist.net")

    def PrintAnimeList(self):
        self.Gui.Text.PrintDisplay(GetAnimeList.AnimeList())        

    def PrintSerieList(self):
        self.Gui.Text.PrintDisplay(GetAnimeList.SerieList())

    
    def __LoadImage(self, Name:str):
        Selected:Anime = Anime()
        Selected.UpdateData(Name)
        self.Gui.ImageSlot.ProcessPhoto(Selected)

    
    def GetAnimeStatus(self):
        Name:str = self.__GetEntry(self.AnimeIndex.PrintInfo.EntryIndex.Name)
        Name = self.__FindName(Name)

        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in self.Gui.EntryList[self.AnimeIndex.PrintInfo.EntryIndex.Name].options):
                self.Gui.Text.PrintDisplay(Watch.GetStatus(Name))
                self.__LoadImage(Name)
                self.__ClearEntry(self.AnimeIndex.PrintInfo.EntryIndex.Name)
            else:
                print(f"GetAnimeStatus name not found: {Name} in {self.Gui.EntryList[self.AnimeIndex.PrintInfo.EntryIndex.Name].options}")
        else:
            print(f"GetAnimeStatus path not found: {JsonUtil.TrueName(Name)}")


    def PrintSeason(self):
        SeasonID:str = self.__GetEntry(self.AnimeIndex.PrintSeason.EntryIndex.SeasonID)
        self.Gui.Text.PrintDisplay(Watch.PrintSeason(SeasonID))
        self.__ClearEntry(self.AnimeIndex.PrintSeason.EntryIndex.SeasonID)
    
    def PrintStatusList(self):
        Info:str = self.__GetEntry(self.AnimeIndex.PrintStatusList.EntryIndex.StatusID)
        if (os.path.exists("./Data/AnimeStatusList.json")):
            Status:dict = JsonUtil.LoadJson("./Data/AnimeStatusList.json")
            Filter = self.Gui.AnimeDataLists.GetFilter()
            if (Info != ""):  
                if (Info == "Watching"):
                    NameList:list[str] = Status.get("Watching", [])
                    NewList:list[str] = []
                    
                    for name in NameList:
                        SelectedAnime:Anime = Watch.SelectAnime(name)
                        if (Filter == "All"):
                            NewList.append(name)
                            NewList.append(f" //CurrentEP: {SelectedAnime.EpisodeStatus}, Season: {SelectedAnime.Season}")
                        elif (SelectedAnime.Season == Filter):
                            NewList.append(name)
                            NewList.append(f" //CurrentEP: {SelectedAnime.EpisodeStatus}, Season: {SelectedAnime.Season}")

                    self.Gui.Text.PrintDisplay(NewList)
                    self.__ClearEntry(self.AnimeIndex.PrintStatusList.EntryIndex.StatusID)
                else:
                    StatusList:list[str] = ["Completed", "PlanToWatch", "Dropped"]
                    NameList:list[str] = Status[f"{Info}"]
                    if (Info in StatusList):     
                        if (Filter == "All"):
                            Selected:list[str] = NameList
                            self.Gui.Text.PrintDisplay(Selected)
                            self.__ClearEntry(self.AnimeIndex.PrintStatusList.EntryIndex.StatusID)
                        else:
                            NewList:list[str] = []
                            for name in NameList:
                                SelectedAnime:Anime = Watch.SelectAnime(name)
                                if (SelectedAnime.Season == Filter):
                                    NewList.append(name)

                            self.Gui.Text.PrintDisplay(NewList)
                            self.__ClearEntry(self.AnimeIndex.PrintStatusList.EntryIndex.StatusID)
                    else:
                        print("Status not found")
            else:
                NewStatus:dict[str, list[str]] = {"Watching": [], "Completed": [], "PlanToWatch": [], "Dropped": []}
                for status in Status:
                    NameList:list[str] = Status[f"{status}"]
                    for name in NameList:
                        SelectedAnime:Anime = Watch.SelectAnime(name)
                        if (Filter == "All"):
                            NewStatus[f"{status}"].append(name)
                        elif (SelectedAnime.Season == Filter):
                            NewStatus[f"{status}"].append(name)
                self.Gui.Text.PrintDisplay(NewStatus)
        else:
            print("StatusList path not found")
        

    def OpenMyAnimeListLink(self):
        Name:str = self.__GetEntry(self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name)
        Name = self.__FindName(Name)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in self.Gui.EntryList[self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name].options):
                link:str = Watch.SelectAnime(Name).MyAnimeListLink
                if (link != ""):
                    web.open(link)
                    self.__ClearEntry(self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name)
                else:
                    print("OpenLink anime link is empty")
            else:
                print("OpenLink name not not found")
        else:
            print("OpenLink path not found")


    def PrintSerie(self):
        Name:str = self.__GetEntry(self.AnimeIndex.PrintSerie.EntryIndex.SerieID)
        self.__FindName(Name, True)
        if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(Name)}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(Name)}.json")
            self.Gui.Text.PrintDisplay(Info)
            self.__ClearEntry(self.AnimeIndex.PrintSerie.EntryIndex.SerieID)  
        else:
            print("PrintSerie path not found")
    
    def PrintSeasonCalendar(self):
        SeasonID:str = self.__GetEntry(self.AnimeIndex.PrintCallendar.EntryIndex.SeasonID)
        if (os.path.exists(f"./Data/SeasonsCalendar/{JsonUtil.TrueName(SeasonID)}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/SeasonsCalendar/{JsonUtil.TrueName(SeasonID)}.json")[SeasonID]
            self.Gui.Text.PrintDisplay(Info)
            self.__ClearEntry(self.AnimeIndex.PrintCallendar.EntryIndex.SeasonID)
        else:
            print("PrintSeasonCalendar path not found")

    def OpenSeasonLink(self):
        Season = self.__GetEntry(self.AnimeIndex.OpenSeasonLink.EntryIndex.SeasonID)        
        if (os.path.exists(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")):
            SeasonsLinks:dict = JsonUtil.LoadJson(f"./Data/SeasonsLinks.json")

            if (Season in SeasonsLinks and SeasonsLinks[Season] != ""):
                Link = SeasonsLinks[Season]

                web.open(Link)                
                self.__ClearEntry(self.AnimeIndex.OpenSeasonLink.EntryIndex.SeasonID)
            else:
                print("OpenSeasonLink season not found")
        else:
            print("OpenSeasonLink season path not found")
    
    def OpenWatchLink(self):
        Name = self.__GetEntry(self.AnimeIndex.OpenWatchLink.EntryIndex.Name)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")["Anime"]

            if (Info["WatchLink"] == ""):
                raise Exception("OpenWatchLink: link is empty")
            
            if (Name in self.Gui.EntryList[self.AnimeIndex.OpenWatchLink.EntryIndex.Name].options):
                web.open(Info["WatchLink"])
                self.__ClearEntry(self.AnimeIndex.OpenWatchLink.EntryIndex.Name)
            else:
                raise Exception("OpenWatchLink: name not found")
        else:
            print("OpenWatchLink season path not found")
        
