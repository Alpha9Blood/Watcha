import os , sys
sys.path.append(os.getcwd())
import tkinter as tk
import webbrowser as web
from GUI_Index import *
from Utils import JsonUtils

JsonUtil = JsonUtils()

class Anime:

    def __init__(self, name:str, maxepisodes:int, status:str, Season:str):
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
        self.DataBase:dict = self.Data()        
    
    def CurrentEpisodeStatus(self):
        if (self.Episode > 0):
            return f"{self.Episode}/{self.MaxEpisodes}"
        else:
            return f"{self.Episode}/Undefined"
        
    def CurrentStatusList(self):
        return ["PlanToWatch", "Watching", "Completed", "Dropped"]
    
    def UpdateStatus(self):
        """
        Updates the status of the anime based on the current episode number.

        The status is updated as follows:
            - If the episode number is greater than 0 and not dropped, the status is set to "Watching" if the episode number is less than the maximum episodes, or "Completed" if the episode number is equal to the maximum episodes.
            - If the episode number is 0, the status is set to "PlanToWatch".
            - If the episode number is less than 0, the status is set to "Error".

        """
        if (self.Episode > 0 and not self.CurrentStatus == "Dropped"):
            if (self.Episode >= self.MaxEpisodes):
                self.Episode = self.MaxEpisodes
                self.CurrentStatus = "Completed"
            elif (self.Episode < self.MaxEpisodes):
                self.CurrentStatus = "Watching"
        elif (self.Episode == 0):
            self.CurrentStatus = "PlanToWatch"
        elif (self.Episode < 0):
            self.CurrentStatus = "Error"

    
    def ConvertData(self):
        """
        Converts data from the DataBase dictionary to the Anime object's properties.

        """
        Anime = self.DataBase.get("Anime", [])
        self.Name = Anime.get("Name", "")
        self.EpisodeStatus = Anime.get("EpisodesStatus", "")
        self.CurrentStatus = Anime.get("Status", "")
        self.Season = Anime.get("Season", "")
        self.MaxEpisodes = Anime.get("MaxEpisodes", 0)
        self.Episode = Anime.get("Episode", 0)
        self.SerieName = Anime.get("SerieName", "")
        self.MyAnimeListLink = Anime.get("MyAnimeListLink", "")
        self.Score = Anime.get("Score", 0.0)
    
    
    @property
    def AnimeData(self):
        return {
            "Anime": {
                "Name": self.Name,
                "EpisodesStatus": self.CurrentEpisodeStatus(),
                "Status": self.CurrentStatus,
                "Season": self.Season,
                "MaxEpisodes": self.MaxEpisodes,
                "Episode": self.Episode,
                "SerieName": self.SerieName,
                "MyAnimeListLink": self.MyAnimeListLink,
                "Score": self.Score
            }
        }
    def Data(self):
        return self.AnimeData
    

