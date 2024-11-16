import os , sys
from tkinter import ttk
sys.path.append(os.getcwd())
from Script.Managers.CustomTypes.CustomEntry import CustomEntry
import webbrowser as web
from Script.GUI_Index import *
from Script.Utils import JsonUtil
from Script.Data.AnimeLists import GetAnimeList

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
        self.Path = ""    
    
    def CurrentEpisodeStatus(self) -> str:
        if (self.Episode > 0 and self.MaxEpisodes != 0):
            return f"{self.Episode}/{self.MaxEpisodes}"
        else:
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
            if (self.MaxEpisodes > 0):
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
                print("Store directory not found")
        else:
            if (self.Name != ""):
                JsonUtil.CreateJson(Data, Path)
            else:
                print("StoreData anime name not found")
    
    def UpdateData(self, Name:str, UpdateStatus:bool = True):
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Info:dict = self.GetData(Name)
            self.Name = Info["Name"]
            self.EpisodeStatus = Info["EpisodesStatus"] 
            self.CurrentStatus = Info["Status"]
            self.Season = Info["Season"]
            self.MaxEpisodes = Info["MaxEpisodes"]
            self.Episode = Info["Episode"]
            self.SerieName = Info["SerieName"]
            self.MyAnimeListLink = Info["MyAnimeListLink"]  
            self.Score = Info["Score"]
            self.Path = self.DirectoryPath()
            if (UpdateStatus):
                self.UpdateStatus()
        else:
            print("UpdateData anime not found")
    
    
  
    def AnimeData(self) -> dict:
        return {
            "Anime": {
                "Name": JsonUtil.CursedStoreName(self.Name),
                "EpisodesStatus": self.CurrentEpisodeStatus(),
                "Status": self.CurrentStatus,
                "Season": self.Season,
                "MaxEpisodes": self.MaxEpisodes,
                "Episode": self.Episode,
                "SerieName": JsonUtil.CursedStoreName(self.SerieName),
                "MyAnimeListLink": self.MyAnimeListLink,
                "Score": self.Score
            }
        }




