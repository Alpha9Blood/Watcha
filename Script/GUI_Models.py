
from enum import Enum
import tkinter as tk
class GUI_Models:
    def __init__(self):      
        self.PerfilList:list[Enum] = [self.Presets.Default, self.Presets.AnimeSet, self.Presets.AnimeGet]
        self.SelectedPreset:Enum = self.Presets.Default
    
    def GuiInit(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI
        self.Gui.janela.configure(bg='#000000')
        self.Gui.janela.title('Watcha')
        self.Gui.janela.geometry('1600x800')

    def WhiteModel(self):
        self.Gui.janela.configure(bg='#FFFFFF')
        
    def BlackModel(self):
        self.Gui.janela.configure(bg='#000000')
    
    def SwitchModels(self):
        if self.Gui.janela.cget('bg') == '#000000':
            self.Switch = True
        if (self.Switch):
            self.WhiteModel()
            self.Switch = False
        else:
            self.BlackModel()
    
    def InitDisplay(self):
        self.Gui.Text.GetList = [tk.Text(self.Gui.janela), tk.Scrollbar(self.Gui.janela)]

    
    
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
        if (len(self.Gui.janela.winfo_children()) > 0):      
            for i in self.Gui.janela.winfo_children():
                if (i != self.Gui.Menu):
                    i.destroy()
            
            self.Gui.janela.children.clear()
            
            
            self.Gui.Presets.ResetIndex()
            self.Gui.DefaultList()
            self.SelectedPreset = self.Presets.Default
        
        
    
    def AnimeSet(self):
        """
        Sets up the AnimeSet GUI.

        This function creates and configures the necessary GUI elements for the AnimeSet preset.
        If the selected preset is not the AnimeSet, it deletes the existing preset and creates
        the AnimeSet preset.

        """
        

        if (self.SelectedPreset != self.Presets.AnimeSet):
            self.DeletePreset()

            self.Gui.Presets.AnimeSet.AddAnime()

            self.Gui.Presets.AnimeSet.DeleteAnime()

            self.Gui.Presets.AnimeSet.AddEpisode()

            self.Gui.Presets.AnimeSet.UpdateScore()

            self.Gui.Presets.AnimeSet.RemoveLeastAdded()

            self.Gui.Presets.AnimeSet.SetCurrentStatus()
            
            self.Gui.Presets.AnimeSet.SetMyAnimeListLink()

            self.Gui.Presets.AnimeSet.AddToCalendar()
            
            self.Gui.Presets.AnimeSet.SetSeasonLink()


            self.SelectedPreset = self.Presets.AnimeSet
        else:
            print("Already in AnimeSet")
        

    def AnimeGet(self):
        """
        Initializes the AnimeGet preset by deleting the current preset, 
        initializing the display, and creating various GUI elements for 
        anime-related operations such as getting status, printing seasons, 
        printing status lists, opening links, printing series, and printing 
        anime lists.

        """

        if (self.SelectedPreset != self.Presets.AnimeGet):    
            self.DeletePreset()
            self.InitDisplay()

            self.Gui.Presets.AnimeGet.Filter()

            self.Gui.Presets.AnimeGet.GetStatus()

            self.Gui.Presets.AnimeGet.PrintSeason()

            self.Gui.Presets.AnimeGet.PrintStatusList()

            self.Gui.Presets.AnimeGet.OpenLink()

            self.Gui.Presets.AnimeGet.PrintSerie()

            self.Gui.Presets.AnimeGet.PrintAnimeList()

            self.Gui.Presets.AnimeGet.PrintSerieList()

            self.Gui.Presets.AnimeGet.OpenMyAnimeList()

            self.Gui.Presets.AnimeGet.PrintCalendar()

            self.Gui.Presets.AnimeGet.OpenSeasonLink()


            self.SelectedPreset = self.Presets.AnimeGet
        else:
            print("Already in AnimeGet")
    
    def MangaSet(self):
        """
        Initializes the MangaSet preset by deleting the current preset, 
        initializing the display, and creating various GUI elements for 
        manga-related operations such as adding new manga, setting links, 
        removing manga, editing favorites, editing chapters, setting status, 
        and editing scores.

        """
        if (self.SelectedPreset != self.Presets.MangaSet):
            self.DeletePreset()

            self.Gui.Presets.MangaSet.AddNewManga()

            self.Gui.Presets.MangaSet.SetLink()

            self.Gui.Presets.MangaSet.RemoveManga()

            self.Gui.Presets.MangaSet.EditFavorites()

            self.Gui.Presets.MangaSet.EditChapters()

            self.Gui.Presets.MangaSet.SetStatus()

            self.Gui.Presets.MangaSet.EditScore()

            self.SelectedPreset = self.Presets.MangaSet
        else:
            print("Already in MangaSet")
    
    def MangaGet(self):
        """
        Initializes the MangaGet preset by deleting the current preset, 
        initializing the display, and creating various GUI elements for 
        manga-related operations such as printing manga, printing current status, 
        and opening links.

        """
    
        if (self.SelectedPreset != self.Presets.MangaGet):
            self.DeletePreset()
            self.InitDisplay()

            self.Gui.Presets.MangaGet.PrintManga()

            self.Gui.Presets.MangaGet.PrintCurrentStatus()

            self.Gui.Presets.MangaGet.OpenLink()

            self.Gui.Presets.MangaGet.PrintFavorites()

            self.SelectedPreset = self.Presets.MangaGet
        else:
            print("Already in MangaGet")
            
    
    class Presets(Enum):
        Default = 0
        AnimeSet = 1
        AnimeGet = 2
        MangaSet = 3
        MangaGet = 4