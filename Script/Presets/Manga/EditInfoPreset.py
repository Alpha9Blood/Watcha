from Script.GUI_Index import MangaI
from Script.ManageData.Manga.MangaLists import GetMangaList
class EditInfo:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.MangaIndex:MangaI = MangaI()

    def EditChapters(self):
        self.Gui.Button.CreateBut('AddChapters', self.Gui.MangaExec.AddChapters , 1180, 1 , 150)
        self.MangaIndex.EditChapters.ButtonIndex.AddChapters = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.EditChapters.ButtonIndex.AddChapters].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)

        self.Gui.Button.CreateBut('SetChapters', self.Gui.MangaExec.SetChapters , 1315, 1 , 150)
        self.MangaIndex.EditChapters.ButtonIndex.SetChapters = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.EditChapters.ButtonIndex.SetChapters].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)

        self.Gui.Text.CreateLabel("EditChapters", 1250, 1, 25)
        self.MangaIndex.EditChapters.TextIndex.Title = self.Gui.Presets.UpdateTextIndex()
        self.Gui.LabelList[self.MangaIndex.EditChapters.TextIndex.Title].config(width=12, height= 3, font=('Arial', 13))

        self.Gui.Text.CreateLabel("Name", 1072, 1, 102)
        self.MangaIndex.EditChapters.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.LabelList[self.MangaIndex.EditChapters.TextIndex.Name], "Can be simplified.")
        self.Gui.Entry.CreateEntry(1168, 1, 110)
        self.MangaIndex.EditChapters.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.EditChapters.EntryIndex.Name].AddList(GetMangaList.OnGoingList)
        self.Gui.EntryList[self.MangaIndex.EditChapters.EntryIndex.Name].config(width=25)     
        
        self.Gui.Entry.CreateEntry(1355, 1, 226)
        self.MangaIndex.EditChapters.EntryIndex.Chapter = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.EditChapters.EntryIndex.Chapter].config(width=3)

    def RemoveManga(self):
        self.Gui.Button.CreateBut('RemoveManga', self.Gui.MangaExec.DeleteManga , 1290, 1 , 634)
        self.MangaIndex.RemoveManga.ButtonIndex.RemoveManga = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.RemoveManga.ButtonIndex.RemoveManga].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.MangaIndex.RemoveManga.ButtonIndex.RemoveManga].config(width=12)

        self.Gui.Text.CreateLabel("Name", 1080, 1, 580)
        self.MangaIndex.RemoveManga.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(1180, 1, 589)
        self.MangaIndex.RemoveManga.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.RemoveManga.EntryIndex.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.MangaIndex.RemoveManga.EntryIndex.Name])
        self.Gui.EntryList[self.MangaIndex.RemoveManga.EntryIndex.Name].config(width=25)
    
    def EditInfo(self):
        self.Gui.Button.CreateBut('UpdateInfo', self.Gui.MangaExec.EditInfo , 280, 1, 180)
        self.MangaIndex.EditInfo.ButtonIndex.SetStatus = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.EditInfo.ButtonIndex.SetStatus].config(width=12)

        self.Gui.Text.CreateLabel("Name", 100, 1, 120)
        self.MangaIndex.EditInfo.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 1, 130)
        self.MangaIndex.EditInfo.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.EditInfo.EntryIndex.Name].AddList(GetMangaList.MangaList)  
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.MangaIndex.EditInfo.EntryIndex.Name])
        self.Gui.EntryList[self.MangaIndex.EditInfo.EntryIndex.Name].config(width=25)

        self.Gui.Text.CreateLabel("Score", 100, 1, 200)
        self.MangaIndex.EditInfo.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        
        self.Gui.Entry.CreateEntry(200, 1, 210)
        self.MangaIndex.EditInfo.EntryIndex.Score = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.EditInfo.EntryIndex.Score].config(width=3)

        self.Gui.Text.CreateLabel("Status", 100, 2)
        self.MangaIndex.EditInfo.TextIndex.Status = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 2)
        self.MangaIndex.EditInfo.EntryIndex.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.EditInfo.EntryIndex.Status].AddList(GetMangaList.CurrentStatusTypeList)
        self.Gui.EntryList[self.MangaIndex.EditInfo.EntryIndex.Status].config(width=8)

    def EditFavorites(self):
        self.Gui.Button.CreateBut('AddFavorite', self.Gui.MangaExec.AddFavorite , 120, 1 , 470)
        self.MangaIndex.EditFavorites.ButtonIndex.AddFavorites = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.EditFavorites.ButtonIndex.AddFavorites].config(width=12)

        self.Gui.Button.CreateBut('DeleteFavorites', self.Gui.MangaExec.DeleteFavorite , 320, 1 , 470)
        self.MangaIndex.EditFavorites.ButtonIndex.DeleteFavorites = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.EditFavorites.ButtonIndex.DeleteFavorites].config(width=14)

        self.Gui.Text.CreateLabel("Name", 100, 1, 420)
        self.MangaIndex.EditFavorites.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 1, 429)
        self.MangaIndex.EditFavorites.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.EditFavorites.EntryIndex.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.MangaIndex.EditFavorites.EntryIndex.Name])
        self.Gui.EntryList[self.MangaIndex.EditFavorites.EntryIndex.Name].config(width=25)
        
        