class Watcha:

    def __init__(self):
        self.selected:Anime = Anime("", 0, "", "")
    
    def NameList(self):
        Names:list = JsonUtil.LoadJson("./Data/ListedAnimes.json")
        return Names
    
    def SerieListData(self):
        Data:dict = JsonUtil.LoadJson("./Data/StatusList.json")
        return Data
    
    def TrueName(self, Name:str):
        """
        Returns a string with all occurrences of ':' replaced with '_'.
        
        Parameters:
            Name (str): The string to replace ':' with '_'.
        
        Returns:
            str: The modified string.
        """
        if  (Name.count(":") > 0):
            return Name.replace(":", "_")
        else:
            return Name
        
    
    def TrueSerieName(self, SerieName:str):
        if (SerieName.count(":") > 0):
            return SerieName.replace(":", "_")
        else:
            return SerieName


    def PrintData(self):
        return {
            "Anime": {
                "Name": self.selected.Name,
                "Episodes": self.selected.CurrentEpisodeStatus(),
                "Status": self.selected.CurrentStatus,
                "Season": self.selected.Season,
                "SerieName": self.selected.SerieName,
                "Score": self.selected.Score
            }
        }
    
    


    def GetStatusList(self, Type:str):
        """
        Retrieves a specific status list from the SerieListData dictionary.

        Args:
            Type (str): The type of status list to retrieve (e.g. "Completed", "Watching", etc.).

        Returns:
            list: The status list of the specified type, or None if it does not exist.
        """
        return self.SerieListData().get(f"{Type}List")
    
    def UpdateBaseData(self, Name):
        """
        Updates the base data of an anime in the database.

        Args:
            Name (str): The name of the anime.

        Notes:
            This function checks if the anime's data file exists. If it does, it updates the base data by loading the data from the file and converting it. If the file does not exist, it prints an error message.
        
        """
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            self.selected.DataBase = JsonUtil.LoadJson(f"./Data/AnimeData/{self.TrueName(Name)}.json")
            self.selected.ConvertData()
        else:
            print("UpdateData not found")

        

    def UpdateStatusList(self):
        """
        Updates the status list based on the current status of each anime in the name list.
        
        This function iterates over each anime in the name list and updates the corresponding status list based on the current status of the anime. The status lists include CompletedList, DroppedList, PlanToWatchList, and WatchingList.
        
        For each anime, the function calls the UpdateBaseData method to update the base data. It then retrieves the current status and name of the anime.
        
        If the current status is "Watching" and the anime is not already in the WatchingList, it adds the anime to the WatchingList.
        
        If the current status is "Completed" and the anime is not already in the CompletedList, it adds the anime to the CompletedList. If the anime is already in the WatchingList, it removes it from the WatchingList.
        
        If the current status is "PlanToWatch" and the anime is not already in the PlanToWatchList, it adds the anime to the PlanToWatchList.
        
        If the current status is "Dropped" and the anime is not already in the DroppedList, it adds the anime to the DroppedList. If the anime is already in the WatchingList, it removes it from the WatchingList.
        
        Finally, the function creates a dictionary called Lists, which contains the four status lists. It then serializes the Lists dictionary to a JSON file named "StatusList.json" in the "./Data" directory.
        
        """
        CompletedList:list = []
        DroppedList:list = []
        PlanToWatchList:list = []
        WatchingList:list = []

        for anime in self.NameList(): 
            self.UpdateBaseData(anime)
            SelectedStatus:str = self.selected.CurrentStatus
            SelectedName:str = self.selected.Name                    
            if (SelectedStatus == "Watching" and WatchingList.count(SelectedName) == 0):
                WatchingList.append(SelectedName)
            elif (SelectedStatus == "Completed" and CompletedList.count(SelectedName) == 0):
                CompletedList.append(SelectedName)
                if (WatchingList.count(SelectedName) > 0):
                    WatchingList.remove(SelectedName)
            elif (SelectedStatus == "PlanToWatch" and PlanToWatchList.count(SelectedName) == 0):
                PlanToWatchList.append(SelectedName)
            elif (SelectedStatus == "Dropped" and DroppedList.count(SelectedName) == 0):
                DroppedList.append(SelectedName)
                if (WatchingList.count(SelectedName) > 0):
                    WatchingList.remove(SelectedName)

        Lists:dict = {
            "Completed": CompletedList,
            "Dropped": DroppedList,
            "PlanToWatch": PlanToWatchList,
            "Watching": WatchingList
        }
        if (os.path.exists("./Data/StatusList.json")):
            JsonUtil.UpdateJson(Lists, "./Data/StatusList.json")
        else:
            JsonUtil.CreateJson(Lists, "./Data/StatusList.json")

    def UpdateData(self, Name):     
        """
        Updates the data for a given anime name.

        Args:
            Name (str): The name of the anime.

        Notes:
            This function calls UpdateStatusList and UpdateBaseData to update the data.
        """
        self.UpdateStatusList()
        self.UpdateBaseData(Name)
        
    
    def GetAnime(self, Name):
        """
        Retrieves an anime object based on the provided name.

        Args:
            Name (str): The name of the anime.

        Returns:
            The anime object if found, otherwise the default selected object.
        """
        self.UpdateBaseData(Name)
        return self.selected 

    
    def GetStatus(self, Name):
        """
        Retrieves the status of an anime from the data file.

        Args:
            Name (str): The name of the anime.

        Returns:
            The anime's data if found, otherwise prints an error message.

        Notes:
            This function checks if the anime's data file exists, updates the data, and prints the data if found.
        """
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            self.UpdateData(Name)
            return self.PrintData()         
        else:
            print("Anime data not found")

    def UpdateEpisode(self, Name:str, Set:bool = False, SetEp:int = 0):
        """
        Updates the episode of an anime in the data file.

        Args:
            Name (str): The name of the anime.
            Set (bool, optional): If True, sets the episode to the provided SetEp value. Defaults to False.
            SetEp (int, optional): The episode number to set. Defaults to 0.

        Notes:
            - The function first checks if the anime data file exists.
            - If the file exists, it updates the episode number of the anime in the selected object.
            - If Set is True, it sets the episode number to the provided SetEp value.
            - If Set is False, it increments the episode number by 1.
            - It then updates the status of the anime and saves the updated data to the anime data file.
            - If the anime data file is not found, it prints "UpdateEpisode not found".
        """
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            self.UpdateData(Name)
            if (Set):
                self.selected.Episode = SetEp
            else:
                self.selected.Episode += 1
            self.selected.UpdateStatus()
            JsonUtil.UpdateJson(self.selected.Data(), f"./Data/AnimeData/{self.TrueName(Name)}.json")            
        else:
            print("UpdateEpisode not found")

    def SetCurrentStatus(self, Name:str, Status:str):
        """
        Sets the current status of an anime in the database.

        Args:
            Name (str): The name of the anime.
            Status (str): The new status of the anime. It can be one of "Watching", "Completed", "Dropped", or "PlanToWatch".

        This function checks if the anime data file exists for the given name. If it does, it updates the selected object with the new status.
        If the new status is valid, it sets the current status of the anime to the new status. Otherwise, it sets the current status to "Error".
        The updated anime data is then saved to the anime data file.

        If the anime data file is not found, it prints "SetCurrentStatus not found".
        """
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            self.UpdateData(Name)
            if (self.selected.CurrentStatusList().count(Status) > 0):
                self.selected.CurrentStatus = f"{Status}"
            else:
                self.selected.CurrentStatus = "Error"
            JsonUtil.UpdateJson(self.selected.Data(), f"./Data/AnimeData/{self.TrueName(Name)}.json")    
        else:
            print("SetCurrentStatus not found")

    def SetScore(self, Name:str, Score:float):
        """
        Sets the Score (rating) of an anime in the database.

        Args:
            Name (str): The name of the anime.
            Score (float): The new Score (rating) of the anime.

        Updates the Score of the anime and saves the updated data to the anime data file.
        If the anime data file is not found, it prints "SetScore not found".
        """
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            self.UpdateData(Name)
            self.selected.Score = Score
            JsonUtil.UpdateJson(self.selected.Data(), f"./Data/AnimeData/{self.TrueName(Name)}.json")
        else:
            print("SetScore not found")
    
    def Remove(self, Name:str):
        """
        Remove an anime from the database.

        Args:
            Name (str): The name of the anime to be removed.

        Removes the anime from the database by updating the corresponding season list, series data, status list, and anime data files.

        Raises:
            FileNotFoundError: If the season list, series data, status list, or anime data file is not found.

        """
        self.UpdateData(Name)
        ListedSeason:list = JsonUtil.LoadJson(f"./Data/Seasons/{self.selected.Season}.json")
        ListedSeason.remove(Name)
        if (len(ListedSeason) > 0):
            JsonUtil.UpdateJson(ListedSeason, f"./Data/Seasons/{self.selected.Season}.json")
        else:
            os.remove(f"./Data/Seasons/{self.selected.Season}.json")

        if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")):
            List:list = JsonUtil.LoadJson(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")
            List.remove(Name)            
            if (List.count(Name) == 0):
                os.remove(f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")
            else:
                JsonUtil.UpdateJson(List, f"./Data/SerieData/{self.TrueSerieName(self.selected.SerieName)}.json")
        else:
            print("RemoveSerieData not found")

        StatusList:dict = JsonUtil.LoadJson("./Data/StatusList.json")
        StatusList[f"{self.selected.CurrentStatus}"].remove(Name)
        JsonUtil.UpdateJson(StatusList, "./Data/StatusList.json")

        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            os.remove(f"./Data/AnimeData/{self.TrueName(Name)}.json")
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
            FileNotFoundError: If the file "./Data/ListedSeries.json" or "./Data/SerieData/{self.TrueSerieName(seriename)}.json" does not exist.

        Side Effects:
            - Appends the anime name to the "./Data/ListedSeries.json" file if the series name is not empty and the series name is not already in the file.
            - Appends the anime name to the "./Data/SerieData/{self.TrueSerieName(seriename)}.json" file if the anime name is not already in the file.
            - Sets the "SerieName" attribute of the "NewAnime" object to the series name if the series name is not empty.
            - Appends the anime name to the "./Data/Seasons/{NewAnime.Season}.json" file if the anime name is not already in the file.
            - Creates a new empty list and appends the anime name to it if the file "./Data/Seasons/{NewAnime.Season}.json" does not exist.
            - Appends the anime name to the "./Data/ListedAnimes.json" file if the anime name is not already in the file.
            - Creates a new empty list and appends the anime name to it if the file "./Data/ListedAnimes.json" does not exist.
            - Saves the "NewAnime" object data to the "./Data/AnimeData/{self.TrueName(name)}.json" file.
            - Calls the "UpdateData" method with the anime name as an argument.
        """
        NewAnime = Anime(name, maxpisodes, currentstatus, Season)

        if (not seriename == ""):
            
            if (os.path.exists(f"./Data/ListedSeries.json")):
                SerieList:list = JsonUtil.LoadJson("./Data/ListedSeries.json")
                if (SerieList.count(seriename) == 0):   
                    SerieList.append(seriename)
                    JsonUtil.UpdateJson(SerieList, "./Data/ListedSeries.json")
            else:
                SerieNameList:list = [seriename]
                JsonUtil.CreateJson(SerieNameList, "./Data/ListedSeries.json")
            
            if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json")):
                SerieDataList:list = JsonUtil.LoadJson(f"./Data/SerieData/{self.TrueSerieName(seriename)}.json")
                if (SerieDataList.count(name) == 0):
                    SerieDataList.append(name)
                    JsonUtil.UpdateJson(SerieDataList, f"./Data/SerieData/{self.TrueSerieName(seriename)}.json")
            else:
                AnimeNameList:list = [name]
                JsonUtil.CreateJson(AnimeNameList, f"./Data/SerieData/{self.TrueSerieName(seriename)}.json")

            NewAnime.SerieName = seriename
        
        if (os.path.exists(f"./Data/Seasons/{NewAnime.Season}.json")):
            SeasonList:list = JsonUtil.LoadJson(f"./Data/Seasons/{NewAnime.Season}.json")
            if (SeasonList.count(NewAnime.Name) == 0):
                SeasonList.append(NewAnime.Name)
                JsonUtil.UpdateJson(SeasonList, f"./Data/Seasons/{NewAnime.Season}.json")
        else:
            SeasonList:list = [NewAnime.Name]
            JsonUtil.CreateJson(SeasonList, f"./Data/Seasons/{NewAnime.Season}.json")
        
        if (os.path.exists(f"./Data/ListedAnimes.json")):
            AnimeList:list = JsonUtil.LoadJson(f"./Data/ListedAnimes.json")
            if (AnimeList.count(name) == 0):
                AnimeList.append(name)
                JsonUtil.UpdateJson(AnimeList, f"./Data/ListedAnimes.json")
        else:
            AnimeList:list = [name]
            JsonUtil.CreateJson(AnimeList, f"./Data/ListedAnimes.json")
        JsonUtil.CreateJson(NewAnime.Data(), f"./Data/AnimeData/{self.TrueName(name)}.json")
        self.UpdateData(name)

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
        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            self.UpdateData(Name)
            self.selected.MyAnimeListLink = Link
            JsonUtil.UpdateJson(self.selected.Data(), f"./Data/AnimeData/{self.TrueName(Name)}.json")
        else:
            print("UpdateMyAnimeListLink not found")


    def PrintSeason(self, SeasonID:str):
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
            return (f"{SeasonID}", List)
        else:
            print("PrintSeason path not found")
            return "PrintSeason path not found"
            

    def AddToSerie(self, Seriename, Animename):
        """
        Adds an anime to a specified series.

        Args:
            Seriename (str): The name of the series.
            Animename (str): The name of the anime.

        This function checks if the series and anime data files exist. If they do, the anime is added to the specified series.
        If the files do not exist, a "FileNotFoundError" is raised.
        """
        if (os.path.exists(f"./Data/SerieData/{self.TrueSerieName(Seriename)}.json") and os.path.exists(f"./Data/AnimeData/{self.TrueName(Animename)}.json")):
            List:list = JsonUtil.LoadJson(f"./Data/SerieData/{self.TrueSerieName(Seriename)}.json")
            List.append(Animename)
            JsonUtil.UpdateJson(List, f"./Data/SerieData/{self.TrueSerieName(Seriename)}.json")
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
        AnimeID:Anime = self.GetAnime(Name)

        if (not os.path.exists(f"./Data/SeasonsCalendar/{AnimeID.Season}.json")):
            Calendar:dict = {
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
            if (AnimeID.Season != ""):
                JsonUtil.CreateJson(Calendar, f"./Data/SeasonsCalendar/{AnimeID.Season}.json")

        if (os.path.exists(f"./Data/AnimeData/{self.TrueName(Name)}.json")):
            Days:list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
            SeasonDict:dict = JsonUtil.LoadJson(f"./Data/SeasonsCalendar/{AnimeID.Season}.json")
            Monday:list = SeasonDict.get("Monday", [])
            Tuesday:list = SeasonDict.get("Tuesday", [])
            Wednesday:list = SeasonDict.get("Wednesday", [])
            Thursday:list = SeasonDict.get("Thursday", [])
            Friday:list =  SeasonDict.get("Friday", [])
            Saturday:list = SeasonDict.get("Saturday", [])
            Sunday:list = SeasonDict.get("Sunday", [])
            DaysList:list = [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]

            if (DaysList[Days.index(Day)].count(Name) == 0):

                DaysList[Days.index(Day)].append(self.GetAnime(Name).Name)

                Calendar:dict = {
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
        




Watch = Watcha()

class ExecuteFunctions:
    
    
    def __init__(self, Janela):
        self.Gui = Janela
        self.SetEntryIndex = AnimeSet.EntryIndex
        self.GetEntryIndex = AnimeGet.EntryIndex
        
    
    #Tools
    def ClearEntry(self, Index:int = -1, IndexList:list = []):
        
        """
        Clears the entry fields in the GUI.

        Args:
            Index (int): The index of the entry field to clear. Defaults to -1.
            IndexList (list): A list of indices of entry fields to clear. Defaults to an empty list.

        """
        if (Index > -1):
            self.EntryList()[Index].delete(0, 'end')
        if (IndexList != []):
            for i in IndexList:
                self.EntryList()[i].delete(0, 'end')

    def GetEntry(self, index:int):
        return self.EntryList()[index].get()
         
    def ButList(self):
        But:list[tk.Button] = self.Gui.ButList
        return But

    def TextList(self):
        Text:list[tk.Label] = self.Gui.TextList
        return Text

    def EntryList(self):
        Entry:list[tk.Entry] = self.Gui.EntryList
        return Entry
    
    def NameList(self):
        if (os.path.exists("./Data/ListedAnimes.json")):
            Name:list = JsonUtil.LoadJson("./Data/ListedAnimes.json")
            return Name
        else:
            Name:list = []
            JsonUtil.CreateJson(Name, "./Data/ListedAnimes.json")
            return Name
        
    def SerieList(self):
        if (os.path.exists("./Data/ListedSeries.json")):
            Serie:list = JsonUtil.LoadJson("./Data/ListedSeries.json")
            return Serie
        else:
            Serie:list = []
            JsonUtil.CreateJson(Serie, "./Data/ListedSeries.json")
            return Serie


    #ExecFuncs


    #Set

    
    def RemoveLeastAdded(self):
        
        Namelist = self.NameList()
        SerieList = self.SerieList()
        Name:str = Namelist[::-1][0]
        
        Namelist.remove(Name)        
        SerieList.remove(Watch.GetAnime(Name).SerieName)
        Watch.Remove(Name)
        JsonUtil.UpdateJson(Namelist, "./Data/ListedAnimes.json")
        JsonUtil.UpdateJson(SerieList, "./Data/ListedSeries.json") 

    def Add(self):
        Name:str = self.GetEntry(self.SetEntryIndex.AddAnime.Name)
        if (len(self.GetEntry(self.SetEntryIndex.AddAnime.MaxEp)) > 0):
            MaxEpisodes:int = int(self.GetEntry(1))
        else:
            MaxEpisodes:int = 0
        Status:str = self.GetEntry(self.SetEntryIndex.AddAnime.Status)
        Season:str = self.GetEntry(self.SetEntryIndex.AddAnime.Season)
        Serie:str = self.GetEntry(self.SetEntryIndex.AddAnime.Serie)

        def AddIsComplete():
            if (len(Name) > 0 and len(Status) > 0 and len(Season) > 0):
                return True
            else:
                return False
        if (AddIsComplete()):
            Watch.SetNewAnime(Name, MaxEpisodes, Status, Season, Serie)
            
            for i in range(5):
                self.ClearEntry(i)
        else:
            print("AddInfo is not completed")
    
    def RemoveAnime(self):
        Name:str = self.GetEntry(self.SetEntryIndex.DeleteAnime.Name)
        Namelist = self.NameList()
        SerieList = self.SerieList()
        if (Namelist.count(Name) > 0):
            Namelist.remove(Name)        
            SerieList.remove(Watch.GetAnime(Name).SerieName)
            Watch.Remove(Name)
            JsonUtil.UpdateJson(Namelist, "./Data/ListedAnimes.json")
            JsonUtil.UpdateJson(SerieList, "./Data/ListedSeries.json")
            self.ClearEntry(self.SetEntryIndex.DeleteAnime.Name)
        else:
            print("AnimeRemove not found")

    def AddEppisode(self):
        Name:str = self.GetEntry(self.SetEntryIndex.AddEpisode.Name)
        Finded:bool = False
        NameList = self.NameList()
        if (Name != ""):
            for i in range(NameList.__len__()):
                Selected:str = NameList[i]
                if (not Finded and Selected.count(Name) > 0):
                    if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                        Watch.UpdateEpisode(Selected)
                        Finded = True
                        self.ClearEntry(self.SetEntryIndex.AddEpisode.Name)
                    else:
                        print("AddEpisode path not found") 

    def SetEpisode(self):
        Name:str = self.GetEntry(self.SetEntryIndex.AddEpisode.Name)
        SetEP = self.GetEntry(self.SetEntryIndex.AddEpisode.Ep)

        Finded:bool = False
        NameList = self.NameList()
        if (len(SetEP) > 0 and Name != ""):
            for i in range(NameList.__len__()):
                Selected:str = NameList[i]
                if (not Finded and Selected.count(Name) > 0):
                    if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                        Watch.UpdateEpisode(Selected, True, int(SetEP))
                        Finded = True
                        self.ClearEntry(self.SetEntryIndex.AddEpisode.Name)
                        self.ClearEntry(self.SetEntryIndex.AddEpisode.Ep)
                    else:
                        print("SetEpisode path not found")
    
    def UpdateScore(self):
        Name = self.GetEntry(self.SetEntryIndex.UpdateScore.Name)
        Score = float(self.GetEntry(self.SetEntryIndex.UpdateScore.Score))
        if (self.NameList().count(Name) > 0):
            Watch.SetScore(Name, Score)
            self.ClearEntry(self.SetEntryIndex.UpdateScore.Name)
            self.ClearEntry(self.SetEntryIndex.UpdateScore.Score)
        else:
            print("UpdateScore not found")
              

    def OverrideCurrentStatus(self):
        Name:str = self.GetEntry(self.SetEntryIndex.SetCurrentStatus.Name)
        Status:str = self.GetEntry(self.SetEntryIndex.SetCurrentStatus.Status)
        if (self.NameList().count(Name) > 0):
            Watch.SetCurrentStatus(Name, Status)
            self.ClearEntry(self.SetEntryIndex.SetCurrentStatus.Name)
            self.ClearEntry(self.SetEntryIndex.SetCurrentStatus.Status)
        else:
            print("OverrideCurrentStatus not found")

    def AddMyAnimeListLink(self):
        Name = self.GetEntry(self.SetEntryIndex.MyAnimeListLink.Name)
        Link = self.GetEntry(self.SetEntryIndex.MyAnimeListLink.Link)
        if (self.NameList().count(Name) > 0):
            Watch.UpdateMyAnimeListLink(Name, Link)
            self.ClearEntry(self.SetEntryIndex.MyAnimeListLink.Name)
            self.ClearEntry(self.SetEntryIndex.MyAnimeListLink.Link)
        else:
            print("AddMyAnimeListLink not found")


    def AddToCalendar(self):
        Name = self.GetEntry(self.SetEntryIndex.AddToCallendar.Name)
        Day = self.GetEntry(self.SetEntryIndex.AddToCallendar.Day)
        if (self.NameList().count(Name) > 0):
            Watch.CreateCalendar(Name, Day)
            self.ClearEntry(self.SetEntryIndex.AddToCallendar.Name)
            """ self.ClearEntry(self.SetEntryIndex.AddToCallendar.Day) """
        else:
            print("AddToCalendar not found")
        


    #Get

    def OpenMyAnimeList(self):
        web.open("https://myanimelist.net")

    def PrintAnimeList(self):
        self.Gui.Texto.PrintDisplay(self.NameList())        

    def PrintSerieList(self):
        self.Gui.Texto.PrintDisplay(self.SerieList())

    
    def GetAnimeStatus(self):
        Name:str = self.GetEntry(self.GetEntryIndex.GetStatus.Name)
        Finded:bool = False
        NameList:list = self.NameList()
        if (Name != ""):
            for i in range(NameList.__len__()):
                Selected:str = NameList[i]
                if (not Finded and Selected.count(Name) > 0):
                    if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Selected)}.json")):
                        self.Gui.Texto.PrintDisplay(Watch.GetStatus(Selected))
                        Finded = True
                        self.ClearEntry(self.GetEntryIndex.GetStatus.Name)
                    else:
                        print("GetAnimeStatus path not found")

    def PrintSeason(self):
        SeasonID:str = self.GetEntry(self.GetEntryIndex.PrintSeason.SeasonID)
        self.Gui.Texto.PrintDisplay(Watch.PrintSeason(SeasonID))
        self.ClearEntry(self.GetEntryIndex.PrintSeason.SeasonID)
    
    def PrintStatusList(self):
        Info:str = self.GetEntry(self.GetEntryIndex.PrintStatusList.StatusID)
        if (os.path.exists("./Data/StatusList.json")):
            Status:dict = JsonUtil.LoadJson("./Data/StatusList.json")
        else:
            print("PrintStatusList path not found")
        if (Info != "" and os.path.exists("./Data/StatusList.json")):
            Selected:list = Status.get(f"{Info}", [])
            self.Gui.Texto.PrintDisplay(Selected)
            self.ClearEntry(self.GetEntryIndex.PrintStatusList.StatusID)
        else:
            StatusList:list[str] = ["Watching", "Completed", "PlanToWatch", "Dropped"]
            if (StatusList.count(Info) > 0):
                self.Gui.Texto.PrintDisplay(Info)
                self.ClearEntry(self.GetEntryIndex.PrintStatusList.StatusID)
            else:
                print("PrintStatusList not found")

    def OpenLink(self):
        Name:str = self.GetEntry(self.GetEntryIndex.OpenLink.Name)
        if (os.path.exists(f"./Data/AnimeData/{Watch.TrueName(Name)}.json")):
            link = Watch.GetAnime(Name).MyAnimeListLink
            web.open(link)
            self.ClearEntry(self.GetEntryIndex.OpenLink.Name)
        else:
            print("OpenLink path not found")

    def PrintSerie(self):
        Name:str = self.GetEntry(self.GetEntryIndex.PrintSerie.Name)
        if (os.path.exists(f"./Data/SerieData/{Name}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/SerieData/{Name}.json")
            self.Gui.Texto.PrintDisplay(Info)
            self.ClearEntry(self.GetEntryIndex.PrintSerie.Name)
        else:
            print("PrintSerie path not found")
    
    def PrintSeasonCalendar(self):
        SeasonID:str = self.GetEntry(self.GetEntryIndex.PrintCallendar.SeasonID)
        if (os.path.exists(f"./Data/SeasonsCalendar/{SeasonID}.json")):
            Info:dict = JsonUtil.LoadJson(f"./Data/SeasonsCalendar/{SeasonID}.json")
            self.Gui.Texto.PrintDisplay(Info)
            self.ClearEntry(self.GetEntryIndex.PrintCallendar.SeasonID)
        else:
            print("PrintSeasonCalendar path not found")
        