class Watcha:

    def __init__(self):
        self.selected:Anime = Anime()
    
    def SelectAnime(self, Name:str) -> Anime:
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)
            return self.selected
        else:
            print("SelectAnime anime not found")
            return self.selected
    
    def UpdateStatusList(self, Selected:Anime, UpdateStatus:bool = True):
        Name = Selected.Name
        if (os.path.exists(f"./Data/AnimeStatusList.json")):
            Status:dict[str, list[str]] = GetAnimeList.AnimeStatusList()
            SelectedList:list[str] = Status[Selected.CurrentStatus]

            if (UpdateStatus):
                Selected.UpdateStatus()

            if (Name in SelectedList):
                return
            else:
                SelectedList.append(Name)
            
            for status in Status:
                if (status != Selected.CurrentStatus):
                    if (Name in Status[status]):
                        Status[status].remove(Name)            

            JsonUtil.UpdateJson(Status, f"./Data/AnimeStatusList.json")
        else:
            Status:dict[str, list[str]] = {"Watching": [], "Completed": [], "PlanToWatch": [], "Dropped": []}
            Status[Selected.CurrentStatus].append(Name)
            JsonUtil.CreateJson(Status, f"./Data/AnimeStatusList.json")
    
    #
    
    def GetStatus(self, Name:str) -> dict:
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")["Anime"]
            PrintInfo:dict[str, str] = {
                "Name": Info["Name"],
                "EpisodesStatus": Info["EpisodesStatus"],
                "Status": Info["Status"],
                "Season": Info["Season"],
                "SerieName": Info["SerieName"],
                "Score": Info["Score"]
            }
            Score:float = float(PrintInfo["Score"])
            if (Score == 0):
                PrintInfo["Score"] = "N/A"
            return PrintInfo
        else:
            print("GetStatus Anime not found")
            return {}

    def GetCurrentStatus(self, currentStatus:str = "") -> list[str] | dict[str, list[str]]:
        if (os.path.exists(f"./Data/AnimeStatusList.json")):        
            if (currentStatus == ""):
                CurrentStatusList:dict[str, list[str]] = GetAnimeList.AnimeStatusList()
                return CurrentStatusList
            else:
                StatusList:list[str] = GetAnimeList.AnimeCurrentStatusList(currentStatus)
                return StatusList
        else:
            print("GetCurrentStatus Anime not found")
            return {}
            

    def UpdateEpisode(self, Name:str, Set:bool = False, Episode:int = 0):
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name, UpdateStatus = False)
            if (Set):
                self.selected.Episode = Episode
            else:
                self.selected.Episode += 1
            self.UpdateStatusList(self.selected)
            self.selected.StoreData()
        else:
            print("UpdateEpisode anime not found")

    def SetCurrentStatus(self, Name:str, Status:str):
        """
        Sets the current status of an anime to the specified status.

        Args:
            Name (str): The name of the anime.
            Status (str): The status to set the anime to.

        Raises:
            FileNotFoundError: If the anime data file for the specified anime does not exist.

        Side Effects:
            - Updates the anime data file by setting the current status of the anime to the specified status.
            - If the anime is in the current status list, it removes the anime from the list.
            - If the anime is not in the current status list, it sets the current status of the anime to "Error".
        """
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name, UpdateStatus = False)
            self.selected.CurrentStatus = Status
            self.UpdateStatusList(self.selected, False)
            self.selected.StoreData(UpdateStatus = False)
        else:
            print("SetCurrentStatus not found")

    def SetScore(self, Name:str, Score:float):
        
        """
        Sets the score of an anime to the specified score.

        Args:
            Name (str): The name of the anime.
            Score (float): The score to set the anime to.

        Raises:
            FileNotFoundError: If the anime data file for the specified anime does not exist.

        Side Effects:
            - Updates the anime data file by setting the score of the anime to the specified score.
        """
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)
            self.selected.Score = Score
            self.selected.StoreData()
        else:
            print("SetScore not found")
    
    def Remove(self, Name:str):      
        """
        Removes an anime from the list of anime and removes its data file.

        Args:
            Name (str): The name of the anime to remove.

        Raises:
            FileNotFoundError: If the anime data file for the specified anime does not exist.

        Side Effects:
            - Removes the anime from the list of anime in the current season.
            - If the anime is the only one in the season, removes the season from the list of seasons.
            - Removes the anime from the list of anime in the serie.
            - If the anime is the only one in the serie, removes the serie from the list of series.
            - Removes the anime from the list of anime in the current status.
            - Removes the anime data file.
        """
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)

            if (os.path.exists(f"./Data/Seasons/{self.selected.Season}.json")):
                Season:list = JsonUtil.LoadJson(f"./Data/Seasons/{self.selected.Season}.json")
                if (Name in Season):
                    Season.remove(Name)
                else:
                    print("Anime not found in season list")

                if (len(Season) == 0):
                    os.remove(f"./Data/Seasons/{self.selected.Season}.json")
                else:
                    JsonUtil.UpdateJson(Season, f"./Data/Seasons/{self.selected.Season}.json")
            
            if (os.path.exists("./Data/ListedAnimeSeasons.json")):
                ListedSeasons:list[str] = JsonUtil.LoadJson(f"./Data/ListedAnimeSeasons.json")
                if (self.selected.Season in ListedSeasons):
                    if (len(GetAnimeList.GetSeason(self.selected.Season)) == 0):
                        ListedSeasons.remove(self.selected.Season)
                else:
                    print("Anime not found in season list")

                if (len(ListedSeasons) == 0):
                    os.remove(f"./Data/ListedAnimeSeasons.json")
                else:
                    JsonUtil.UpdateJson(ListedSeasons, f"./Data/ListedAnimeSeasons.json")
                    
            if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")):
                SerieList:list = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")
                
                if (Name in SerieList):
                    SerieList.remove(Name)
                else:
                    print("Anime not found in serie list")

                if (len(SerieList) == 0):
                    os.remove(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")
                else:
                    JsonUtil.UpdateJson(SerieList, f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")
                
                if (os.path.exists("./Data/ListedSeries.json")):
                    ListedSeries:list = JsonUtil.LoadJson(f"./Data/ListedSeries.json")
                    
                    if (not os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json") and self.selected.SerieName in ListedSeries):
                        ListedSeries.remove(self.selected.SerieName)
                    else:
                        print("Serie not found in serie list")

                    if (len(ListedSeries) == 0):
                        os.remove("./Data/ListedSeries.json")
                    else:
                        JsonUtil.UpdateJson(ListedSeries, "./Data/ListedSeries.json")
            else:
                print("RemoveSerieData not found")
            
            AnimeStatusListInfo:dict[str, list[str]] = GetAnimeList.AnimeStatusList()
            Info:list[str] = AnimeStatusListInfo[self.selected.CurrentStatus]
            if (Name in Info):
                Info.remove(Name)
                JsonUtil.UpdateJson(AnimeStatusListInfo, "./Data/AnimeStatusList.json")
            else:
                print("Anime not found in status list")
            
            if (os.path.exists(f"./Data/ListedAnimes.json")):
                ListedAnimes:list = JsonUtil.LoadJson(f"./Data/ListedAnimes.json")
                if (Name in ListedAnimes):
                    ListedAnimes.remove(Name)
                else:
                    print("Anime not found in anime list")

                if (len(ListedAnimes) == 0):
                    os.remove("./Data/ListedAnimes.json")
                else:
                    JsonUtil.UpdateJson(ListedAnimes, "./Data/ListedAnimes.json")

            os.remove(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
        else:
            print("RemoveAnime not found")

    def SetNewAnime(self, name:str, maxpisodes:int, currentstatus:str, Season:str, seriename:str = ""):
        """
        Creates a new anime object and saves it to the database.

        Args:
            name (str): The name of the anime.
            maxpisodes (int): The maximum number of episodes for the anime.
            currentstatus (str): The current status of the anime.
            Season (str): The season of the anime.
            seriename (str, optional): The name of the series the anime belongs to. Defaults to "".

        Raises:
            FileNotFoundError: If the file "./Data/ListedSeries.json" or "./Data/SerieData/{JsonUtil.TrueName(seriename)}.json" does not exist.

        Side Effects:
            - Appends the anime name to the "./Data/ListedSeries.json" file if the series name is not empty and the series name is not already in the file.
            - Appends the anime name to the "./Data/SerieData/{JsonUtil.TrueName(seriename)}.json" file if the anime name is not already in the file.
            - Sets the "SerieName" attribute of the "NewAnime" object to the series name if the series name is not empty.
            - Appends the anime name to the "./Data/Seasons/{NewAnime.Season}.json" file if the anime name is not already in the file.
            - Creates a new empty list and appends the anime name to it if the file "./Data/Seasons/{NewAnime.Season}.json" does not exist.
            - Appends the anime name to the "./Data/ListedAnimes.json" file if the anime name is not already in the file.
            - Creates a new empty list and appends the anime name to it if the file "./Data/ListedAnimes.json" does not exist.
            - Saves the "NewAnime" object data to the "./Data/AnimeData/{JsonUtil.TrueName(name)}.json" file.
            - Calls the "UpdateData" method with the anime name as an argument.
        """
        NewAnime = Anime(name, maxpisodes, currentstatus, Season)

        if (not seriename == ""):
            
            if (os.path.exists(f"./Data/ListedSeries.json")):
                SerieList:list = JsonUtil.LoadJson("./Data/ListedSeries.json")
                if (seriename not in SerieList):   
                    SerieList.append(seriename)
                    JsonUtil.UpdateJson(SerieList, "./Data/ListedSeries.json")
                else:
                    print("Serie already in list")
            else:
                SerieNameList:list = [seriename]
                JsonUtil.CreateJson(SerieNameList, "./Data/ListedSeries.json")
            
            if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")):
                SerieDataList:list = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")
                if (name not in SerieDataList):
                    SerieDataList.append(name)
                    JsonUtil.UpdateJson(SerieDataList, f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")
            else:
                AnimeNameList:list = [name]
                JsonUtil.CreateJson(AnimeNameList, f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")

            NewAnime.SerieName = seriename
        
        if (os.path.exists(f"./Data/Seasons/{NewAnime.Season}.json")):
            SeasonList:list = JsonUtil.LoadJson(f"./Data/Seasons/{NewAnime.Season}.json")
            if (NewAnime.Name not in SeasonList):
                SeasonList.append(NewAnime.Name)
                JsonUtil.UpdateJson(SeasonList, f"./Data/Seasons/{NewAnime.Season}.json")
            else:
                print("Season already in list")
        else:
            SeasonList:list = [NewAnime.Name]
            JsonUtil.CreateJson(SeasonList, f"./Data/Seasons/{NewAnime.Season}.json")
        
        if (os.path.exists(f"./Data/ListedAnimeSeasons.json")):
            ListedSeasons:list[str] = JsonUtil.LoadJson(f"./Data/ListedAnimeSeasons.json")
            if (NewAnime.Season not in ListedSeasons):
                ListedSeasons.append(NewAnime.Season)
                JsonUtil.UpdateJson(ListedSeasons, f"./Data/ListedAnimeSeasons.json")
        else:
            ListedSeasons:list[str] = [NewAnime.Season]
            JsonUtil.CreateJson(ListedSeasons, f"./Data/ListedAnimeSeasons.json")

        if (os.path.exists("./Data/AnimeStatusList.json")):
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/AnimeStatusList.json")
            Status:list[str] = StatusList[NewAnime.CurrentStatus]
            if (NewAnime.Name not in Status):
                Status.append(NewAnime.Name)
                JsonUtil.UpdateJson(StatusList, "./Data/AnimeStatusList.json")
            else:
                print("Status already in list")
        else:
            StatusList:dict[str, list[str]] = {"Watching": [], "Completed": [], "PlanToWatch": [], "Dropped": []}
            StatusList[NewAnime.CurrentStatus].append(NewAnime.Name)
            JsonUtil.CreateJson(StatusList, "./Data/AnimeStatusList.json")
        
        if (os.path.exists(f"./Data/ListedAnimes.json")):
            AnimeList:list = JsonUtil.LoadJson(f"./Data/ListedAnimes.json")
            if (NewAnime.Name not in AnimeList):
                AnimeList.append(NewAnime.Name)
                JsonUtil.UpdateJson(AnimeList, f"./Data/ListedAnimes.json")
            else:
                print("Anime already in list")
        else:
            AnimeList:list = [NewAnime.Name]
            JsonUtil.CreateJson(AnimeList, f"./Data/ListedAnimes.json")

        NewAnime.StoreData(True)

    def UpdateMyAnimeListLink(self, Name, Link):
        """
        Updates the MyAnimeList link for a given anime.

        Args:
            Name (str): The name of the anime.
            Link (str): The new MyAnimeList link.

        Notes:
            This function checks if the anime's data file exists. If it does, it updates the MyAnimeList link,
            saves the updated data to the file, and prints an error message if the file does not exist.
        """
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name, False)
            self.selected.MyAnimeListLink = Link
            self.selected.StoreData()
        else:
            print("UpdateMyAnimeListLink not found")


    def PrintSeason(self, SeasonID:str) -> str:
        """
        Prints the season data for a given SeasonID.

        Args:
            SeasonID (str): The ID of the season to print.

        Returns:
            tuple: A tuple containing the SeasonID and a list of season data if the season file exists.
            str: A string indicating that the season file was not found if it does not exist.
        """
        if (os.path.exists(f"./Data/Seasons/{SeasonID}.json")):
            List:list = JsonUtil.LoadJson(f"./Data/Seasons/{SeasonID}.json")
            return f"{SeasonID}: {List}"
        else:
            print("PrintSeason path not found")
            return ""
            

    def AddToSerie(self, Seriename, Animename):
        """
        Adds an anime to a specified series.

        Args:
            Seriename (str): The name of the series.
            Animename (str): The name of the anime.

        This function checks if the series and anime data files exist. If they do, the anime is added to the specified series.
        If the files do not exist, a "FileNotFoundError" is raised.
        """
        if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(Seriename)}.json") and os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Animename)}.json")):
            List:list = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(Seriename)}.json")
            List.append(Animename)
            JsonUtil.UpdateJson(List, f"./Data/SerieData/{JsonUtil.TrueName(Seriename)}.json")
        else:
            print("AddToSerie not found")

    def CreateCalendar(self, Name:str, Day:str):    
        """
        Creates a calendar for a given anime and day.

        Args:
            Name (str): The name of the anime.
            Day (str): The day of the week. Can be one of the following: "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
            
        Notes:
            This function first checks if the anime's season calendar exists. If not, it creates one.
            Then, it checks if the anime's data exists. If it does, it adds the anime to the corresponding day in the calendar.
            If the anime is already in the calendar or if the anime's data does not exist, it prints an error message.
        """
        AnimeID:Anime = self.SelectAnime(Name)

        if (not os.path.exists(f"./Data/SeasonsCalendar/{AnimeID.Season}.json")):
            if (AnimeID.Season != ""):
                Calendar:dict[str, dict[str, list[str]]] = {
                    f"{AnimeID.Season}":  {
                        "Monday": [],
                        "Tuesday": [],
                        "Wednesday": [],
                        "Thursday": [],
                        "Friday": [],
                        "Saturday": [],
                        "Sunday": []
                    }
                }
                
                JsonUtil.CreateJson(Calendar, f"./Data/SeasonsCalendar/{AnimeID.Season}.json")
            else:
                print("CreateCalendar AnimeID season not found")

        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Days:list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
            SeasonDict:dict[str, list[str]] = JsonUtil.LoadJson(f"./Data/SeasonsCalendar/{AnimeID.Season}.json")
            Monday:list[str] = SeasonDict.get("Monday", [])
            Tuesday:list[str] = SeasonDict.get("Tuesday", [])
            Wednesday:list[str] = SeasonDict.get("Wednesday", [])
            Thursday:list[str] = SeasonDict.get("Thursday", [])
            Friday:list[str] =  SeasonDict.get("Friday", [])
            Saturday:list[str] = SeasonDict.get("Saturday", [])
            Sunday:list[str] = SeasonDict.get("Sunday", [])
            DaysList:list[list[str]] = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

            if (Name not in DaysList[Days.index(Day)]):

                DaysList[Days.index(Day)].append(AnimeID.Name)

                Calendar = {
                    f"{AnimeID.Season}":  {
                        "Monday": Monday,
                        "Tuesday": Tuesday,
                        "Wednesday": Wednesday,
                        "Thursday": Thursday,
                        "Friday": Friday,
                        "Saturday": Saturday,
                        "Sunday": Sunday
                    }
                }
                JsonUtil.UpdateJson(Calendar, f"./Data/SeasonsCalendar/{AnimeID.Season}.json")
            else:
                print("CreateCalendar add not found or already exists")
        else:
            print("CreateCalendar name path not found")
    
    def GetSeason(self, Season:str) -> list[str]:
        if (os.path.exists(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")):
            Info:list[str] = JsonUtil.LoadJson(f"./Data/Seasons/{JsonUtil.TrueName(Season)}.json")
            return Info
        else:
            print("GetSeason anime not found")
            return []
        
        
Watch = Watcha()




class WatchaExecute:
    
    
    def __init__(self):
        self.SetEntryIndex = AnimeSet.EntryIndex
        self.GetEntryIndex = AnimeGet.EntryIndex
    
    def GuiInit(self, Janela):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = Janela
    
    
    #Tools
    def ClearEntry(self, Index:int = -1, IndexList:list[int] = []):           
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

    def GetEntry(self, index:int) -> str:
        EntryList:list[CustomEntry] = self.Gui.EntryList
        return EntryList[index].get()
        
    def FindName(self, Name:str, Serie:bool = False) -> str:
        """
        Finds an anime by name in the list of anime stored in the "./Data/ListedAnimes.json" file.

        Args:
            Name (str): The name of the anime to search for.

        Returns:
            str: The name of the anime found, or an empty string if not found.

        Notes:
            This function is case-insensitive.
        """
        if (Serie):
            List:list[str] = GetAnimeList.SerieList()
            Result:str = ""
            for i in range(len(List)):
                Selected:str = List[i]
                if (Name.lower() in Selected.lower()):
                    Result = List[i]
                    return Result
        else:
            List:list[str] = GetAnimeList.AnimeList()
            Result:str = ""
            for i in range(len(List)):
                Selected:str = List[i]
                if (Name.lower() in Selected.lower()):
                    Result = List[i]
                    return Result
        
        if (Result == ""):
            print("FindName Anime not found")
        
        return Result
    
    


    #ExecFuncs


    #Set

    
    

    def Add(self):
        Name:str = self.GetEntry(self.SetEntryIndex.AddAnime.Name)
        if (Name != ""):
            Ep:str = self.GetEntry(self.SetEntryIndex.AddAnime.MaxEp)
            try:
                MaxEpisode:int = 0
                if (Ep != ""):
                    MaxEpisode:int = int(Ep)
                    if (MaxEpisode < 0):
                        MaxEpisode = 0
            except ValueError:
                print("MaxEpisodes must be an integer")
                return
            Status:str = self.GetEntry(self.SetEntryIndex.AddAnime.Status)
            Season:str = self.GetEntry(self.SetEntryIndex.AddAnime.Season)
            Serie:str = self.GetEntry(self.SetEntryIndex.AddAnime.Serie)

            def AddIsComplete() -> bool:
                if (MaxEpisode >= 0 and Status != "" and Season != ""):
                    return True
                else:
                    return False
            
            NameList:list[str] = GetAnimeList.AnimeList()
            if (Name not in NameList):
                if (AddIsComplete()):
                    Watch.SetNewAnime(Name, MaxEpisode, Status, Season, Serie)
                    Entrys:list[int] = [self.SetEntryIndex.AddAnime.Name,self.SetEntryIndex.AddAnime.MaxEp,self.SetEntryIndex.AddAnime.Status,self.SetEntryIndex.AddAnime.Season,self.SetEntryIndex.AddAnime.Serie]
                    self.ClearEntry(IndexList= Entrys)
                else:
                    print("AddInfo is not completed")
            else:
                print("Anime already exists")
        else:
            print("Anime name is empty")
    
    def RemoveAnime(self):
        Name:str = self.GetEntry(self.SetEntryIndex.DeleteAnime.Name)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.Remove(Name)
            self.ClearEntry(self.SetEntryIndex.DeleteAnime.Name)
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
        Name:str = self.GetEntry(self.SetEntryIndex.AddEpisode.Name)
        Name = self.FindName(Name)
        
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in GetAnimeList.OnGoingList()):
                Watch.UpdateEpisode(Name)
                self.ClearEntry(self.SetEntryIndex.AddEpisode.Name)
            else:
                print("AddEpisode is not in OnGoingList")
        else:
            print("AddEpisode path not found")

    def SetEpisode(self):
        Name:str = self.GetEntry(self.SetEntryIndex.AddEpisode.Name)
        try:
            SetEP:int = int(self.GetEntry(self.SetEntryIndex.AddEpisode.Ep))
        except ValueError:
            print("SetEpisode EP must be an integer number")
            return
        Name = self.FindName(Name)

        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in GetAnimeList.OnGoingList()):
                Watch.UpdateEpisode(Name, True, SetEP)
                self.ClearEntry(self.SetEntryIndex.AddEpisode.Name)
                self.ClearEntry(self.SetEntryIndex.AddEpisode.Ep)
            else:
                print("SetEpisode is not in OnGoingList")
        else:
            print("SetEpisode path not found")
    
    def UpdateScore(self):
        Name = self.GetEntry(self.SetEntryIndex.UpdateScore.Name)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Scor:str = self.GetEntry(self.SetEntryIndex.UpdateScore.Score)

            if (Scor != ""):
                try:
                    Score:float = float(Scor)
                    if (Score >= 0 and Score <= 10):
                        Watch.SetScore(Name, Score)
                        self.ClearEntry(self.SetEntryIndex.UpdateScore.Name)
                        self.ClearEntry(self.SetEntryIndex.UpdateScore.Score)
                    else:
                        print("UpdateScore Score must be between 0 and 10")
                except ValueError:
                    print("UpdateScore Score must be a integer number")
            else:
                print("UpdateScore Score is empty")        
        else:
            print("UpdateScore not found")
              

    def OverrideCurrentStatus(self):
        Name:str = self.GetEntry(self.SetEntryIndex.SetCurrentStatus.Name)
        Status:str = self.GetEntry(self.SetEntryIndex.SetCurrentStatus.Status)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.SetCurrentStatus(Name, Status)
            self.ClearEntry(self.SetEntryIndex.SetCurrentStatus.Name)
            self.ClearEntry(self.SetEntryIndex.SetCurrentStatus.Status)
        else:
            print("OverrideCurrentStatus not found")

    def AddMyAnimeListLink(self):
        Name = self.GetEntry(self.SetEntryIndex.MyAnimeListLink.Name)
        Link = self.GetEntry(self.SetEntryIndex.MyAnimeListLink.Link)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.UpdateMyAnimeListLink(Name, Link)
            self.ClearEntry(self.SetEntryIndex.MyAnimeListLink.Name)
            self.ClearEntry(self.SetEntryIndex.MyAnimeListLink.Link)
        else:
            print("AddMyAnimeListLink not found")


    def AddToCalendar(self):
        Name = self.GetEntry(self.SetEntryIndex.AddToCallendar.Name)
        Day = self.GetEntry(self.SetEntryIndex.AddToCallendar.Day)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            Watch.CreateCalendar(Name, Day)
            self.ClearEntry(self.SetEntryIndex.AddToCallendar.Name)
            """ self.ClearEntry(self.SetEntryIndex.AddToCallendar.Day) """
        else:
            print("AddToCalendar not found")

    def SetSeasonLink(self):
        SeasonID = self.GetEntry(self.SetEntryIndex.SetSeasonLink.SeasonID)
        Link = self.GetEntry(self.SetEntryIndex.SetSeasonLink.Link)
        if (os.path.exists(f"./Data/Seasons/{JsonUtil.TrueName(SeasonID)}.json")):
            Info:dict  = {f"{SeasonID}": Link}
            if (os.path.exists("./Data/SeasonsLinks.json")):
                Seasonslinks:dict = JsonUtil.LoadJson("./Data/SeasonsLinks.json")
                if (SeasonID not in Seasonslinks):
                    JsonUtil.AddToDictJson(Info, "./Data/SeasonsLinks.json")
                    self.ClearEntry(self.SetEntryIndex.SetSeasonLink.SeasonID)
                    self.ClearEntry(self.SetEntryIndex.SetSeasonLink.Link)
                else:
                    print("SetSeasonLink Name already exist")
            else:
                JsonUtil.CreateJson(Info, "./Data/SeasonsLinks.json")
                self.ClearEntry(self.SetEntryIndex.SetSeasonLink.SeasonID)
                self.ClearEntry(self.SetEntryIndex.SetSeasonLink.Link)
        else:
            print("SetSeasonLink season path not found")
              


    #Get

    def OpenMyAnimeList(self):
        web.open("https://myanimelist.net")

    def PrintAnimeList(self):
        self.Gui.Text.PrintDisplay(GetAnimeList.AnimeList())        

    def PrintSerieList(self):
        self.Gui.Text.PrintDisplay(GetAnimeList.SerieList())

    
    def GetAnimeStatus(self):
        Name:str = self.GetEntry(self.GetEntryIndex.GetStatus.Name)
        Name = self.FindName(Name)

        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.Gui.Text.PrintDisplay(Watch.GetStatus(Name))
            self.ClearEntry(self.GetEntryIndex.GetStatus.Name)
        else:
            print(f"GetAnimeStatus path not found: {JsonUtil.TrueName(Name)}")


    def PrintSeason(self):
        SeasonID:str = self.GetEntry(self.GetEntryIndex.PrintSeason.SeasonID)
        self.Gui.Text.PrintDisplay(Watch.PrintSeason(SeasonID))
        self.ClearEntry(self.GetEntryIndex.PrintSeason.SeasonID)
    
    def PrintStatusList(self):
        Info:str = self.GetEntry(self.GetEntryIndex.PrintStatusList.StatusID)
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
                    self.ClearEntry(self.GetEntryIndex.PrintStatusList.StatusID)
                else:
                    StatusList:list[str] = ["Completed", "PlanToWatch", "Dropped"]
                    NameList:list[str] = Status[f"{Info}"]
                    if (Info in StatusList):     
                        if (Filter == "All"):
                            Selected:list[str] = NameList
                            self.Gui.Text.PrintDisplay(Selected)
                            self.ClearEntry(self.GetEntryIndex.PrintStatusList.StatusID)
                        else:
                            NewList:list[str] = []
                            for name in NameList:
                                SelectedAnime:Anime = Watch.SelectAnime(name)
                                if (SelectedAnime.Season == Filter):
                                    NewList.append(name)

                            self.Gui.Text.PrintDisplay(NewList)
                            self.ClearEntry(self.GetEntryIndex.PrintStatusList.StatusID)
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
        

    def OpenLink(self):
        Name:str = self.GetEntry(self.GetEntryIndex.OpenLink.Name)
        Name = self.FindName(Name)
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in GetAnimeList.AnimeList()):
                link:str = Watch.SelectAnime(Name).MyAnimeListLink
                if (link != ""):
                    web.open(link)
                    self.ClearEntry(self.GetEntryIndex.OpenLink.Name)
                else:
                    print("OpenLink anime link is empty")
            else:
                print("OpenLink name not not found")
        else:
            print("OpenLink path not found")

    def PrintSerie(self):
        Name:str = self.GetEntry(self.GetEntryIndex.PrintSerie.SerieID)
        self.FindName(Name, True)
        if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(Name)}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(Name)}.json")
            self.Gui.Text.PrintDisplay(Info)
            self.ClearEntry(self.GetEntryIndex.PrintSerie.SerieID)
        else:
            print("PrintSerie path not found")
    
    def PrintSeasonCalendar(self):
        SeasonID:str = self.GetEntry(self.GetEntryIndex.PrintCallendar.SeasonID)
        if (os.path.exists(f"./Data/SeasonsCalendar/{JsonUtil.TrueName(SeasonID)}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/SeasonsCalendar/{JsonUtil.TrueName(SeasonID)}.json")
            self.Gui.Text.PrintDisplay(Info)
            self.ClearEntry(self.GetEntryIndex.PrintCallendar.SeasonID)
        else:
            print("PrintSeasonCalendar path not found")

    def OpenSeasonLink(self):
        Name = self.GetEntry(self.GetEntryIndex.OpenSeasonLink.SeasonID)        
        if (os.path.exists(f"./Data/Seasons/{JsonUtil.TrueName(Name)}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/SeasonsLinks.json")
            if (Info.get(Name) != None):
                Link = Info[f"{Name}"]
                web.open(Link)
                self.ClearEntry(self.GetEntryIndex.OpenSeasonLink.SeasonID)
            else:
                print("OpenSeasonLink season not found")
        else:
            print("SetSeasonLink season path not found")
        
