from Script.Data.AnimeLists import GetAnimeList
from WatchaScript import Watch
from Script.GUI_Index import AnimeGet

class AnimeListManager:
    def __init__(self):
        self.Options:list[str] = self.GetList()
        self.SelectedFilter = self.GetList()[0]
        self.SelectedList:list[str] = []
        self.EntryIndex = AnimeGet.EntryIndex()
    
    def GuiInit(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI
    
    def ClearCustomLists(self):
        self.Gui.Entry.EntryType.AnimeList.clear()
        self.Gui.Entry.EntryType.UpdateList.clear()
    
    def GetList(self) -> list[str]:
        List:list[str] = ["All"] + GetAnimeList.GetListedSeasons()
        return List

    def UpdateFilter(self):
        Entry = self.Gui.EntryList[self.EntryIndex.FilterOptions.Selected].get()
        self.SelectedFilter = Entry
        
    
    def UpdateList(self):
        self.UpdateFilter()
        if (self.SelectedFilter == "All"):
            self.SelectedList = GetAnimeList.AnimeList()
        else:
            if (self.SelectedFilter in GetAnimeList.GetListedSeasons()):
                self.SelectedList = Watch.GetSeason(self.SelectedFilter)
            else:
                print("Season not found")
                self.SelectedList = []

    def GetFilter(self) -> str:
        self.UpdateFilter()
        return self.SelectedFilter
    
    
    def GetSelectedList(self) -> list[str]:
        self.UpdateList()
        return self.SelectedList