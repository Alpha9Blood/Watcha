from Script.GUI_Index import AnimeSet
from Script.Data.AnimeLists import GetAnimeList
class AnimePresetSet:
    def __init__(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI
        self.ButtonIndex = AnimeSet.ButtonIndex()
        self.EntryIndex = AnimeSet.EntryIndex()
        self.TextIndex = AnimeSet.TextIndex()
                

    def AddAnime(self):

        #AddAnime
        self.Gui.Button.CreateBut('AddAnime', self.Gui.WatchaExec.Add , 355, 1 , 123)
        self.ButtonIndex.AddAnime = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.AddAnime].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        
        #Name
        self.Gui.Entry.CreateEntry(200, 1, 39)
        self.EntryIndex.AddAnime.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddAnime.Name].config(width=25)               
        #MaxEp
        self.Gui.Entry.CreateEntry(200, 2)
        self.EntryIndex.AddAnime.MaxEp = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddAnime.MaxEp].config(width=2)
        #Status
        self.Gui.Entry.CreateEntry(200, 3)
        self.EntryIndex.AddAnime.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddAnime.Status].config(width=11)
        self.Gui.EntryList[self.EntryIndex.AddAnime.Status].AddList(GetAnimeList.CurrentStatusTypeList)
        #Season
        self.Gui.Entry.CreateEntry(200, 4)
        self.EntryIndex.AddAnime.Season = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddAnime.Season].AddList(GetAnimeList.GetListedSeasons)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.AddAnime.Season])
        self.Gui.EntryList[self.EntryIndex.AddAnime.Season].config(width=12)
        #Serie
        self.Gui.Entry.CreateEntry(200, 5)
        self.EntryIndex.AddAnime.Serie = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddAnime.Serie].AddList(GetAnimeList.SerieList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.AddAnime.Serie])
        self.Gui.EntryList[self.EntryIndex.AddAnime.Serie].config(width=15)

        #Name
        self.Gui.Text.CreateText("Name", 100, 1, 30)
        self.TextIndex.AddAnime.Name = self.Gui.Presets.UpdateTextIndex()
        #MaxEp
        self.Gui.Text.CreateText("MaxEp", 100, 2)
        self.TextIndex.AddAnime.MaxEp = self.Gui.Presets.UpdateTextIndex()
        #Status
        self.Gui.Text.CreateText("Status", 100, 3)
        self.TextIndex.AddAnime.Status = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddAnime.Status], "Can be Watching, Completed, Dropped, or PlanToWatch.")
        #Season
        self.Gui.Text.CreateText("Season", 100, 4)
        self.TextIndex.AddAnime.Season = self.Gui.Presets.UpdateTextIndex()
        #Serie
        self.Gui.Text.CreateText("Serie", 100, 5)
        self.TextIndex.AddAnime.Serie = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddAnime.Serie], "Is optional.")


    def DeleteAnime(self):
        self.Gui.Button.CreateBut('DeleteAnime', self.Gui.WatchaExec.RemoveAnime , 1100, 1 , 670)
        self.ButtonIndex.DeleteAnime = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.DeleteAnime].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)

        self.Gui.Text.CreateText("Name", 1100, 1, 612)
        self.TextIndex.DeleteAnime.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(1200, 1, 620)
        self.EntryIndex.DeleteAnime.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.DeleteAnime.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.DeleteAnime.Name])
        self.Gui.EntryList[self.EntryIndex.DeleteAnime.Name].config(width=25)


    def AddEpisode(self):
        self.Gui.Button.CreateBut('AddEp', self.Gui.WatchaExec.AddEppisode , 1180, 1 , 150)
        self.ButtonIndex.AddEpisode = self.Gui.Presets.UpdateButtonIndex()


        self.Gui.Button.CreateBut('SetEp', self.Gui.WatchaExec.SetEpisode , 1315, 1 , 150)
        self.ButtonIndex.SetEpisode = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Text.CreateText("AddEpisode", 1250, 1, 25)
        self.TextIndex.AddEpisode.Title = self.Gui.Presets.UpdateTextIndex()
        self.Gui.TextList[self.TextIndex.AddEpisode.Title].config(width=12, height= 3, font=('Arial', 13))

        self.Gui.Text.CreateText("Name", 1072, 1, 102)
        self.TextIndex.AddEpisode.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddEpisode.Name], "Can be simplified.")
        
        self.Gui.Entry.CreateEntry(1168, 1, 110)
        self.EntryIndex.AddEpisode.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddEpisode.Name].AddList(GetAnimeList.OnGoingList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.AddEpisode.Name])
        self.Gui.EntryList[self.EntryIndex.AddEpisode.Name].config(width=25)     
        
        self.Gui.Entry.CreateEntry(1355, 1, 226)
        self.EntryIndex.AddEpisode.Ep = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddEpisode.Ep].config(width=2)


    def UpdateScore(self):
        self.Gui.Button.CreateBut('UpdateScore', self.Gui.WatchaExec.UpdateScore , 1230, 1 , 360)
        self.ButtonIndex.UpdateScore = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Text.CreateText("Name", 1062, 1, 318)
        self.TextIndex.UpdateScore.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(1155, 1, 326)
        self.EntryIndex.UpdateScore.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.UpdateScore.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.UpdateScore.Name])
        self.Gui.EntryList[self.EntryIndex.UpdateScore.Name].config(width=25)
        
        self.Gui.Entry.CreateEntry(1465, 1, 330)
        self.EntryIndex.UpdateScore.Score = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.UpdateScore.Score].config(width=3)


    def RemoveLeastAdded(self):
        self.Gui.Button.CreateBut('RemoveLeastAdded', self.Gui.WatchaExec.RemoveLeastAdded , 1300, 1 , 670)
        self.ButtonIndex.RemoveLeastAdded = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.RemoveLeastAdded].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.ButtonIndex.RemoveLeastAdded].config(width=19)


    def SetCurrentStatus(self):        
        self.Gui.Button.CreateBut('SetCurrentStatus', self.Gui.WatchaExec.OverrideCurrentStatus, 1340, 1 , 500)
        self.ButtonIndex.SetCurrentStatus = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.SetCurrentStatus].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.ButtonIndex.SetCurrentStatus].config(width=14)
        
        self.Gui.Text.CreateText("Name", 1080, 1, 450)
        self.TextIndex.SetCurrentStatus.Name = self.Gui.Presets.UpdateTextIndex()             
        
        self.Gui.Entry.CreateEntry(1180, 1, 460)
        self.EntryIndex.SetCurrentStatus.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetCurrentStatus.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.SetCurrentStatus.Name])
        self.Gui.EntryList[self.EntryIndex.SetCurrentStatus.Name].config(width=25)
        
        self.Gui.Text.CreateText("SetStatus", 1080, 2)
        self.TextIndex.SetCurrentStatus.SetStatus = self.Gui.Presets.UpdateTextIndex()
        self.Gui.TextList[self.TextIndex.SetCurrentStatus.SetStatus].config(width=10)
        
        self.Gui.Entry.CreateEntry(1180, 2)
        self.EntryIndex.SetCurrentStatus.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetCurrentStatus.Status].AddList(GetAnimeList.CurrentStatusTypeList)
        self.Gui.EntryList[self.EntryIndex.SetCurrentStatus.Status].config(width=11)

        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.SetCurrentStatus.SetStatus], "Can be Watching, Completed, Dropped, or PlanToWatch.")
        
        
    def SetMyAnimeListLink(self):
        self.Gui.Button.CreateBut('SetMyAnimeListLink', self.Gui.WatchaExec.AddMyAnimeListLink, 250, 1 , 420)
        self.ButtonIndex.SetMyAnimeListLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.SetMyAnimeListLink].config(width=20)

        self.Gui.Text.CreateText("Name", 100, 1, 320)
        self.TextIndex.MyAnimeListLink.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 1, 330)
        self.EntryIndex.MyAnimeListLink.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.MyAnimeListLink.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.MyAnimeListLink.Name])
        self.Gui.EntryList[self.EntryIndex.MyAnimeListLink.Name].config(width=25)

        self.Gui.Text.CreateText("MyAnimeListLink", 40, 2)
        self.TextIndex.MyAnimeListLink.Link = self.Gui.Presets.UpdateTextIndex()
        self.Gui.TextList[self.TextIndex.MyAnimeListLink.Link].config(width=16, font=('Arial', 13))

        self.Gui.Entry.CreateEntry(200, 2)
        self.EntryIndex.MyAnimeListLink.Link = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.MyAnimeListLink.Link].config(width=25)
    

    def AddToCalendar(self):
        self.Gui.Button.CreateBut('AddToCalendar', self.Gui.WatchaExec.AddToCalendar, 700, 1 , 660)
        self.ButtonIndex.AddToCallendar = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.AddToCallendar].config(width=13)

        self.Gui.Text.CreateText("Name", 600, 1, 550)
        self.TextIndex.AddToCallendar.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(700, 1, 559)
        self.EntryIndex.AddToCallendar.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddToCallendar.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.AddToCallendar.Name])
        self.Gui.EntryList[self.EntryIndex.AddToCallendar.Name].config(width=25)

        self.Gui.Text.CreateText("Day", 600, 2)
        self.TextIndex.AddToCallendar.Day = self.Gui.Presets.UpdateTextIndex()
        
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddToCallendar.Day], "Can be one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.")

        self.Gui.Entry.CreateEntry(700, 2)
        self.EntryIndex.AddToCallendar.Day = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddToCallendar.Day].AddList(GetAnimeList.DaysList)
        self.Gui.EntryList[self.EntryIndex.AddToCallendar.Day].config(width=10)


    def SetSeasonLink(self):
        self.Gui.Button.CreateBut('SetSeasonLink', self.Gui.WatchaExec.SetSeasonLink, 200, 1 , 610)
        self.ButtonIndex.SetSeasonLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.SetSeasonLink].config(width=18)

        self.Gui.Text.CreateText("SeasonID", 100, 1, 510)
        self.TextIndex.SetSeasonLink.SeasonID = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 1, 519)
        self.EntryIndex.SetSeasonLink.SeasonID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetSeasonLink.SeasonID].AddList(GetAnimeList.GetListedSeasons)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.SetSeasonLink.SeasonID])
        self.Gui.EntryList[self.EntryIndex.SetSeasonLink.SeasonID].config(width=12)

        self.Gui.Text.CreateText("Link", 100, 2)
        self.TextIndex.SetSeasonLink.SeasonID = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 2)
        self.EntryIndex.SetSeasonLink.Link = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetSeasonLink.Link].config(width=25)