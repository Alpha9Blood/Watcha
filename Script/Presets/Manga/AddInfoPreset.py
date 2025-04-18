from Script.GUI_Index import MangaI
from Script.ManageData.Manga.MangaLists import GetMangaList
class AddInfo:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.MangaIndex:MangaI = MangaI()


    def AddNewManga(self):
        self.Gui.Button.CreateBut('AddNewManga', self.Gui.MangaExec.AddNewManga , 350, 1 , 110)
        self.MangaIndex.AddNewManga.ButtonIndex.AddNewManga = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.AddNewManga.ButtonIndex.AddNewManga].UpdateOnPress(self.Gui.Entry.UpdateEntrysOptions)
        self.Gui.ButList[self.MangaIndex.AddNewManga.ButtonIndex.AddNewManga].config(width=12)

        self.Gui.Text.CreateLabel("Name", 100, 1, 30)
        self.MangaIndex.AddNewManga.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 1, 37)
        self.MangaIndex.AddNewManga.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.AddNewManga.EntryIndex.Name].config(width=25)

        self.Gui.Text.CreateLabel("Chapters", 100, 2)
        self.MangaIndex.AddNewManga.TextIndex.Chapters = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 2)
        self.MangaIndex.AddNewManga.EntryIndex.Chapters = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.MangaIndex.AddNewManga.EntryIndex.Chapters])
        self.Gui.EntryList[self.MangaIndex.AddNewManga.EntryIndex.Chapters].config(width=4)

        self.Gui.Text.CreateLabel("Status", 100, 3)
        self.MangaIndex.AddNewManga.TextIndex.Status = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.LabelList[self.MangaIndex.AddNewManga.TextIndex.Status], "Can be Reading, PlanToRea, Completed or Dropped.")
        self.Gui.Entry.CreateEntry(200, 3)
        self.MangaIndex.AddNewManga.EntryIndex.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.AddNewManga.EntryIndex.Status].AddList(GetMangaList.CurrentStatusTypeList)
        self.Gui.EntryList[self.MangaIndex.AddNewManga.EntryIndex.Status].config(width=10)

    def SetLink(self):
        self.Gui.Button.CreateBut('SetLink', self.Gui.MangaExec.SetLink , 325, 1 , 324)
        self.MangaIndex.SetLink.ButtonIndex.SetLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.SetLink.ButtonIndex.SetLink].config(width=12)

        self.Gui.Text.CreateLabel("Name", 100, 1, 220)
        self.MangaIndex.SetLink.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 1, 229)
        self.MangaIndex.SetLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.SetLink.EntryIndex.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.MangaIndex.SetLink.EntryIndex.Name])
        self.Gui.EntryList[self.MangaIndex.SetLink.EntryIndex.Name].config(width=25)

        self.Gui.Text.CreateLabel("Link", 100, 2)
        self.MangaIndex.SetLink.TextIndex.Link = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Entry.CreateEntry(200, 2)
        self.MangaIndex.SetLink.EntryIndex.Link = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.SetLink.EntryIndex.Link].config(width=25)
    
    def SetMyAnimeListLink(self):
        self.Gui.Button.CreateBut('SetMyAnimeListLink', self.Gui.MangaExec.AddMyAnimeListLink, 250, 1 , 620)
        self.MangaIndex.SetMyAnimeListLink.ButtonIndex.AddLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.SetMyAnimeListLink.ButtonIndex.AddLink].config(width=20)

        self.Gui.Text.CreateLabel("Name", 100, 1, 520)
        self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(200, 1, 530)
        self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name].AddList(GetMangaList.MangaList)
        self.Gui.Entry.EntryFilter.UpdateList.append(self.Gui.EntryList[self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name])
        self.Gui.EntryList[self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name].config(width=25)

        self.Gui.Text.CreateLabel("MyAnimeListLink", 40, 2)
        self.MangaIndex.SetMyAnimeListLink.TextIndex.Link = self.Gui.Presets.UpdateTextIndex()
        self.Gui.LabelList[self.MangaIndex.SetMyAnimeListLink.TextIndex.Link].config(width=16, font=('Arial', 13))

        self.Gui.Entry.CreateEntry(200, 2)
        self.MangaIndex.SetMyAnimeListLink.EntryIndex.Link = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.SetMyAnimeListLink.EntryIndex.Link].config(width=25)