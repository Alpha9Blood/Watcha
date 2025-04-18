from typing import Callable
import os
from Script.GUI_Index import CustomI
from Script.Utils import Math


class ViewList:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.CustomIndex = CustomI()
        self.ViewIndex:int = 0
        self.CurrentPage:int = 0
        self.PreviousPage:int = 0
        self.lines:int = 0
        self.SelectedList:list[str] = []
        self.__AnimeOrMangaList:tuple[Callable, Callable] = (lambda x: x, lambda x: x)

    def SetViewLines(self, AnimeOrMangalist:list[str]):
        self.lines = Math.RoundUp(len(AnimeOrMangalist), 5)

    def SelectList(self, AnimeOrManga:str, List:list[str] = []):
        if (AnimeOrManga.lower() == "anime"):
            self.__AnimeOrMangaList = (self.Gui.AnimeExec.ViewAll, self.Gui.AnimeExec.ViewPrevious)
        elif (AnimeOrManga.lower() == "manga"):
            self.__AnimeOrMangaList = (self.Gui.MangaExec.ViewAll, self.Gui.MangaExec.ViewPrevious)
        else:
            raise Exception("SelectList: Invalid AnimeOrManga")
        
        self.SelectedList = List
            
    
    def ViewNextButton(self):
        if (self.CurrentPage >= self.lines):
            return
        
        self.Gui.Button.CreateBut('Next', self.__AnimeOrMangaList[0] , 800, 1 , 20)
        
    
    def ViewPreviousButton(self):
        if (self.CurrentPage < 3):
            return
        
        self.Gui.Button.CreateBut('Previous', self.__AnimeOrMangaList[1] , 500, 1 , 20)

    def ViewReset(self):
        self.Gui.Models.DeletePreset()
        self.Gui.Presets.CustomPresets.ReturnToMenu()
        self.Gui.Presets.ViewList.ViewNextButton()
        self.Gui.Presets.ViewList.ViewPreviousButton()