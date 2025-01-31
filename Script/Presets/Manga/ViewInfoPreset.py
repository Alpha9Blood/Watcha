from Script.GUI_Index import MangaI
from Script.ManageData.Manga.MangaLists import GetMangaList
class ViewInfo:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.MangaIndex = MangaI()

    def PrintInfo(self):
        self.Gui.Button.CreateBut('PrintInfo', self.Gui.MangaExec.PrintManga , 230, 1 , 80)
        self.MangaIndex.PrintInfo.ButtonIndex.PrintInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.PrintInfo.ButtonIndex.PrintInfo].config(width=12)

        self.Gui.Text.CreateText("Name", 80, 1, 30)
        self.MangaIndex.PrintInfo.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.MangaIndex.PrintInfo.TextIndex.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 39)
        self.MangaIndex.PrintInfo.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.PrintInfo.EntryIndex.Name].AddList(GetMangaList.MangaList)
        self.Gui.EntryList[self.MangaIndex.PrintInfo.EntryIndex.Name].config(width=25)
    
    def PrintCurrentStatus(self):
        self.Gui.Button.CreateBut('PrintCurrentStatus', self.Gui.MangaExec.PrintCurrentStatus , 230, 1 , 200)
        self.MangaIndex.PrintCurrentStatus.ButtonIndex.PrintCurrentStatus = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.PrintCurrentStatus.ButtonIndex.PrintCurrentStatus].config(width=18)

        self.Gui.Text.CreateText("Status", 80, 1, 150)
        self.MangaIndex.PrintCurrentStatus.TextIndex.Status = self.Gui.Presets.UpdateTextIndex()
        Text:str = "Can be Reading, PlanToRead, Completed or Dropped. If nothing is selected, all statuses will be printed."
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.MangaIndex.PrintCurrentStatus.TextIndex.Status], Text)

        self.Gui.Entry.CreateEntry(180, 1, 160)
        self.MangaIndex.PrintCurrentStatus.EntryIndex.Status = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.MangaIndex.PrintCurrentStatus.EntryIndex.Status].AddList(GetMangaList.CurrentStatusTypeList)
        self.Gui.EntryList[self.MangaIndex.PrintCurrentStatus.EntryIndex.Status].config(width=8)
    
    def PrintFavorites(self):
        self.Gui.Button.CreateBut('PrintFavorites', self.Gui.MangaExec.PrintFavorites , 1200, 1, 90)
        self.MangaIndex.PrintFavorites.ButtonIndex.PrintFavorites = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MangaIndex.PrintFavorites.ButtonIndex.PrintFavorites].config(width=15)