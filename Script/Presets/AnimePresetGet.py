from Script.GUI_Index import AnimeGet
from Script.Data.AnimeLists import GetAnimeList
class AnimePresetGet:
    def __init__(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI
        self.ButtonIndex = AnimeGet.ButtonIndex()
        self.EntryIndex = AnimeGet.EntryIndex()
        self.TextIndex = AnimeGet.TextIndex()
    
    def Filter(self):
        self.Gui.Text.CreateText("Filter", 900, 1, 20)
        self.TextIndex.Filter.Selected = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(980, 1, 25)
        self.EntryIndex.FilterOptions.Selected = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.FilterOptions.Selected].AddList(self.Gui.AnimeDataLists.GetList, True)
        self.Gui.EntryList[self.EntryIndex.FilterOptions.Selected].config(state='normal')
        self.Gui.EntryList[self.EntryIndex.FilterOptions.Selected].insert(0, self.Gui.AnimeDataLists.SelectedFilter)
        self.Gui.EntryList[self.EntryIndex.FilterOptions.Selected].config(state='readonly')
        self.Gui.EntryList[self.EntryIndex.FilterOptions.Selected].SetActiveSwitch(self.Gui.Entry.UpdateFilterEntrys)
        self.Gui.EntryList[self.EntryIndex.FilterOptions.Selected].config(width=12)

    def GetStatus(self):
        self.Gui.Button.CreateBut('GetStatus', self.Gui.WatchaExec.GetAnimeStatus , 230, 1 , 80)     
        self.ButtonIndex.GetStatus = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.GetStatus].config(width=12)
        self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.ButtonIndex.GetStatus], "Print the data of the selected anime.")
        
        self.Gui.Text.CreateText("Name", 80, 1, 30)
        self.TextIndex.GetStatus.StatusID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.GetStatus.StatusID], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 39)
        self.EntryIndex.GetStatus.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.GetStatus.Name].AddList(self.Gui.AnimeDataLists.GetSelectedList)
        self.Gui.Entry.EntryType.AnimeList.append(self.Gui.EntryList[self.EntryIndex.GetStatus.Name])
        self.Gui.EntryList[self.EntryIndex.GetStatus.Name].config(width=25)


    def PrintSeason(self):
        self.Gui.Button.CreateBut('PrintSeason', self.Gui.WatchaExec.PrintSeason , 170, 1 , 200)
        self.ButtonIndex.PrintSeason = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintSeason].config(width=12)

        self.Gui.Text.CreateText("SeasonID", 80, 1, 150)
        self.TextIndex.PrintSeason.SeasonID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintSeason.SeasonID], "File name containing season data.")

        self.Gui.Entry.CreateEntry(170, 1, 159)
        self.EntryIndex.PrintSeason.SeasonID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.PrintSeason.SeasonID].AddList(GetAnimeList.GetListedSeasons)
        self.Gui.EntryList[self.EntryIndex.PrintSeason.SeasonID].config(width=12)


    def PrintStatusList(self):    
        self.Gui.Button.CreateBut('PrintStatusList', self.Gui.WatchaExec.PrintStatusList , 170, 1 , 320)
        self.ButtonIndex.PrintStatusList = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintStatusList].config(width=14)
        self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.ButtonIndex.PrintStatusList], "If StatusID is empty, all status will be printed.")

        self.Gui.Text.CreateText("StatusID", 80, 1, 270)
        self.TextIndex.PrintStatusList.StatusID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintStatusList.StatusID], "Can be Watching, Completed, Dropped, or PlanToWatch.")

        self.Gui.Entry.CreateEntry(170, 1, 279)
        self.EntryIndex.PrintStatusList.StatusID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.PrintStatusList.StatusID].AddList(GetAnimeList.CurrentStatusTypeList)
        self.Gui.EntryList[self.EntryIndex.PrintStatusList.StatusID].config(width=11)


    def OpenLink(self):
        self.Gui.Button.CreateBut('OpenLink', self.Gui.WatchaExec.OpenLink , 170, 1 , 560)
        self.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Text.CreateText("Name", 80, 1, 510)
        self.TextIndex.OpenLink.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.OpenLink.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 519)
        self.EntryIndex.OpenLink.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.OpenLink.Name].AddList(self.Gui.AnimeDataLists.GetSelectedList)
        self.Gui.Entry.EntryType.AnimeList.append(self.Gui.EntryList[self.EntryIndex.OpenLink.Name])
        self.Gui.EntryList[self.EntryIndex.OpenLink.Name].config(width=25)


    def PrintSerie(self):
        self.Gui.Button.CreateBut('PrintSerie', self.Gui.WatchaExec.PrintSerie , 170, 1 , 440)
        self.ButtonIndex.PrintSerie = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Text.CreateText("SerieID", 80, 1, 390)
        self.TextIndex.PrintSerie.SerieID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintSerie.SerieID], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 399)
        self.EntryIndex.PrintSerie.SerieID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.PrintSerie.SerieID].AddList(GetAnimeList.SerieList)
        self.Gui.EntryList[self.EntryIndex.PrintSerie.SerieID].config(width=15)


    def PrintAnimeList(self):
        self.Gui.Button.CreateBut('PrintAnimeList', self.Gui.WatchaExec.PrintAnimeList , 1200, 1 , 200)
        self.ButtonIndex.PrintAnimeList = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintAnimeList].config(width=14)
        

    def PrintSerieList(self):
        self.Gui.Button.CreateBut('PrintSerieList', self.Gui.WatchaExec.PrintSerieList , 1200, 1 , 350)
        self.ButtonIndex.PrintSerieList = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintSerieList].config(width=14)


    def OpenMyAnimeList(self):
        self.Gui.Button.CreateBut('OpenMyAnimeList', self.Gui.WatchaExec.OpenMyAnimeList , 700, 1 , 20)
        self.ButtonIndex.OpenMyAnimeList = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.OpenMyAnimeList].config(width=16)


    def PrintCalendar(self):
        self.Gui.Button.CreateBut('PrintCalendar', self.Gui.WatchaExec.PrintSeasonCalendar, 700, 1 , 680)
        self.ButtonIndex.PrintCallendar = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintCallendar].config(width=13)
        self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.ButtonIndex.PrintCallendar], "Show season calendar")

        self.Gui.Text.CreateText("SeasonID", 600, 1, 630)
        self.TextIndex.PrintCallendar.SeasonID = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintCallendar.SeasonID], "File name containing season data")

        self.Gui.Entry.CreateEntry(700, 1, 639)
        self.EntryIndex.PrintCallendar.SeasonID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.PrintCallendar.SeasonID].AddList(GetAnimeList.GetListedSeasons)
        self.Gui.EntryList[self.EntryIndex.PrintCallendar.SeasonID].config(width=12)
    

    def OpenSeasonLink(self):
        self.Gui.Button.CreateBut('OpenSeasonLink', self.Gui.WatchaExec.OpenSeasonLink , 170, 1 , 680)
        self.ButtonIndex.OpenSeasonLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.OpenSeasonLink].config(width=16)

        self.Gui.Text.CreateText("SeasonID", 80, 1, 630)
        self.TextIndex.OpenSeasonLink.SeasonID = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(170, 1, 639)
        self.EntryIndex.OpenSeasonLink.SeasonID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.OpenSeasonLink.SeasonID].AddList(GetAnimeList.GetListedSeasons)
        self.Gui.EntryList[self.EntryIndex.OpenSeasonLink.SeasonID].config(width=12)



