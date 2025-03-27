import os
from Script.ManageData.Anime.AnimeObj import Anime
from Script.Utils import JsonUtil
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.ManageData.Anime.ManageSeasons import SeasonManager


class AnimeWatcha:

    def __init__(self):
        self.selected:Anime = Anime()
    
    def SelectAnime(self, Name:str) -> Anime:
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("SelectAnime anime not found")
        
        self.selected.UpdateData(Name)
        return self.selected
    
    def UpdateStatusList(self, Selected:Anime, UpdateStatus:bool = True):
        Name = Selected.Name
        if (os.path.exists(f"./Data/AnimeStatusList.json")):
            Status:dict[str, list[str]] = GetAnimeList.AnimeStatusList()
            
            if (UpdateStatus):
                Selected.UpdateStatus()

            SelectedList:list[str] = Status[Selected.CurrentStatus]
            if (Name in SelectedList):
                return

            SelectedList.append(Name)
            
            for status in Status:
                if (status != Selected.CurrentStatus and Name in Status[status]):
                    Status[status].remove(Name)            

            JsonUtil.UpdateJson(Status, f"./Data/AnimeStatusList.json")
        else:
            Status:dict[str, list[str]] = {"Watching": [], "Completed": [], "PlanToWatch": [], "Dropped": []}
            Status[Selected.CurrentStatus].append(Name)
            JsonUtil.CreateJson(Status, f"./Data/AnimeStatusList.json")
    
    #
    
    def GetStatus(self, Name:str) -> dict:
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("GetStatus Anime not found")
        
        Info:dict = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")["Anime"]
        PrintInfo:dict[str, str] = {
            "Name": Info["Name"],
            "EpisodeStatus": Info["EpisodeStatus"],
            "Status": Info["Status"],
            "Season": Info["Season"],
            "SerieName": Info["SerieName"],
            "Score": Info["Score"]
        }
        Score:float = float(PrintInfo["Score"])
        if (Score == 0):
            PrintInfo["Score"] = "N/A"
        return PrintInfo

    def GetCurrentStatus(self, currentStatus:str = "") -> list[str] | dict[str, list[str]]:
        """
        Retrieves the current status of anime from a JSON file.

        Args:
            -   currentStatus (str, optional): The specific status to filter the anime list by. 
            If empty, returns the entire status list. Defaults to "".

        Returns:
            -   list[str] | dict[str, list[str]]: A list of anime with the specified status if `currentStatus` is provided,
            otherwise a dictionary containing all status lists.

        Raises:
            Exception: If the JSON file containing the anime status list is not found.
        """
        if (not os.path.exists(f"./Data/AnimeStatusList.json")):
            raise Exception("GetCurrentStatus: AnimeStatusList path not found")
        
        if (currentStatus == ""):
            CurrentStatusList:dict[str, list[str]] = GetAnimeList.AnimeStatusList()
            return CurrentStatusList
        else:
            StatusList:list[str] = GetAnimeList.AnimeCurrentStatusList(currentStatus)
            return StatusList
            
            

    def UpdateEpisode(self, Name:str, Set:bool = False, Episode:str = ""):
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception(f"UpdateEpisode anime {Name = } not found")
        
        self.selected.UpdateData(Name, UpdateStatus = False)
        
        if (Set):
            try:
                EpisodeI:int = int(Episode)
                if (EpisodeI < 0):
                    EpisodeI = 0
                self.selected.Episode = EpisodeI
            except:
                raise ValueError("UpdateEpisode Episode must be a integer number")
        else:
            self.selected.Episode += 1

        self.UpdateStatusList(self.selected)
        self.selected.StoreData()

    def SetCurrentStatus(self, Name:str, Status:str):
        if (Status == ""):
            raise Exception("SetCurrentStatus status is empty")
        
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception(f"SetCurrentStatus anime {Name = } not found")
        
        self.selected.UpdateData(Name, UpdateStatus = False)
        self.selected.CurrentStatus = Status
        if (Status == "Completed"):
            self.selected.UpdateStatus()
        self.UpdateStatusList(self.selected, False)
        self.selected.StoreData(UpdateStatus = False)

    def SetScore(self, Name:str, Score:str):
        
        
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("SetScore not found")
        
        if (Score == ""):
            raise Exception("SetScore Score is empty")
        
        try:
            ScoreF:float = float(Score)
        except ValueError:
            raise ValueError(f"SetScore {Score = } must be a integer number")
        
        self.selected.UpdateData(Name)
        self.selected.Score = ScoreF
        self.selected.StoreData()
    
    def EditMaxEp(self, Name:str, MaxEp:str):
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception(f"EditMaxEp: {Name = } not found")
        
        if (MaxEp == ""):
            raise Exception("EditMaxEp MaxEp is empty")
        
        try:
            MaxEpI:int = int(MaxEp)
        except ValueError:
            raise ValueError(f"EditMaxEp: {MaxEp = } must be a integer number")
        
        self.selected.UpdateData(Name)
        self.selected.MaxEpisodes = MaxEpI
        self.selected.StoreData()
    
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
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception(f"RemoveAnime {Name = } path not found")
        
        self.selected.UpdateData(Name)

        # remove anime from its season
        if (os.path.exists(f"./Data/Seasons/{self.selected.Season}.json")):
            Season:list = JsonUtil.LoadJson(f"./Data/Seasons/{self.selected.Season}.json")
            ListedSeasonLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/SeasonsLinks.json")     

            if (len(Season) == 0):
                os.remove(f"./Data/Seasons/{self.selected.Season}.json")
                SelectedSeasonLinks:dict[str, str] = ListedSeasonLinks[str(SeasonManager.GetSeasonYear(self.selected.Season))]
                if (self.selected.Season in SelectedSeasonLinks):
                    SelectedSeasonLinks.pop(self.selected.Season)
                    if (len(SelectedSeasonLinks) == 0):
                        ListedSeasonLinks.pop(str(SeasonManager.GetSeasonYear(self.selected.Season)))
                    JsonUtil.UpdateJson(ListedSeasonLinks, "./Data/SeasonsLinks.json")
                else:
                    print("Season not found in season links")

            else:
                JsonUtil.UpdateJson(Season, f"./Data/Seasons/{self.selected.Season}.json")
        
        # remove season
        if (os.path.exists("./Data/ListedAnimeSeasons.json")):
            Season:list = JsonUtil.LoadJson(f"./Data/Seasons/{self.selected.Season}.json")
            ListedSeasons:list[str] = JsonUtil.LoadJson(f"./Data/ListedAnimeSeasons.json")
            
            if (self.selected.Season in ListedSeasons):
                if (len(GetAnimeList.GetSeason(self.selected.Season)) == 0):
                    ListedSeasons.remove(self.selected.Season)
            else:
                print("Anime not found in season list")

            if (Name in Season):
                Season.remove(Name)
            else:
                print("Anime not found in season list")
            
            if (len(ListedSeasons) == 0):
                os.remove(f"./Data/ListedAnimeSeasons.json")
            else:
                JsonUtil.UpdateJson(ListedSeasons, f"./Data/ListedAnimeSeasons.json")

        # remove anime from its serie       
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
        
        # remove anime from its status
        AnimeStatusListInfo:dict[str, list[str]] = GetAnimeList.AnimeStatusList()
        Info:list[str] = AnimeStatusListInfo[self.selected.CurrentStatus]
        if (Name in Info):
            Info.remove(Name)
            JsonUtil.UpdateJson(AnimeStatusListInfo, "./Data/AnimeStatusList.json")
        else:
            print("Anime not found in status list")

        # remove anime from listed animes 
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

        #remove images
        if (os.path.exists(f"./Data/AnimeImages/{JsonUtil.TrueName(Name)}.png")):
            os.remove(f"./Data/AnimeImages/{JsonUtil.TrueName(Name)}.png")

        # remove anime data
        os.remove(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
            

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

        if (currentstatus not in GetAnimeList.CurrentStatusTypeList()):
            raise Exception(f"Status not found: {currentstatus}")
        
        NewAnime:Anime = Anime(name, maxpisodes, currentstatus, Season)
        
        # set serie nameif it is not empty
        if (seriename != ""):
            
            if (os.path.exists(f"./Data/ListedSeries.json")):
                SerieList:list = JsonUtil.LoadJson("./Data/ListedSeries.json")
                if (seriename not in SerieList):   
                    SerieList.append(seriename)
                    JsonUtil.UpdateJson(SerieList, "./Data/ListedSeries.json")
                else:
                    print("SetNewAnime: Serie already in list")
            else:
                SerieNameList:list = [seriename]
                JsonUtil.CreateJson(SerieNameList, "./Data/ListedSeries.json")
            
            if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")):
                SerieDataList:list = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")
                if (name not in SerieDataList):
                    SerieDataList.append(name)
                    JsonUtil.UpdateJson(SerieDataList, f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")
                else:
                    print("SetNewAnime: name already in SerieDataList")
            else:
                AnimeNameList:list = [name]
                JsonUtil.CreateJson(AnimeNameList, f"./Data/SerieData/{JsonUtil.TrueName(seriename)}.json")

            NewAnime.SerieName = seriename
        
        # set season
        if (os.path.exists(f"./Data/Seasons/{NewAnime.Season}.json")):
            SeasonList:list = JsonUtil.LoadJson(f"./Data/Seasons/{NewAnime.Season}.json")
            if (NewAnime.Name not in SeasonList):
                SeasonList.append(NewAnime.Name)
                JsonUtil.UpdateJson(SeasonList, f"./Data/Seasons/{NewAnime.Season}.json")
            else:
                print("SetNewAnime: Season already in list")
        else:
            SeasonList:list = [NewAnime.Name]
            JsonUtil.CreateJson(SeasonList, f"./Data/Seasons/{NewAnime.Season}.json")

        # set season links and list

        SeasonManager.CheckSeasonlink(NewAnime)
        
        SelectedSeason:dict[str, list[str]] = JsonUtil.LoadJson(f"./Data/SeasonsLinks.json")[str(SeasonManager.GetSeasonYear(NewAnime.Season))]
        if (SelectedSeason[NewAnime.Season] == ""):
            SeasonManager.AddSeasonLinks(NewAnime.Season)

        # set statuslist
        if (os.path.exists("./Data/AnimeStatusList.json")):
            StatusList:dict[str, list[str]] = JsonUtil.LoadJson("./Data/AnimeStatusList.json")
            Status:list[str] = StatusList[NewAnime.CurrentStatus]
            if (NewAnime.Name not in Status):
                Status.append(NewAnime.Name)
                JsonUtil.UpdateJson(StatusList, "./Data/AnimeStatusList.json")
            else:
                print("SetNewAnime: Status already in list")
        else:
            StatusList:dict[str, list[str]] = {"Watching": [], "Completed": [], "PlanToWatch": [], "Dropped": []}
            StatusList[NewAnime.CurrentStatus].append(NewAnime.Name)
            JsonUtil.CreateJson(StatusList, "./Data/AnimeStatusList.json")
        
        # set listed animes
        if (os.path.exists(f"./Data/ListedAnimes.json")):
            AnimeList:list = JsonUtil.LoadJson(f"./Data/ListedAnimes.json")
            if (NewAnime.Name not in AnimeList):
                AnimeList.append(NewAnime.Name)
                JsonUtil.UpdateJson(AnimeList, f"./Data/ListedAnimes.json")
            else:
                print("SetNewAnime: Anime already in list")
        else:
            AnimeList:list = [NewAnime.Name]
            JsonUtil.CreateJson(AnimeList, f"./Data/ListedAnimes.json")

        # save data
        NewAnime.StoreData(True)

    def UpdateMyAnimeListLink(self, Name, Link):
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception("UpdateMyAnimeListLink path not found")
        else:
            self.selected.UpdateData(Name, False)
            self.selected.MyAnimeListLink = Link
            self.selected.StoreData()


    def PrintSeason(self, SeasonID:str) -> list:
        """
        Prints the season data for a given SeasonID.

        Args:
            SeasonID (str): The ID of the season to print.

        Returns:
            tuple: A tuple containing the SeasonID and a list of season data if the season file exists.
            str: A string indicating that the season file was not found if it does not exist.
        """
        if (not os.path.exists(f"./Data/Seasons/{SeasonID}.json")):
            raise Exception(f"PrintSeason: path not found / SeasonID: {SeasonID}")
        
        List:list[str] = JsonUtil.LoadJson(f"./Data/Seasons/{SeasonID}.json")
        return List

    def AddToSerie(self, Seriename, Animename):
        """
        Adds an anime to a specified series.

        Args:
            Seriename (str): The name of the series.
            Animename (str): The name of the anime.

        This function checks if the series and anime data files exist. If they do, the anime is added to the specified series.
        If the files do not exist, a "FileNotFoundError" is raised.
        """
        if (not os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(Seriename)}.json") and not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Animename)}.json")):
            raise Exception("AddToSerie: Anime or Serie path not found")
        
        List:list = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(Seriename)}.json")
        List.append(Animename)
        JsonUtil.UpdateJson(List, f"./Data/SerieData/{JsonUtil.TrueName(Seriename)}.json")

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

        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception(f"CreateCalendar: {JsonUtil.TrueName(Name)} path not found")

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
                raise Exception(f"CreateCalendar: {AnimeID.Season} is empty")

        
        Days:list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        SeasonDict:dict[str, list[str]] = JsonUtil.LoadJson(f"./Data/SeasonsCalendar/{AnimeID.Season}.json")[AnimeID.Season]
        Monday:list[str] = SeasonDict["Monday"]
        Tuesday:list[str] = SeasonDict["Tuesday"]
        Wednesday:list[str] = SeasonDict["Wednesday"]
        Thursday:list[str] = SeasonDict["Thursday"]
        Friday:list[str] =  SeasonDict["Friday"]
        Saturday:list[str] = SeasonDict["Saturday"]
        Sunday:list[str] = SeasonDict["Sunday"]
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
            print("CreateCalendar: Anime already in calendar")
    
    
    def AddWatchLink(self, Name:str, Link:str):
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            raise Exception(f"AddWatchLink: {JsonUtil.TrueName(Name)} path not found")
        
        Info:dict = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
        Info["Anime"]["WatchLink"] = Link
        JsonUtil.UpdateJson(Info, f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")
       
Watch = AnimeWatcha()