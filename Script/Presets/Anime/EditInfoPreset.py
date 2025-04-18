from Script.GUI_Index import AnimeI
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.ManageData.Anime.ManageSeasons import SeasonManager
class EditInfo:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.AnimeIndex = AnimeI()
    
    def DeleteAnime(self):
        self.Gui.Button.CreateBut('DeleteAnime', self.Gui.AnimeExec.RemoveAnime , 1100, 1 , 670)
        self.AnimeIndex.DeleteAnime.ButtonIndex.DeleteAnime = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.DeleteAnime.ButtonIndex.DeleteAnime].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)

        self.Gui.Text.CreateLabel("Name", 1100, 1, 612)
        self.AnimeIndex.DeleteAnime.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(1200, 1, 620)
        self.AnimeIndex.DeleteAnime.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.DeleteAnime.EntryIndex.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.DeleteAnime.EntryIndex.Name])
        self.Gui.EntryList[self.AnimeIndex.DeleteAnime.EntryIndex.Name].config(width=25)


    def UpdateEpisode(self):
        # Title Text
        self.Gui.Text.CreateLabel("UpdateEpisode", 1250, 1, 125)
        self.AnimeIndex.UpdateEpisode.TextIndex.Title = self.Gui.Presets.UpdateTextIndex()
        self.Gui.LabelList[self.AnimeIndex.UpdateEpisode.TextIndex.Title].config(width=16, height=3, font=('Arial', 13))

        # Name Label and Entry
        self.Gui.Text.CreateLabel("Name", 1072, 1, 202)
        self.AnimeIndex.UpdateEpisode.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.LabelList[self.AnimeIndex.UpdateEpisode.TextIndex.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(1168, 1, 210)
        self.AnimeIndex.UpdateEpisode.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.UpdateEpisode.EntryIndex.Name].AddList(GetAnimeList.OnGoingList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.UpdateEpisode.EntryIndex.Name])
        self.Gui.EntryList[self.AnimeIndex.UpdateEpisode.EntryIndex.Name].config(width=25)

        # Episode Entry
        self.Gui.Entry.CreateEntry(1355, 1, 326)
        self.AnimeIndex.UpdateEpisode.EntryIndex.Ep = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.UpdateEpisode.EntryIndex.Ep].config(width=2)

        # Action Buttons
        self.Gui.Button.CreateBut('AddEp', self.Gui.AnimeExec.AddEppisode, 1180, 1, 250)
        self.AnimeIndex.UpdateEpisode.ButtonIndex.AddEpisode = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.UpdateEpisode.ButtonIndex.AddEpisode].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)

        self.Gui.Button.CreateBut('SetEp', self.Gui.AnimeExec.SetEpisode, 1315, 1, 250)
        self.AnimeIndex.UpdateEpisode.ButtonIndex.SetEpisode = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.UpdateEpisode.ButtonIndex.SetEpisode].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)


    def RemoveLeastAdded(self):
        self.Gui.Button.CreateBut('RemoveLeastAdded', self.Gui.AnimeExec.RemoveLeastAdded , 1300, 1 , 670)
        self.AnimeIndex.RemoveLeastAdded.ButtonIndex.RemoveLeastAdded = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.RemoveLeastAdded.ButtonIndex.RemoveLeastAdded].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.AnimeIndex.RemoveLeastAdded.ButtonIndex.RemoveLeastAdded].config(width=19)


    def EditAnimeInfo(self):        
        self.Gui.Button.CreateBut('EditInfo', self.Gui.AnimeExec.EditAnimeInfo, 300, 1 , 180)
        self.AnimeIndex.EditInfo.ButtonIndex.UpdateInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.EditInfo.ButtonIndex.UpdateInfo].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.AnimeIndex.EditInfo.ButtonIndex.UpdateInfo].config(width=14)
        
        self.Gui.Text.CreateLabel("Name", 100, 1, 120)
        self.AnimeIndex.EditInfo.EntryIndex.Name = self.Gui.Presets.UpdateTextIndex()             
        
        self.Gui.Entry.CreateEntry(200, 1, 130)
        self.AnimeIndex.EditInfo.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Name].AddList(GetAnimeList.AnimeList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Name])
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Name].config(width=25)
        
        self.Gui.Text.CreateLabel("MaxEP", 100, 1, 200)
        self.AnimeIndex.EditInfo.TextIndex.Status = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Text.CreateLabel("Status", 100, 2)
        self.AnimeIndex.EditInfo.TextIndex.Status = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Text.CreateLabel("Serie", 100, 3)
        self.AnimeIndex.EditInfo.TextIndex.Serie = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Text.CreateLabel("Season", 100, 4)
        self.AnimeIndex.AddAnime.TextIndex.Season = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Text.CreateLabel("Year", 320, 4)
        self.AnimeIndex.AddAnime.TextIndex.Year = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Text.CreateLabel("Score", 100, 5)
        self.AnimeIndex.EditInfo.TextIndex.Score = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 1, 210)
        self.AnimeIndex.EditInfo.EntryIndex.MaxEp = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.MaxEp].config(width=3)
        
        self.Gui.Entry.CreateEntry(200, 2)
        self.AnimeIndex.EditInfo.EntryIndex.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Status].AddList(GetAnimeList.CurrentStatusTypeList)
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Status].config(width=10)

        self.Gui.Entry.CreateEntry(200, 3)
        self.AnimeIndex.EditInfo.EntryIndex.Serie = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Serie].AddList(GetAnimeList.SerieList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Serie])
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Serie].config(width=16)

        self.Gui.Entry.CreateEntry(200, 4)
        self.AnimeIndex.AddAnime.EntryIndex.SeasonName = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonName].AddList(SeasonManager.ReturnSeasons, True)
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonName].config(width=8)

        self.Gui.Entry.CreateEntry(400, 4)
        self.AnimeIndex.AddAnime.EntryIndex.SeasonYear = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonYear].AddList(SeasonManager.ReturnSeasonsYears)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.AnimeIndex.AddAnime.EntryIndex.SeasonYear])

        self.Gui.Entry.CreateEntry(200, 5)
        self.AnimeIndex.EditInfo.EntryIndex.Score = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.EditInfo.EntryIndex.Score].config(width=5)

        self.Gui.Presets.CreateTooltip(self.Gui.LabelList[self.AnimeIndex.EditInfo.TextIndex.Status], "Can be Watching, Completed, Dropped, or PlanToWatch.")