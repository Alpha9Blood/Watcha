from Script.ManageData.Anime.AnimeLists import GetAnimeList
from AnimeScript import Watch
from Script.GUI_Index import CustomI

class AnimeListManager:
    def __init__(self):
        self.Options:list[str] = self.GetList()
        self.SelectedFilter = self.GetList()[0]
        self.SelectedList:list[str] = []
        self.CustomIndex = CustomI()
    
    def GuiInit(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
    
    def ClearCustomLists(self):
        self.Gui.Entry.EntryFilter.AnimeList.clear()
        self.Gui.Entry.EntryFilter.UpdateList.clear()
    
    def GetList(self) -> list[str]:
        List:list[str] = ["All"] + GetAnimeList.GetListedSeasons()
        return List

    def UpdateFilter(self):
        Entry = self.Gui.EntryList[self.CustomIndex.Filter.EntryIndex.Selected].get()
        self.SelectedFilter = Entry
        
    
    def UpdateList(self):
        self.UpdateFilter()
        if (self.SelectedFilter == "All"):
            self.SelectedList = GetAnimeList.AnimeList()
        else:
            if (self.SelectedFilter in GetAnimeList.GetListedSeasons()):
                self.SelectedList = GetAnimeList.GetSeason(self.SelectedFilter)
            else:
                print("Season not found")
                self.SelectedList.clear()

    def GetFilter(self) -> str:
        self.UpdateFilter()
        return self.SelectedFilter
    
    
    def GetSelectedList(self) -> list[str]:
        self.UpdateList()
        return self.SelectedList