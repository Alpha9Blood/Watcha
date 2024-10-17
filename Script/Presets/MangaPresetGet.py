from Script.GUI_Index import MangaGet
from Script.Data.MangaLists import GetMangaList
class MangaPresetGet:
    def __init__(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI
        self.ButtonIndex = MangaGet.ButtonIndex()
        self.EntryIndex = MangaGet.EntryIndex()
        self.TextIndex = MangaGet.TextIndex()
    

    def PrintManga(self):
        self.Gui.Button.CreateBut('PrintManga', self.Gui.MangaExec.PrintManga , 230, 1 , 80)
        self.ButtonIndex.PrintManga = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintManga].config(width=12)

        self.Gui.Texto.CreateText("Name", 80, 1, 30)
        self.TextIndex.PrintManga.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintManga.Name], "Can be simplified.")
        self.Gui.Entry.CreateEntry(170, 1, 39)
        self.EntryIndex.PrintManga.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.PrintManga.Name].AddList(GetMangaList.MangaList)
        self.Gui.EntryList[self.EntryIndex.PrintManga.Name].config(width=25)
    
    def PrintCurrentStatus(self):
        self.Gui.Button.CreateBut('PrintCurrentStatus', self.Gui.MangaExec.PrintCurrentStatus , 230, 1 , 200)
        self.ButtonIndex.PrintCurrentStatus = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintCurrentStatus].config(width=18)

        self.Gui.Texto.CreateText("Status", 80, 1, 150)
        self.TextIndex.PrintCurrentStatus.Status = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintCurrentStatus.Status], "Can be Reading, PlanToRead, Completed or Dropped. If nothing is selected, all statuses will be printed.")
        self.Gui.Entry.CreateEntry(180, 1, 160)
        self.EntryIndex.PrintCurrentStatus.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.PrintCurrentStatus.Status].AddList(GetMangaList.CurrentStatusTypeList)
        self.Gui.EntryList[self.EntryIndex.PrintCurrentStatus.Status].config(width=8)
    
    def OpenLink(self):
        self.Gui.Button.CreateBut('OpenLink', self.Gui.MangaExec.OpenLink , 230, 1 , 320)
        self.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()

        self.Gui.Texto.CreateText("Name", 80, 1, 270)
        self.TextIndex.OpenLink.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.OpenLink.Name], "Can be simplified.")
        self.Gui.Entry.CreateEntry(180, 1, 280)
        self.EntryIndex.OpenLink.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.EntryIndex.OpenLink.Name].AddList(GetMangaList.MangaList)
        self.Gui.EntryList[self.EntryIndex.OpenLink.Name].config(width=25)
    
    def PrintFavorites(self):
        self.Gui.Button.CreateBut('PrintFavorites', self.Gui.MangaExec.PrintFavorites , 1200, 1, 90)
        self.ButtonIndex.PrintFavorites = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.ButtonIndex.PrintFavorites].config(width=15)