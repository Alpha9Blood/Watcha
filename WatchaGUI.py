import tkinter as tk
from AnimeScript import AnimeExecute
from MangaScript import MangaExecute
from TkToolTip.TkToolTip import ToolTip
from Script.GUI_Index import *
from Script.GUI_Models import GUI_Models
from Script.Managers.CustomTypes.CustomEntry import CustomEntry
from Script.Managers.CustomTypes.CustomButton import CustomButton
from Script.Managers.ListManager import AnimeListManager
from Script.Managers.EntryManager import EntryManager
from Script.Managers.TextManager import TextManager
from Script.Managers.ButtonManager import ButtonManager
from Script.Managers.PresetsManager import PresetsManager
from Script.Managers.ImageManager import ImageManager
from Script.ManageData.ImageExtractor import ImageControler



class WatchaGUI:
    
    def __init__(self):

        self.ButList:list[CustomButton] = []
        self.LabelList:list[tk.Label] = []
        self.EntryList:list[CustomEntry] = []
        self.ToolTipList:list[ToolTip] = []
        self.TextList:list[tk.Text] = []

        self.window = tk.Tk()
        
        self.ImageExtractor = ImageControler()

        self.AnimeExec = AnimeExecute()
        self.AnimeExec.GuiInit(self)
        self.MangaExec = MangaExecute()
        self.MangaExec.GuiInit(self)

        self.Models = GUI_Models()
        self.Models.GuiInit(self)
        
        
        self.Button = ButtonManager()
        self.Button.GuiInit(self)
        self.Entry = EntryManager()
        self.Entry.GuiInit(self)
        self.Text = TextManager()
        self.Text.GuiInit(self)
        self.ImageSlot = ImageManager()
        self.ImageSlot.GuiInit(self)
        

        

        
        self.AnimeDataLists = AnimeListManager()
        self.AnimeDataLists.GuiInit(self)

        self.Presets = PresetsManager()
        self.Presets.GuiInit(self)

        self.Menu = tk.Menu(self.window)

        SalameMenu:tk.Menu = tk.Menu(self.Menu, tearoff=0)

        SalameMenu.add_command(label='SwitchBackgrounColor', command=self.Models.SwitchModels)
        SalameMenu.add_command(label='PrintAllTk', command=self.AllTk)
        
        
        
        self.Menu.add_cascade(label='Salame', menu=SalameMenu)
        self.Menu.add_command(label='Reset', command=self.Models.MenuPreset)
        self.Menu.add_command(label='Quit w', command=self.window.destroy)
        
        
        self.window.config(menu=self.Menu)

        self.Models.MenuPreset()

        self.window.mainloop()


    #Func
    
    def DefaultList(self):
        self.ButList.clear()
        self.LabelList.clear()
        self.EntryList.clear()
        self.ToolTipList.clear()
        self.TextList.clear()
        self.Entry.EntryFilter.Reset()
        self.AnimeDataLists.ClearCustomLists()
        self.ImageSlot.InstacedPhotos.clear()
        

    def AllTk(self):
        print(self.window.winfo_children())

        
    def DeleteAll(self):
        if (len(self.window.winfo_children()) > 0):  
            for i in self.window.winfo_children():
                if (i != self.Menu):
                    i.destroy()

            self.window.children.clear()
            
                       
            self.Presets.ResetIndex()
            self.DefaultList()
            self.Models.SelectedPreset = self.Models.Presets.Default


def InicializeGUI():
    return WatchaGUI()  