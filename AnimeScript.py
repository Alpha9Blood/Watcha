import os
import webbrowser as web
from Script.ManageData.Anime.AnimeObj import Anime
from Script.Managers.CustomTypes.CustomEntry import CustomEntry
from Script.GUI_Index import AnimeI
from Script.Utils import JsonUtil
from Script.Utils import Math
from Script.ManageData.Anime.ManageSeasons import SeasonManager
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.ManageData.Anime.AnimeWatcha import Watch
from Script.ManageData.Anime.ManageSeries import SerieManager

class AnimeExecute:
    
    def __init__(self):
        self.AnimeIndex = AnimeI()
    
    def GuiInit(self, window):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = window
    
    
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
        Finds the full name of an anime in the list of anime names.

        Args:
            Name (str): The name of the anime to search for.
            Serie (bool): If the search should be done in the list of series. Defaults to False.
            CustomData (list[str]): A custom list of anime names to search in. Defaults to an empty list.

        Returns:
            str: The full name of the anime.

        Raises:
            Exception: If the anime is not found in the list.
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

        if (Name in List):
            return Name
        
        for var in List:
            if (Name in var.lower()):
                Name = var
                return Name
        
        raise Exception(f"__FindName: anime not found: {Name} in AnimeList")

    #Set

    
    def Add(self):
        Name:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.Name)
        if (Name == ""):
            print("AddAnime: Anime name is empty")
            return
        if (Name in GetAnimeList.AnimeList()):
            print(f"AddAnime: Anime already exists: {Name}")
            return
        
        Status:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.Status)
        if (Status not in GetAnimeList.CurrentStatusTypeList()):
            print("AddAnime: invalid status")
            return

        SeasonName:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.SeasonName)
        if (SeasonName not in SeasonManager.SeasonsOrder):
            print("AddAnime: invalid season")
            return
        
        SeasonYear:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.SeasonYear)
        if (not SeasonYear.isdigit()):
            print("AddAnime: SeasonYear must be a integer number: " + SeasonYear)
            return
        
        MaxEpisode:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.MaxEp)
        if (MaxEpisode != ""):
            try:
                MaxEpisodeI = int(MaxEpisode)
                if (MaxEpisodeI < 0):
                    MaxEpisodeI = 0
            except ValueError:
                raise ValueError("AddAnime: MaxEpisode must be an integer:" + MaxEpisode)
        else:
            MaxEpisodeI = 0
        
        Season:str = f"{SeasonName}_{SeasonYear}"
        Serie:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.Serie)

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
            
    def RemoveAnime(self):
        Name:str = self.__GetEntry(self.AnimeIndex.DeleteAnime.EntryIndex.Name)
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"AnimeRemove not found: ./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            return
        
        Watch.Remove(Name)
        self.__ClearEntry(self.AnimeIndex.DeleteAnime.EntryIndex.Name)
            
    def RemoveLeastAdded(self):   
        Namelist = GetAnimeList.AnimeList()
        if (Namelist == []):
            print("RemoveLeastAdded AnimeList is empty")
            return
        
        Name:str = Namelist[::-1][0]
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"RemoveLeastAdded anime not found: ./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            return
        
        Watch.Remove(Name)

    def AddEppisode(self):
        Name:str = self.__GetEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)
        if (Name == ""):
            print("AddEpisode: name is empty")
            return
        
        OnGoingList:list[str] = GetAnimeList.OnGoingList()
        Name = self.__FindName(Name, CustomData = OnGoingList) 
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"AddEpisode path not found: ./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            return
        
        Watch.UpdateEpisode(Name)
        self.__ClearEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)

    def SetEpisode(self):
        Name:str = self.__GetEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)

        if (Name == ""):
            print("SetEpisode: name is empty")
            return
        
        OnGoingList:list[str] = GetAnimeList.OnGoingList()
        Name = self.__FindName(Name, CustomData = OnGoingList)
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"SetEpisode path not found: ./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            return
        
        Episode:str = self.__GetEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Ep)
        Watch.UpdateEpisode(Name, True, Episode)
        self.__ClearEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Name)
        self.__ClearEntry(self.AnimeIndex.UpdateEpisode.EntryIndex.Ep)
    
    def EditAnimeInfo(self):
        Name:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Name)

        if (Name == ""):
            print("EditAnimeInfo: name is empty")
            return
        
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"EditAnimeInfo anime not found: {Name}")
            return
        
        Status:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Status)
        Score:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Score)
        MaxEp:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.MaxEp)
        Serie:str = self.__GetEntry(self.AnimeIndex.EditInfo.EntryIndex.Serie)

        SeasonName:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.SeasonName)
        if (SeasonName not in SeasonManager.SeasonsOrder):
            print("AddAnime: invalid season")
            return
        
        SeasonYear:str = self.__GetEntry(self.AnimeIndex.AddAnime.EntryIndex.SeasonYear)
        
        if (SeasonYear != ""):
            if (not SeasonYear.isdigit()):
                raise ValueError("AddAnime: SeasonYear must be a integer number: " + SeasonYear)
            
            Season:str = f"{SeasonName}_{SeasonYear}"
            SeasonManager.EditAnimeSeason(Name, Season)

        if (Score != ""):
            Watch.SetScore(Name, Score)
            self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.Score)
        
        if (MaxEp != ""):
            Watch.EditMaxEp(Name, MaxEp)
            self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.MaxEp)

        if (Serie != ""):
            SerieManager.EditAnimeSerie(Name, Serie)
            self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.Serie)
        
        #TODO: Test ordem status
        if (Status != ""):
            Watch.SetCurrentStatus(Name, Status)
            self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.Status)
        
        self.__ClearEntry(self.AnimeIndex.EditInfo.EntryIndex.Name)

    def AddMyAnimeListLink(self):
        Name = self.__GetEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name)
        
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"AddMyAnimeListLink not found:./Data/MangaData/{JsonUtil.TrueName(Name)}.json")
            return
        
        Link = self.__GetEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Link)
        if (Link == ""):
            print("AddMyAnimeListLink link is empty")
            return
        
        if ("https://myanimelist.net/anime/" not in Link):
            print("AddMyAnimeListLink link is not myanimelist")
            return
        
        Watch.UpdateMyAnimeListLink(Name, Link)
        self.Gui.ImageExtractor.StoreExtractedImage(Name, Link)
        self.__ClearEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name)
        self.__ClearEntry(self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Link)
            

    def AddToCalendar(self):
        Name = self.__GetEntry(self.AnimeIndex.AddToCallendar.EntryIndex.Name)
        
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"AddToCalendar not found: ./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            return
        
        Day = self.__GetEntry(self.AnimeIndex.AddToCallendar.EntryIndex.Day)
        Watch.CreateCalendar(Name, Day)
        self.__ClearEntry(self.AnimeIndex.AddToCallendar.EntryIndex.Name)

    def SetWatchLink(self):
        Name = self.__GetEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Name)
        
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"SetWatchLink path not found: ./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            return

        Link = self.__GetEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Link)
        if (Link == ""):
            print("SetWatchLink link is empty")
            return
        
        Watch.AddWatchLink(Name, Link)
        self.__ClearEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Name)
        self.__ClearEntry(self.AnimeIndex.SetWatchLink.EntryIndex.Link)      


    #Get


    def OpenMALHomePage(self):
        web.open("https://myanimelist.net")

    def PrintAnimeList(self):
        self.Gui.Text.PrintDisplay(GetAnimeList.AnimeList())        

    def PrintSerieList(self):
        self.Gui.Text.PrintDisplay(GetAnimeList.SerieList())
    
    def __LoadImage(self, Name:str, posXY:tuple[int, int] = (1170, 220), CoverSize:tuple = (200, 300)):
        Selected:Anime = Watch.SelectAnime(Name)
        self.Gui.ImageSlot.ProcessPhoto(Selected, posXY, CoverSize)
    
    def GetAnimeStatus(self):
        Name:str = self.__GetEntry(self.AnimeIndex.PrintInfo.EntryIndex.Name)

        if (Name == ""):
            print("SetEpisode: name is empty")
            return
        
        Name = self.__FindName(Name)

        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"GetAnimeStatus path not found: {JsonUtil.TrueName(Name)}")
            return
        
        if (Name not in self.Gui.EntryList[self.AnimeIndex.PrintInfo.EntryIndex.Name].options):
            print(f"GetAnimeStatus {Name = } not found in options")
            return
        
        self.Gui.Text.PrintDisplay(Watch.GetStatus(Name))
        self.__LoadImage(Name)
        self.__ClearEntry(self.AnimeIndex.PrintInfo.EntryIndex.Name)

    def PrintSeason(self):
        SeasonID:str = self.__GetEntry(self.AnimeIndex.PrintSeason.EntryIndex.SeasonID)

        if (not os.path.exists(f"./Data/SeasonsCalendar/{JsonUtil.TrueName(SeasonID)}.json")):
            print(f"Invalid {SeasonID = }")
            return
        
        self.Gui.Text.PrintDisplay(Watch.PrintSeason(SeasonID))
        self.__ClearEntry(self.AnimeIndex.PrintSeason.EntryIndex.SeasonID)
    
    def PrintStatusList(self):
        Info:str = self.__GetEntry(self.AnimeIndex.PrintStatusList.EntryIndex.StatusID)
        if (not os.path.exists("./Data/AnimeStatusList.json")):
            print(f"StatusList path: ./Data/AnimeStatusList.json not found")
            return
        
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
                if (Info not in StatusList):
                    print("Status not found")
                    return
                
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
            
    def OpenMyAnimeListLink(self):
        Name:str = self.__GetEntry(self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name)

        if (Name == ""):
            print("SetEpisode: name is empty")
            return
        
        Name = self.__FindName(Name)
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print("OpenLink path not found")
            return
        
        if (Name not in self.Gui.EntryList[self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name].options):
            print("OpenLink name not found")
            return
        
        link:str = Watch.SelectAnime(Name).MyAnimeListLink
        if (link == ""):
            print("OpenLink anime link is empty")
            return
        
        web.open(link)
        self.__ClearEntry(self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name)

    def PrintSerie(self):
        Name:str = self.__GetEntry(self.AnimeIndex.PrintSerie.EntryIndex.SerieID)

        if (Name == ""):
            print("SetEpisode: name is empty")
            return
        
        self.__FindName(Name, True)
        if (not os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(Name)}.json")):
            print("PrintSerie path not found")
            return
    
        Info:dict = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(Name)}.json")
        self.Gui.Text.PrintDisplay(Info)
        self.__ClearEntry(self.AnimeIndex.PrintSerie.EntryIndex.SerieID)  
    
    def PrintSeasonCalendar(self):
        SeasonID:str = self.__GetEntry(self.AnimeIndex.PrintCallendar.EntryIndex.SeasonID)
        if (not os.path.exists(f"./Data/SeasonsCalendar/{JsonUtil.TrueName(SeasonID)}.json")):
            print("PrintSeasonCalendar path not found")
            return
        
        Info:dict = JsonUtil.LoadJson(f"./Data/SeasonsCalendar/{JsonUtil.TrueName(SeasonID)}.json")[SeasonID]
        self.Gui.Text.PrintDisplay(Info)
        self.__ClearEntry(self.AnimeIndex.PrintCallendar.EntryIndex.SeasonID)

    def OpenSeasonLink(self):
        Season = self.__GetEntry(self.AnimeIndex.OpenSeasonLink.EntryIndex.SeasonID)        
        if (not os.path.exists(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")):
            print("OpenSeasonLink season path not found")
            return
        
        SeasonsLinks:dict = JsonUtil.LoadJson(f"./Data/SeasonsLinks.json")[str(SeasonManager.GetSeasonYear(Season))]
        if (Season not in SeasonsLinks):
            print("OpenSeasonLink season not found")
            return
        
        Link = SeasonsLinks[Season]
        if (Link == ""):
            print("OpenSeasonLink link is empty")
            return

        web.open(Link)
        self.__ClearEntry(self.AnimeIndex.OpenSeasonLink.EntryIndex.SeasonID)
    
    def OpenWatchLink(self):
        Name = self.__GetEntry(self.AnimeIndex.OpenWatchLink.EntryIndex.Name)
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print("OpenWatchLink season path not found")
            return
        
        Info:dict = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")["Anime"]

        if (Info["WatchLink"] == ""):
            print("OpenWatchLink: link is empty")
            return
        
        if (Name not in self.Gui.EntryList[self.AnimeIndex.OpenWatchLink.EntryIndex.Name].options):
            print("OpenWatchLink: name not found")
            return

        web.open(Info["WatchLink"])
        self.__ClearEntry(self.AnimeIndex.OpenWatchLink.EntryIndex.Name)



    def ViewAll(self):
        Animelist:list[str] = GetAnimeList.AnimeList()

        self.Gui.Presets.ViewList.SelectList("anime" , Animelist)
        self.Gui.Presets.ViewList.CurrentPage += 2
        
        Yposion:int = 120
        inlineOptions:int = 5
        self.Gui.Presets.ViewList.SetViewLines(self.Gui.Presets.ViewList.SelectedList)

        self.Gui.Presets.ViewList.ViewReset()

        TextList:list[tuple[str,int, int]] = []
        
        index:int = self.Gui.Presets.ViewList.ViewIndex
        for i in range(0, 2):
            for j in range(0, inlineOptions):
                if (index < len(self.Gui.Presets.ViewList.SelectedList)):
                    Xposion = 100 + j * 300
                    self.__LoadImage(self.Gui.Presets.ViewList.SelectedList[index], (Xposion, Yposion), (150, 225))
                    TextList.append((self.Gui.Presets.ViewList.SelectedList[index], Xposion, Yposion + 250))
                    index += 1
                else:
                    break

            Yposion += 300
        
        for name, Xposion, Yposion in TextList:
            self.Gui.Text.CreateText(name, Xposion, CustomYPosition = Yposion, WidthHeight=(20, 1))

        self.Gui.Presets.ViewList.PreviousPage = inlineOptions * 4
        self.Gui.Presets.ViewList.ViewIndex = index

    def ViewPrevious(self):
        self.Gui.Presets.ViewList.ViewIndex -= self.Gui.Presets.ViewList.PreviousPage
        self.Gui.Presets.ViewList.CurrentPage -= 4
        self.ViewAll()