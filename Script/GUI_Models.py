from enum import Enum
import tkinter as tk

class GUI_Models:
    def __init__(self):      
        self.SelectedPreset:Enum = self.Presets.Default
    
    def GuiInit(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.Gui.window.configure(bg='#000000')
        self.Gui.window.title('Watcha')
        self.Gui.window.geometry('1600x800')

    def WhiteModel(self):
        self.Gui.window.configure(bg='#FFFFFF')
        
    def BlackModel(self):
        self.Gui.window.configure(bg='#000000')
    
    def SwitchModels(self):
        if self.Gui.window.cget('bg') == '#000000':
            self.Switch = True
        if (self.Switch):
            self.WhiteModel()
            self.Switch = False
        else:
            self.BlackModel()
    
    def InitDisplay(self):
        self.Gui.Text.GetList = [tk.Text(self.Gui.window), tk.Scrollbar(self.Gui.window)]

    
    
    def DeletePreset(self):
        """
        Deletes the current preset by destroying all GUI elements and resetting the preset lists.

        Resets the following:
            - Button list
            - Entry list
            - Text list
            - Tooltip List
            - Selected preset
            - Preset indexes

        """
        if (len(self.Gui.window.winfo_children()) > 0):      
            for i in self.Gui.window.winfo_children():
                if (i != self.Gui.Menu):
                    i.destroy()
            
            self.Gui.window.children.clear()
            
            self.Gui.Presets.ResetIndex()
            self.Gui.DefaultList()
            self.SelectedPreset = self.Presets.Default
        
        
    
    def AnimeAddPreset(self):

        if (self.SelectedPreset != self.Presets.AnimeAddInfo):
            self.DeletePreset()
            Preset:Enum = self.Presets.AnimeAddInfo

            self.Gui.Presets.AnimeAddInfo.AddAnime()

            self.Gui.Presets.AnimeAddInfo.SetMyAnimeListLink()

            self.Gui.Presets.AnimeAddInfo.SetWatchLink()

            self.Gui.Presets.AnimeAddInfo.AddToCalendar()

            self.Gui.Presets.CustomPresets.ReturnToMenu()

            self.SelectedPreset = Preset
        else:
            print(f"Already in AnimeAddInfo")
        

    def AnimeEditPreset(self):

        if (self.SelectedPreset != self.Presets.AnimeEditInfo):    
            self.DeletePreset()
            Preset:Enum = self.Presets.AnimeEditInfo

            self.Gui.Presets.AnimeEditInfo.UpdateEpisode()

            self.Gui.Presets.AnimeEditInfo.DeleteAnime()

            self.Gui.Presets.AnimeEditInfo.EditAnimeInfo()

            self.Gui.Presets.AnimeEditInfo.RemoveLeastAdded()

            self.Gui.Presets.CustomPresets.ReturnToMenu()

            self.SelectedPreset = Preset
        else:
            print("Already in AnimeEditPreset")
    
    def AnimeOpenPreset(self):

        if (self.SelectedPreset != self.Presets.AnimeOpenLinks):
            self.DeletePreset()
            Preset:Enum = self.Presets.AnimeOpenLinks

            self.Gui.Presets.AnimeOpenLinks.OpenMyAnimeListHomePage()

            self.Gui.Presets.AnimeOpenLinks.OpenSeasonLink()

            self.Gui.Presets.AnimeOpenLinks.OpenMyAnimeListLink()

            self.Gui.Presets.AnimeOpenLinks.OpenWatchLink()

            self.Gui.Presets.CustomPresets.ReturnToMenu()

            self.SelectedPreset = Preset
        else:
            print(f"Already in AnimeOpenPreset")
    
    def AnimeViewPreset(self):

        if (self.SelectedPreset != self.Presets.AnimeViewInfo):
            self.DeletePreset()
            self.InitDisplay()
            Preset:Enum = self.Presets.AnimeViewInfo

            self.Gui.Presets.CustomPresets.Filter()

            self.Gui.Presets.AnimeViewInfo.PrintInfo()

            self.Gui.Presets.AnimeViewInfo.PrintStatusList()

            self.Gui.Presets.AnimeViewInfo.PrintSeason()

            self.Gui.Presets.AnimeViewInfo.PrintSerie()

            self.Gui.Presets.AnimeViewInfo.PrintAnimeList()

            self.Gui.Presets.AnimeViewInfo.PrintSerieList()

            self.Gui.Presets.AnimeViewInfo.PrintCalendar()

            self.Gui.Presets.AnimeViewInfo.ViewAllAnimes()

            self.Gui.Presets.CustomPresets.ReturnToMenu()            

            self.SelectedPreset = Preset
        else:
            print(f"Already in AnimeViewPreset")
    
    def MangaAddPreset(self):

        if (self.SelectedPreset != self.Presets.MangaAddInfo):
            self.DeletePreset()
            Preset:Enum = self.Presets.MangaAddInfo

            self.Gui.Presets.MangaAddInfo.AddNewManga()

            self.Gui.Presets.MangaAddInfo.SetLink()

            self.Gui.Presets.MangaAddInfo.SetMyAnimeListLink()

            self.Gui.Presets.CustomPresets.ReturnToMenu()

            self.SelectedPreset = Preset
        else:
            print("Already in MangaAddInfo")
    
    def MangaEditPreset(self):

        if (self.SelectedPreset != self.Presets.MangaEditInfo):
            self.DeletePreset()
            Preset:Enum = self.Presets.MangaEditInfo

            self.Gui.Presets.MangaEditInfo.EditChapters()

            self.Gui.Presets.MangaEditInfo.RemoveManga()

            self.Gui.Presets.MangaEditInfo.EditInfo()

            self.Gui.Presets.MangaEditInfo.EditFavorites()

            self.Gui.Presets.CustomPresets.ReturnToMenu()

            self.SelectedPreset = Preset
        else:
            print("Already in MangaEditInfo")
        

    def MangaOpenPreset(self):

        if (self.SelectedPreset != self.Presets.MangaOpenLinks):
            self.DeletePreset()
            Preset:Enum = self.Presets.MangaOpenLinks

            self.Gui.Presets.MangaOpenLinks.OpenLink()

            self.Gui.Presets.MangaOpenLinks.OpenMyAnimeListLink()

            self.Gui.Presets.CustomPresets.ReturnToMenu()

            self.SelectedPreset = Preset
        else:
            print("Already in MangaOpenLinks")
    
    def MangaViewPreset(self):

        if (self.SelectedPreset != self.Presets.MangaViewInfo):
            self.DeletePreset()
            self.InitDisplay()
            Preset:Enum = self.Presets.MangaViewInfo

            self.Gui.Presets.MangaViewInfo.PrintInfo()

            self.Gui.Presets.MangaViewInfo.PrintCurrentStatus()

            self.Gui.Presets.MangaViewInfo.PrintFavorites()

            self.Gui.Presets.CustomPresets.ReturnToMenu()

            self.Gui.Presets.MangaViewInfo.ViewAllManga()

            self.SelectedPreset = Preset
        else:
            print("Already in MangaViewInfo")
    
    def MenuPreset(self):

        if (self.SelectedPreset != self.Presets.Menu):
            self.DeletePreset()
            self.Gui.Presets.ViewList.ViewIndex = 0
            self.Gui.Presets.ViewList.CurrentPage = 0
            Preset:Enum = self.Presets.Menu

            self.Gui.Presets.MenuPreset.Geral()

            self.SelectedPreset = Preset
        else:
            print("Already in Menu")
    
    class Presets(Enum):
        Default = -1
        Menu = 0 
        AnimeAddInfo = 1
        AnimeEditInfo = 2
        AnimeOpenLinks = 3
        AnimeViewInfo = 4
        MangaAddInfo = 5
        MangaEditInfo = 6
        MangaOpenLinks = 7
        MangaViewInfo = 8