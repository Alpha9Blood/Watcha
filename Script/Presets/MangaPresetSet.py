from Script.GUI_Index import MangaSet
from Script.Data.MangaLists import GetMangaList
class MangaPresetSet:
    def __init__(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI
        self.ButtonIndex = MangaSet.ButtonIndex()
        self.EntryIndex = MangaSet.EntryIndex()
        self.TextIndex = MangaSet.TextIndex()


    def AddNewManga(self):
        self.Gui.Button.CreateBut('AddNewManga', self.Gui.MangaExec.AddNewManga , 350, 1 , 110)
        self.ButtonIndex.AddNewManga = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.AddNewManga].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.ButtonIndex.AddNewManga].config(width=12)

        self.Gui.Text.CreateText("Name", 100, 1, 30)
        self.TextIndex.AddNewManga.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 1, 37)
        self.EntryIndex.AddNewManga.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddNewManga.Name].config(width=25)

        self.Gui.Text.CreateText("Chapters", 100, 2)
        self.TextIndex.AddNewManga.Chapters = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 2)
        self.EntryIndex.AddNewManga.Chapters = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.AddNewManga.Chapters])
        self.Gui.EntryList[self.EntryIndex.AddNewManga.Chapters].config(width=4)

        self.Gui.Text.CreateText("Status", 100, 3)
        self.TextIndex.AddNewManga.Status = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddNewManga.Status], "Can be Reading, PlanToRea, Completed or Dropped.")
        self.Gui.Entry.CreateEntry(200, 3)
        self.EntryIndex.AddNewManga.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.AddNewManga.Status].AddList(GetMangaList.CurrentStatusTypeList)
        self.Gui.EntryList[self.EntryIndex.AddNewManga.Status].config(width=10)
    

    def RemoveManga(self):
        self.Gui.Button.CreateBut('RemoveManga', self.Gui.MangaExec.DeleteManga , 1290, 1 , 634)
        self.ButtonIndex.DeleteManga = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.DeleteManga].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.ButtonIndex.DeleteManga].config(width=12)

        self.Gui.Text.CreateText("Name", 1080, 1, 580)
        self.TextIndex.DeleteManga.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(1180, 1, 589)
        self.EntryIndex.DeleteManga.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.DeleteManga.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.DeleteManga.Name])
        self.Gui.EntryList[self.EntryIndex.DeleteManga.Name].config(width=25)
    

    def SetLink(self):
        self.Gui.Button.CreateBut('SetLink', self.Gui.MangaExec.SetLink , 325, 1 , 324)
        self.ButtonIndex.SetLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.SetLink].config(width=12)

        self.Gui.Text.CreateText("Name", 100, 1, 220)
        self.TextIndex.SetLink.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 1, 229)
        self.EntryIndex.SetLink.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetLink.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.SetLink.Name])
        self.Gui.EntryList[self.EntryIndex.SetLink.Name].config(width=25)

        self.Gui.Text.CreateText("Link", 100, 2)
        self.TextIndex.SetLink.Link = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 2)
        self.EntryIndex.SetLink.Link = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetLink.Link].config(width=25)


    def EditFavorites(self):
        self.Gui.Button.CreateBut('AddFavorite', self.Gui.MangaExec.AddFavorite , 120, 1 , 470)
        self.ButtonIndex.AddFavorite = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.AddFavorite].config(width=12)

        self.Gui.Button.CreateBut('RemoveFavorite', self.Gui.MangaExec.DeleteFavorite , 320, 1 , 470)
        self.ButtonIndex.DeleteFavorite = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.DeleteFavorite].config(width=14)

        self.Gui.Text.CreateText("Name", 100, 1, 420)
        self.TextIndex.EditFavorites.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 1, 429)
        self.EntryIndex.EditFavorites.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.EditFavorites.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.EditFavorites.Name])
        self.Gui.EntryList[self.EntryIndex.EditFavorites.Name].config(width=25)
    

    def EditChapters(self):
        self.Gui.Button.CreateBut('AddChapters', self.Gui.MangaExec.AddChapters , 1180, 1 , 150)
        self.ButtonIndex.AddChapters = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.AddChapters].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)

        self.Gui.Button.CreateBut('SetChapters', self.Gui.MangaExec.SetChapters , 1315, 1 , 150)
        self.ButtonIndex.SetChapters = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.SetChapters].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)

        self.Gui.Text.CreateText("EditChapters", 1250, 1, 25)
        self.TextIndex.UpdateChapters.Title = self.Gui.Presets.UpdateTextIndex()
        self.Gui.TextList[self.TextIndex.UpdateChapters.Title].config(width=12, height= 3, font=('Arial', 13))

        self.Gui.Text.CreateText("Name", 1072, 1, 102)
        self.TextIndex.UpdateChapters.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.UpdateChapters.Name], "Can be simplified.")
        self.Gui.Entry.CreateEntry(1168, 1, 110)
        self.EntryIndex.UpdateChapters.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.UpdateChapters.Name].AddList(GetMangaList.OnGoingList)
        self.Gui.EntryList[self.EntryIndex.UpdateChapters.Name].config(width=25)     
        
        self.Gui.Entry.CreateEntry(1355, 1, 226)
        self.EntryIndex.UpdateChapters.Chapters = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.UpdateChapters.Chapters].config(width=4)


    def SetStatus(self):
        self.Gui.Button.CreateBut('SetStatus', self.Gui.MangaExec.SetStatus , 1310, 1 , 500)
        self.ButtonIndex.SetStatus = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.SetStatus].config(width=12)

        self.Gui.Text.CreateText("Name", 1080, 1, 450)
        self.TextIndex.SetStatus.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(1180, 1, 460)
        self.EntryIndex.SetStatus.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetStatus.Name].AddList(GetMangaList.MangaList)  
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.SetStatus.Name])
        self.Gui.EntryList[self.EntryIndex.SetStatus.Name].config(width=25)

        self.Gui.Text.CreateText("Status", 1080, 2)
        self.TextIndex.SetStatus.Status = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(1180, 2)
        self.EntryIndex.SetStatus.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.SetStatus.Status].AddList(GetMangaList.CurrentStatusTypeList)
        self.Gui.EntryList[self.EntryIndex.SetStatus.Status].config(width=8)
    

    def EditScore(self):
        self.Gui.Button.CreateBut('UpdateScore', self.Gui.MangaExec.EditScore , 1290, 1 , 350)
        self.ButtonIndex.EditScore = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Text.CreateText("Name", 1080, 1, 300)
        self.TextIndex.EditScore.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(1180, 1, 308)
        self.EntryIndex.EditScore.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.EditScore.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryType.UpdateList.append(self.Gui.EntryList[self.EntryIndex.EditScore.Name])  
        self.Gui.EntryList[self.EntryIndex.EditScore.Name].config(width=25)
        
        self.Gui.Entry.CreateEntry(1490, 1, 310)
        self.EntryIndex.EditScore.Score = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.EditScore.Score].config(width=3)