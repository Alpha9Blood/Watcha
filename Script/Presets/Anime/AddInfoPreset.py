from Script.GUI_Index import AnimeI
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.ManageData.Anime.ManageSeasons import SeasonManager
class AddInfo:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.AnimeIndex =  AnimeI()

    def AddAnime(self):
        #AddAnime
        self.Gui.Button.CreateBut('AddAnime', self.Gui.AnimeExec.Add , 355, 1 , 83)
        self.AnimeIndex.AddAnime.ButtonIndex.AddAnime = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.AddAnime.ButtonIndex.AddAnime].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        
        #Name
        self.Gui.Entry.CreateEntry(200, 1, 39)
        self.AnimeIndex.AddAnime.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.Name].config(width=25)               
        #MaxEp
        self.Gui.Entry.CreateEntry(200, 2)
        self.AnimeIndex.AddAnime.EntryIndex.MaxEp = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.MaxEp].config(width=2)
        #Status
        self.Gui.Entry.CreateEntry(200, 3)
        self.AnimeIndex.AddAnime.EntryIndex.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.Status].config(width=11)
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.Status].AddList(GetAnimeList.CurrentStatusTypeList)
        #Season
        self.Gui.Entry.CreateEntry(200, 4)
        self.AnimeIndex.AddAnime.EntryIndex.SeasonName = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonName].AddList(SeasonManager.ReturnSeasons, True)
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonName].config(width=8)

        self.Gui.Entry.CreateEntry(400, 4)
        self.AnimeIndex.AddAnime.EntryIndex.SeasonYear = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonYear].AddList(SeasonManager.ReturnSeasonsYears)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonYear])
        #Serie
        self.Gui.Entry.CreateEntry(200, 5)
        self.AnimeIndex.AddAnime.EntryIndex.Serie = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.Serie].AddList(GetAnimeList.SerieList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.Serie])
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.Serie].config(width=16)

        #Name
        self.Gui.Text.CreateText("Name", 100, 1, 30)
        self.AnimeIndex.AddAnime.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        #MaxEp
        self.Gui.Text.CreateText("MaxEp", 100, 2)
        self.AnimeIndex.AddAnime.TextIndex.MaxEp = self.Gui.Presets.UpdateTextIndex()
        #Status
        self.Gui.Text.CreateText("Status", 100, 3)
        self.AnimeIndex.AddAnime.TextIndex.Status = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.AddAnime.TextIndex.Status], "Can be Watching, Completed, Dropped, or PlanToWatch.")
        #Season
        self.Gui.Text.CreateText("Season", 100, 4)
        self.AnimeIndex.AddAnime.TextIndex.Season = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Text.CreateText("Year", 320, 4)
        self.AnimeIndex.AddAnime.TextIndex.Year = self.Gui.Presets.UpdateTextIndex()
        #Serie
        self.Gui.Text.CreateText("Serie", 100, 5)
        self.AnimeIndex.AddAnime.TextIndex.Serie = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.AddAnime.TextIndex.Serie], "Is optional.")
    
    def SetMyAnimeListLink(self):
        self.Gui.Button.CreateBut('SetMyAnimeListLink', self.Gui.AnimeExec.AddMyAnimeListLink, 250, 1 , 420)
        self.AnimeIndex.SetMyAnimeListLink.ButtonIndex.MyAnimeListLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.SetMyAnimeListLink.ButtonIndex.MyAnimeListLink].config(width=20)

        self.Gui.Text.CreateText("Name", 100, 1, 320)
        self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 1, 330)
        self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name])
        self.Gui.EntryList[self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Name].config(width=25)

        self.Gui.Text.CreateText("MyAnimeListLink", 40, 2)
        self.AnimeIndex.SetMyAnimeListLink.TextIndex.Link = self.Gui.Presets.UpdateTextIndex()
        self.Gui.TextList[self.AnimeIndex.SetMyAnimeListLink.TextIndex.Link].config(width=16, font=('Arial', 13))

        self.Gui.Entry.CreateEntry(200, 2)
        self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Link = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.SetMyAnimeListLink.EntryIndex.Link].config(width=25)
    
    def SetWatchLink(self):
        self.Gui.Button.CreateBut('SetWatchLink', self.Gui.AnimeExec.SetWatchLink, 200, 1 , 610)
        self.AnimeIndex.SetWatchLink.ButtonIndex.WatchLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.SetWatchLink.ButtonIndex.WatchLink].config(width=18)

        self.Gui.Text.CreateText("Name", 100, 1, 510)
        self.AnimeIndex.SetWatchLink.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 1, 519)
        self.AnimeIndex.SetWatchLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.SetWatchLink.EntryIndex.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.SetWatchLink.EntryIndex.Name])
        self.Gui.EntryList[self.AnimeIndex.SetWatchLink.EntryIndex.Name].config(width=25)

        self.Gui.Text.CreateText("Link", 100, 2)
        self.AnimeIndex.SetWatchLink.TextIndex.Link = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 2)
        self.AnimeIndex.SetWatchLink.EntryIndex.Link = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.SetWatchLink.EntryIndex.Link].config(width=25)
    
    def AddToCalendar(self):
        self.Gui.Button.CreateBut('AddToCalendar', self.Gui.AnimeExec.AddToCalendar, 700, 1 , 660)
        self.AnimeIndex.AddToCallendar.ButtonIndex.AddToCallendar = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.AddToCallendar.ButtonIndex.AddToCallendar].config(width=13)

        self.Gui.Text.CreateText("Name", 600, 1, 550)
        self.AnimeIndex.AddToCallendar.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(700, 1, 559)
        self.AnimeIndex.AddToCallendar.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddToCallendar.EntryIndex.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.AddToCallendar.EntryIndex.Name])
        self.Gui.EntryList[self.AnimeIndex.AddToCallendar.EntryIndex.Name].config(width=25)

        self.Gui.Text.CreateText("Day", 600, 2)
        self.AnimeIndex.AddToCallendar.TextIndex.Day = self.Gui.Presets.UpdateTextIndex()
        
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.AddToCallendar.TextIndex.Day], "Can be one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.")

        self.Gui.Entry.CreateEntry(700, 2)
        self.AnimeIndex.AddToCallendar.EntryIndex.Day = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddToCallendar.EntryIndex.Day].AddList(GetAnimeList.DaysList)
        self.Gui.EntryList[self.AnimeIndex.AddToCallendar.EntryIndex.Day].config(width=10)
    
    