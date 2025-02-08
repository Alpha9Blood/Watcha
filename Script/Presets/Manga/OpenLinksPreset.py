from Script.GUI_Index import MangaI
from Script.ManageData.Manga.MangaLists import GetMangaList
class OpenLinks:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.MangaIndex = MangaI()
        
    def OpenLink(self):
        self.Gui.Button.CreateBut('OpenLink', self.Gui.MangaExec.OpenLink , 230, 1 , 320)
        self.MangaIndex.OpenLink.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Text.CreateText("Name", 80, 1, 270)
        self.MangaIndex.OpenLink.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.MangaIndex.OpenLink.TextIndex.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(180, 1, 280)
        self.MangaIndex.OpenLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.OpenLink.EntryIndex.Name].AddList(GetMangaList.HasMangaLinkList)
        self.Gui.EntryList[self.MangaIndex.OpenLink.EntryIndex.Name].config(width=25)

    def OpenMyAnimeListLink(self):
        self.Gui.Button.CreateBut('OpenMyAnimeListLink', self.Gui.MangaExec.OpenMAL_Link , 170, 1 , 560)
        self.MangaIndex.OpenMyAnimeListLink.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.OpenMyAnimeListLink.ButtonIndex.OpenLink].config(width=19)

        self.Gui.Text.CreateText("Name", 80, 1, 510)
        self.MangaIndex.OpenMyAnimeListLink.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.MangaIndex.OpenMyAnimeListLink.TextIndex.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 519)
        self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name].AddList(GetMangaList.HasMAL_LinkList)
        self.Gui.EntryList[self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name].config(width=25)