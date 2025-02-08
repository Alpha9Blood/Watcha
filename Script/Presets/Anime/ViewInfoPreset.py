from Script.GUI_Index import AnimeI
from Script.ManageData.Anime.AnimeLists import GetAnimeList
class ViewInfo:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.AnimeIndex = AnimeI()

    def PrintInfo(self):
        self.Gui.Button.CreateBut('PrintInfo', self.Gui.AnimeExec.GetAnimeStatus , 230, 1 , 80)
        self.AnimeIndex.PrintInfo.ButtonIndex.GetInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.PrintInfo.ButtonIndex.GetInfo].config(width=12)
        self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.AnimeIndex.PrintInfo.ButtonIndex.GetInfo], "Print the data of the selected anime.")
        
        self.Gui.Text.CreateText("Name", 80, 1, 30)
        self.AnimeIndex.PrintInfo.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.PrintInfo.TextIndex.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 39)
        self.AnimeIndex.PrintInfo.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.PrintInfo.EntryIndex.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.PrintInfo.EntryIndex.Name])
        self.Gui.EntryList[self.AnimeIndex.PrintInfo.EntryIndex.Name].config(width=25)

    def PrintSeason(self):
        self.Gui.Button.CreateBut('PrintSeason', self.Gui.AnimeExec.PrintSeason , 170, 1 , 200)
        self.AnimeIndex.PrintSeason.ButtonIndex.PrintSeason = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.PrintSeason.ButtonIndex.PrintSeason].config(width=12)

        self.Gui.Text.CreateText("SeasonID", 80, 1, 150)
        self.AnimeIndex.PrintSeason.TextIndex.SeasonID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.PrintSeason.TextIndex.SeasonID], "File name containing season data.")

        self.Gui.Entry.CreateEntry(170, 1, 159)
        self.AnimeIndex.PrintSeason.EntryIndex.SeasonID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.PrintSeason.EntryIndex.SeasonID].AddList(GetAnimeList.GetListedSeasons)
        self.Gui.EntryList[self.AnimeIndex.PrintSeason.EntryIndex.SeasonID].config(width=12)

    def PrintStatusList(self):    
        self.Gui.Button.CreateBut('PrintStatusList', self.Gui.AnimeExec.PrintStatusList , 170, 1 , 320)
        self.AnimeIndex.PrintStatusList.ButtonIndex.PrintStatusList = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.PrintStatusList.ButtonIndex.PrintStatusList].config(width=14)
        self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.AnimeIndex.PrintStatusList.ButtonIndex.PrintStatusList], "If StatusID is empty, all status will be printed.")

        self.Gui.Text.CreateText("StatusID", 80, 1, 270)
        self.AnimeIndex.PrintStatusList.TextIndex.StatusID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.PrintStatusList.TextIndex.StatusID], "Can be Watching, Completed, Dropped, or PlanToWatch.")

        self.Gui.Entry.CreateEntry(170, 1, 279)
        self.AnimeIndex.PrintStatusList.EntryIndex.StatusID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.PrintStatusList.EntryIndex.StatusID].AddList(GetAnimeList.CurrentStatusTypeList)
        self.Gui.EntryList[self.AnimeIndex.PrintStatusList.EntryIndex.StatusID].config(width=11)

    def PrintAnimeList(self):
        self.Gui.Button.CreateBut('PrintAnimeList', self.Gui.AnimeExec.PrintAnimeList , 100, 1 , 500)
        self.AnimeIndex.PrintAnimeList.ButtonIndex.PrintList= self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.PrintAnimeList.ButtonIndex.PrintList].config(width=14)
        

    def PrintSerieList(self):
        self.Gui.Button.CreateBut('PrintSerieList', self.Gui.AnimeExec.PrintSerieList , 100, 1 , 600)
        self.AnimeIndex.PrintSerieList .ButtonIndex.PrintList= self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.PrintSerieList.ButtonIndex.PrintList].config(width=14)

    def PrintCalendar(self):
        self.Gui.Button.CreateBut('PrintCalendar', self.Gui.AnimeExec.PrintSeasonCalendar, 700, 1 , 680)
        self.AnimeIndex.PrintCallendar.ButtonIndex.PrintCallendar = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.PrintCallendar.ButtonIndex.PrintCallendar].config(width=13)
        self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.AnimeIndex.PrintCallendar.ButtonIndex.PrintCallendar], "Show season calendar")

        self.Gui.Text.CreateText("SeasonID", 600, 1, 630)
        self.AnimeIndex.PrintCallendar.TextIndex.SeasonID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.PrintCallendar.TextIndex.SeasonID], "File name containing season data")

        self.Gui.Entry.CreateEntry(700, 1, 639)
        self.AnimeIndex.PrintCallendar.EntryIndex.SeasonID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.PrintCallendar.EntryIndex.SeasonID].AddList(GetAnimeList.GetListedSeasons)
        self.Gui.EntryList[self.AnimeIndex.PrintCallendar.EntryIndex.SeasonID].config(width=12)
    
    def PrintSerie(self):
        self.Gui.Button.CreateBut('PrintSerie', self.Gui.AnimeExec.PrintSerie , 1270, 1 , 80)
        self.AnimeIndex.PrintSerie.ButtonIndex.PrintSerie = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Text.CreateText("SerieID", 1180, 1, 30)
        self.AnimeIndex.PrintSerie.TextIndex.SerieID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.PrintSerie.TextIndex.SerieID], "Can be simplified.")

        self.Gui.Entry.CreateEntry(1270, 1, 39)
        self.AnimeIndex.PrintSerie.EntryIndex.SerieID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.PrintSerie.EntryIndex.SerieID].AddList(GetAnimeList.SerieList)
        self.Gui.EntryList[self.AnimeIndex.PrintSerie.EntryIndex.SerieID].config(width=15)