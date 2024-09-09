import os
import sys
import tkinter as tk
sys.path.append(os.getcwd())
from tktooltip.tooltip import ToolTip
from enum import Enum
from WatchaScript import WatchaExecute
from MangaScript import MangaExecute
from GUI_Index import * 
import json




class SalameGUI:
    
    def __init__(self):
        
        
       
        self.ButList:list[tk.Button] = []
        self.TextList:list[tk.Label] = []
        self.EntryList:list[tk.Entry] = []
        self.ToolTipList:list[ToolTip] = []
        self.janela = tk.Tk()
        self.WatchaExec = WatchaExecute()
        self.WatchaExec.GuiInit(self)
        self.MangaExec = MangaExecute()
        self.MangaExec.GuiInit(self)

        

        self.Models = self.JanelaModels()
        self.Models.GuiInit(self)

        self.Menu = tk.Menu(self.janela)
        self.Button = self.ButtonManager()
        self.Button.GuiInit(self)
        self.Entry = self.EntryManager()
        self.Entry.GuiInit(self)
        self.Texto = self.TextManager()
        self.Texto.GuiInit(self)
        self.Presets = self.PresetsManager()
        self.Presets.GuiInit(self)
        
        SalameMenu:tk.Menu = tk.Menu(self.Menu, tearoff=0)
        AnimeMenu:tk.Menu = tk.Menu(self.Menu, tearoff=0)
        MangaMenu:tk.Menu = tk.Menu(self.Menu, tearoff=0)


        self.Menu.add_cascade(label='Anime', menu=AnimeMenu)
        self.Menu.add_cascade(label='Manga', menu=MangaMenu)


        AnimeMenu.add_command(label='AnimeSet', command=self.Models.AnimeSet)
        AnimeMenu.add_command(label='AnimeGet', command=self.Models.AnimeGet)

        MangaMenu.add_command(label='MangaSet', command=self.Models.MangaSet)
        MangaMenu.add_command(label='MangaGet', command=self.Models.MangaGet)

        SalameMenu.add_command(label='SwitchBackgrounColor', command=self.Models.SwitchModels)
        SalameMenu.add_command(label='PrintAllTk', command=self.AllTk)
        
        
        
        self.Menu.add_cascade(label='Salame', menu=SalameMenu)
        self.Menu.add_command(label='Reset', command=self.DeleteAll)
        self.Menu.add_command(label='Quit w', command=self.janela.destroy)

        
        
        
        self.janela.config(menu=self.Menu)
        self.janela.mainloop()


    #Funções
    
    def DefaultList(self):
        self.ButList.clear()
        self.TextList.clear()
        self.EntryList.clear()
        self.ToolTipList.clear()

    def AllTk(self):
        
        print(self.janela.winfo_children())

        
    def DeleteAll(self):   
        if (len(self.janela.winfo_children()) > 0):  
            for i in self.janela.winfo_children():
                if (i != self.Menu):
                    i.destroy()

            self.janela.children.clear()
            
            
            
            
            self.Presets.ResetIndex()
            self.DefaultList()
            self.Models.SelectedPreset = self.Models.Presets.Default

    def ClearEntry(self, EntryIndex:int):
        if (len(self.EntryList) > 0):
            self.EntryList[EntryIndex].delete(0, 'end')
    

    #Classes

    class TextManager:

        def GuiInit(self, SetGUI):
            self.Gui:SalameGUI = SetGUI         
            self.janela = self.Gui.janela
            self.GetList:list = [tk.Text(self.janela), tk.Scrollbar(self.janela)]

        def PresetTextPosition(self, Text:tk.Label, PositionX:int, PositionTag:int, DefaultPos:int = 0):
            CutYPos:int = ((PositionTag - 1) * 50)
            if (PositionTag == 1):
                Text.place(x=PositionX, y=DefaultPos)
                self.TextSpaceY = DefaultPos
            else:
                Text.place(x=PositionX, y=DefaultPos + self.TextSpaceY + CutYPos)

        def ResetText(self):
            if (len(self.Gui.EntryList) > 0):        
                for i in range(len(self.Gui.EntryList)):
                    self.Gui.EntryList[i].delete(0, 'end')
        
        def UpdateDisplay(self):
            self.Display:tk.Text = self.GetList[0]
            self.DisplayScrollbar:tk.Scrollbar = self.GetList[1]
            
        def PrintDisplay(self, Info:dict | list | str):
            self.UpdateDisplay()
            self.Display.place(x=550, y=150)
            self.Display.config(width=50, height=20, font=('Arial', 15), bg="gray")

            self.DisplayScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.Display.config(yscrollcommand=self.DisplayScrollbar.set)
            self.DisplayScrollbar.config(command=self.Display.yview)

            self.Display.delete(1.0, tk.END)
            self.Display.config(cursor="arrow", takefocus=True)
            self.Display.insert(tk.END, json.dumps(Info, indent=4))



        
        def CreateText(self, Text:str, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):
           
            TextToCreate:tk.Label = tk.Label(self.janela)
            TextToCreate.configure(text=Text, font=('Arial', 13))
            TextToCreate.config(width=8, height=2, bg= "lightgray", border=1, relief="groove")
            if (CustomYPosition > 0):
                TextToCreate.place(x=PositionX, y=CustomYPosition)
            else:
                self.PresetTextPosition(TextToCreate, PositionX, PositionTag, DefaultPos)
            if (self.Gui.TextList.count(TextToCreate) == 0):
                self.Gui.TextList.append(TextToCreate)


    class EntryManager():

        def GuiInit(self, SetGUI):
            self.Gui:SalameGUI = SetGUI
            self.janela = self.Gui.janela
        
        def PresetEntryPosition(self, Entry:tk.Entry, PositionX:int, PositionTag:int, DefaultPos:int = 0):           
            CutYPos:int = ((PositionTag - 1) * 50)
            if (PositionTag == 1):
                Entry.place(x=PositionX, y=DefaultPos)
                self.EntrySpaceY = DefaultPos
            else:
                Entry.place(x=PositionX, y=DefaultPos + self.EntrySpaceY + CutYPos)

        def CreateEntry(self, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):

            EntryToCreate:tk.Entry = tk.Entry(self.janela)
            EntryToCreate.update_idletasks()
            EntryToCreate.configure(font=('Arial', 14))
            EntryToCreate.config(width=6, border=1, relief="groove")
            if (CustomYPosition > 0):
                EntryToCreate.place(x=PositionX, y=CustomYPosition)
            else:
                self.PresetEntryPosition(EntryToCreate, PositionX, PositionTag, DefaultPos)
            if (self.Gui.EntryList.count(EntryToCreate) == 0):
                self.Gui.EntryList.append(EntryToCreate)



    class ButtonManager():

        def GuiInit(self, SetGUI):
            self.Gui:SalameGUI = SetGUI
            self.janela = self.Gui.janela
        
        def PresetButPosition(self,But:tk.Button, PositionX:int, PositionTag:int, DefaultPos:int = 0):
            CutYPos:int = ((PositionTag - 1) * 50)
            if (PositionTag == 1):
                But.place(x=PositionX, y=DefaultPos)
                self.ButSpaceY = DefaultPos
            else:
                But.place(x=PositionX, y=DefaultPos + self.ButSpaceY + CutYPos)

        def CreateBut(self, Name:str, Function, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):

            ButToCreate:tk.Button = tk.Button(self.janela)
            ButToCreate.configure(text=Name, font=('Arial', 14), command=Function)
            ButToCreate.config(width=10, height=2, bg= "red", border=1, relief="groove")
            if (CustomYPosition > 0):
                ButToCreate.place(x=PositionX, y=CustomYPosition)
            else:
                self.PresetButPosition(ButToCreate, PositionX, PositionTag, DefaultPos)
            if (self.Gui.ButList.count(ButToCreate) == 0):
                self.Gui.ButList.append(ButToCreate)

    class PresetsManager:

        def __init__(self):
            self.EntryIndex = 0
            self.TextIndex = 0
            self.ButtonIndex = 0
            

        def GuiInit(self, SetGUI):
            self.AnimeSet = self.AnimePresetSet(SetGUI)
            self.AnimeGet = self.AnimePresetGet(SetGUI)
            self.MangaSet = self.MangaPresetSet(SetGUI)
            self.MangaGet = self.MangaPresetGet(SetGUI)
            self.Gui:SalameGUI = SetGUI
        
        def CreateTooltip(self, widget, text, delay = 0.1):
            tooltip = ToolTip(widget, text, delay)
            
            self.Gui.ToolTipList.append(tooltip)

        def ResetIndex(self):
            self.EntryIndex = 0
            self.TextIndex = 0
            self.ButtonIndex = 0
        
        def UpdateEntryIndex(self):
            Index = self.EntryIndex
            self.EntryIndex += 1
            return Index
         
        def UpdateTextIndex(self):
            Index = self.TextIndex
            self.TextIndex += 1
            return Index

        def UpdateButtonIndex(self):
            Index = self.ButtonIndex
            self.ButtonIndex += 1
            return Index
            

        class AnimePresetSet:
            def __init__(self, SetGUI):
                self.Gui:SalameGUI = SetGUI
                self.ButtonIndex = AnimeSet.ButtonIndex()
                self.EntryIndex = AnimeSet.EntryIndex()
                self.TextIndex = AnimeSet.TextIndex()
                     

            def AddAnime(self):

                #AddAnime
                self.Gui.Button.CreateBut('AddAnime', self.Gui.WatchaExec.Add , 350, 1 , 123)
                self.ButtonIndex.AddAnime = self.Gui.Presets.UpdateButtonIndex()
                
                #Name
                self.Gui.Entry.CreateEntry(200, 1, 39)
                self.EntryIndex.AddAnime.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddAnime.Name].config(width=25)               
                #MaxEp
                self.Gui.Entry.CreateEntry(200, 2)
                self.EntryIndex.AddAnime.MaxEp = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddAnime.MaxEp].config(width=2)
                #Status
                self.Gui.Entry.CreateEntry(200, 3)
                self.EntryIndex.AddAnime.Status = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddAnime.Status].config(width=11)
                #Season
                self.Gui.Entry.CreateEntry(200, 4)
                self.EntryIndex.AddAnime.Season = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddAnime.Season].config(width=12)
                #Serie
                self.Gui.Entry.CreateEntry(200, 5)
                self.EntryIndex.AddAnime.Serie = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddAnime.Serie].config(width=15)

                #Name
                self.Gui.Texto.CreateText("Name", 100, 1, 30)
                self.TextIndex.AddAnime.Name = self.Gui.Presets.UpdateTextIndex()
                #MaxEp
                self.Gui.Texto.CreateText("MaxEp", 100, 2)
                self.TextIndex.AddAnime.MaxEp = self.Gui.Presets.UpdateTextIndex()
                #Status
                self.Gui.Texto.CreateText("Status", 100, 3)
                self.TextIndex.AddAnime.Status = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddAnime.Status], "Can be Watching, Completed, Dropped, or PlanToWatch.")
                #Season
                self.Gui.Texto.CreateText("Season", 100, 4)
                self.TextIndex.AddAnime.Season = self.Gui.Presets.UpdateTextIndex()
                #Serie
                self.Gui.Texto.CreateText("Serie", 100, 5)
                self.TextIndex.AddAnime.Serie = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddAnime.Serie], "Is optional.")


            def DeleteAnime(self):
                self.Gui.Button.CreateBut('DeleteAnime', self.Gui.WatchaExec.RemoveAnime , 1100, 1 , 670)
                self.ButtonIndex.DeleteAnime = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("Name", 1100, 1, 612)
                self.TextIndex.DeleteAnime.Name = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Entry.CreateEntry(1200, 1, 620)
                self.EntryIndex.DeleteAnime.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.DeleteAnime.Name].config(width=25)


            def AddEpisode(self):
                self.Gui.Button.CreateBut('AddEp', self.Gui.WatchaExec.AddEppisode , 1180, 1 , 150)
                self.ButtonIndex.AddEpisode = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Button.CreateBut('SetEp', self.Gui.WatchaExec.SetEpisode , 1315, 1 , 150)
                self.ButtonIndex.SetEpisode = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("AddEpisode", 1250, 1, 25)
                self.TextIndex.AddEpisode.Title = self.Gui.Presets.UpdateTextIndex()
                self.Gui.TextList[self.TextIndex.AddEpisode.Title].config(width=12, height= 3, font=('Arial', 13))

                self.Gui.Texto.CreateText("Name", 1072, 1, 102)
                self.TextIndex.AddEpisode.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddEpisode.Name], "Can be simplified.")
                self.Gui.Entry.CreateEntry(1168, 1, 110)
                self.EntryIndex.AddEpisode.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddEpisode.Name].config(width=25)     
                
                self.Gui.Entry.CreateEntry(1355, 1, 226)
                self.EntryIndex.AddEpisode.Ep = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddEpisode.Ep].config(width=2)


            def UpdateScore(self):
                self.Gui.Button.CreateBut('UpdateScore', self.Gui.WatchaExec.UpdateScore , 1230, 1 , 360)
                self.ButtonIndex.UpdateScore = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("Name", 1062, 1, 318)
                self.TextIndex.UpdateScore.Name = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Entry.CreateEntry(1155, 1, 326)
                self.EntryIndex.UpdateScore.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.UpdateScore.Name].config(width=25)
                
                self.Gui.Entry.CreateEntry(1455, 1, 326)
                self.EntryIndex.UpdateScore.Score = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.UpdateScore.Score].config(width=3)


            def RemoveLeastAdded(self):
                self.Gui.Button.CreateBut('RemoveLeastAdded', self.Gui.WatchaExec.RemoveLeastAdded , 1300, 1 , 670)
                self.ButtonIndex.RemoveLeastAdded = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.RemoveLeastAdded].config(width=17)


            def SetCurrentStatus(self):        
                self.Gui.Button.CreateBut('SetCurrentStatus', self.Gui.WatchaExec.OverrideCurrentStatus, 1340, 1 , 500)
                self.ButtonIndex.SetCurrentStatus = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.SetCurrentStatus].config(width=14)
                
                self.Gui.Texto.CreateText("Name", 1080, 1, 450)
                self.TextIndex.SetCurrentStatus.Name = self.Gui.Presets.UpdateTextIndex()             
                self.Gui.Entry.CreateEntry(1180, 1, 460)
                self.EntryIndex.SetCurrentStatus.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetCurrentStatus.Name].config(width=25)
                
                self.Gui.Texto.CreateText("SetStatus", 1080, 2)
                self.TextIndex.SetCurrentStatus.SetStatus = self.Gui.Presets.UpdateTextIndex()
                self.Gui.TextList[self.TextIndex.SetCurrentStatus.SetStatus].config(width=10)
                self.Gui.Entry.CreateEntry(1180, 2)
                self.EntryIndex.SetCurrentStatus.Status = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetCurrentStatus.Status].config(width=11)

                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.SetCurrentStatus.SetStatus], "Can be Watching, Completed, Dropped, or PlanToWatch.")
                
                
            def SetMyAnimeListLink(self):
                self.Gui.Button.CreateBut('SetMyAnimeListLink', self.Gui.WatchaExec.AddMyAnimeListLink, 250, 1 , 420)
                self.ButtonIndex.SetMyAnimeListLink = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.SetMyAnimeListLink].config(width=16)

                self.Gui.Texto.CreateText("Name", 100, 1, 320)
                self.TextIndex.MyAnimeListLink.Name = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Entry.CreateEntry(200, 1, 330)
                self.EntryIndex.MyAnimeListLink.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.MyAnimeListLink.Name].config(width=25)

                self.Gui.Texto.CreateText("MyAnimeListLink", 40, 2)
                self.TextIndex.MyAnimeListLink.Link = self.Gui.Presets.UpdateTextIndex()
                self.Gui.TextList[self.TextIndex.MyAnimeListLink.Link].config(width=16, font=('Arial', 13))

                self.Gui.Entry.CreateEntry(200, 2)
                self.EntryIndex.MyAnimeListLink.Link = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.MyAnimeListLink.Link].config(width=25)
            

            def AddToCalendar(self):
                self.Gui.Button.CreateBut('AddToCalendar', self.Gui.WatchaExec.AddToCalendar, 700, 1 , 660)
                self.ButtonIndex.AddToCallendar = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.AddToCallendar].config(width=13)

                self.Gui.Texto.CreateText("Name", 600, 1, 550)
                self.TextIndex.AddToCallendar.Name = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Entry.CreateEntry(700, 1, 559)
                self.EntryIndex.AddToCallendar.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddToCallendar.Name].config(width=25)

                self.Gui.Texto.CreateText("Day", 600, 2)
                self.TextIndex.AddToCallendar.Day = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddToCallendar.Day], "Can be one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.")

                self.Gui.Entry.CreateEntry(700, 2)
                self.EntryIndex.AddToCallendar.Day = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddToCallendar.Day].config(width=10)


            def SetSeasonLink(self):
                self.Gui.Button.CreateBut('SetSeasonLink', self.Gui.WatchaExec.SetSeasonLink, 200, 1 , 610)
                self.ButtonIndex.SetSeasonLink = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.SetSeasonLink].config(width=13)

                self.Gui.Texto.CreateText("SeasonID", 100, 1, 510)
                self.TextIndex.SetSeasonLink.SeasonID = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Entry.CreateEntry(200, 1, 519)
                self.EntryIndex.SetSeasonLink.SeasonID = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetSeasonLink.SeasonID].config(width=12)

                self.Gui.Texto.CreateText("Link", 100, 2)
                self.TextIndex.SetSeasonLink.SeasonID = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Entry.CreateEntry(200, 2)
                self.EntryIndex.SetSeasonLink.Link = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetSeasonLink.Link].config(width=25)
        
        class AnimePresetGet:
            def __init__(self, SetGUI):
                self.Gui:SalameGUI = SetGUI
                self.ButtonIndex = AnimeGet.ButtonIndex()
                self.EntryIndex = AnimeGet.EntryIndex()
                self.TextIndex = AnimeGet.TextIndex()
            
            def GetStatus(self):
                self.Gui.Button.CreateBut('GetStatus', self.Gui.WatchaExec.GetAnimeStatus , 230, 1 , 80)
                self.ButtonIndex.GetStatus = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.GetStatus].config(width=12)
                self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.ButtonIndex.GetStatus], "Print the data of the selected anime.")
                
                self.Gui.Texto.CreateText("Name", 80, 1, 30)
                self.TextIndex.GetStatus.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.GetStatus.Name], "Can be simplified.")

                self.Gui.Entry.CreateEntry(170, 1, 39)
                self.EntryIndex.GetStatus.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.GetStatus.Name].config(width=25)


            def PrintSeason(self):
                self.Gui.Button.CreateBut('PrintSeason', self.Gui.WatchaExec.PrintSeason , 170, 1 , 200)
                self.ButtonIndex.PrintSeason = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.PrintSeason].config(width=12)

                self.Gui.Texto.CreateText("SeasonID", 80, 1, 150)
                self.TextIndex.PrintSeason.SeasonID = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintSeason.SeasonID], "File name containing season data.")

                self.Gui.Entry.CreateEntry(170, 1, 159)
                self.EntryIndex.PrintSeason.SeasonID = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.PrintSeason.SeasonID].config(width=12)


            def PrintStatusList(self):    
                self.Gui.Button.CreateBut('PrintStatusList', self.Gui.WatchaExec.PrintStatusList , 170, 1 , 320)
                self.ButtonIndex.PrintStatusList = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.PrintStatusList].config(width=14)
                self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.ButtonIndex.PrintStatusList], "If StatusID is empty, all statuses will be printed.")

                self.Gui.Texto.CreateText("StatusID", 80, 1, 270)
                self.TextIndex.PrintStatusList.StatusID = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintStatusList.StatusID], "Can be Watching, Completed, Dropped, or PlanToWatch.")
                self.Gui.Entry.CreateEntry(170, 1, 279)
                self.EntryIndex.PrintStatusList.StatusID = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.PrintStatusList.StatusID].config(width=11)


            def OpenLink(self):
                self.Gui.Button.CreateBut('OpenLink', self.Gui.WatchaExec.OpenLink , 170, 1 , 560)
                self.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("Name", 80, 1, 510)
                self.TextIndex.OpenLink.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(170, 1, 519)
                self.EntryIndex.OpenLink.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.OpenLink.Name].config(width=25)


            def PrintSerie(self):
                self.Gui.Button.CreateBut('PrintSerie', self.Gui.WatchaExec.PrintSerie , 170, 1 , 440)
                self.ButtonIndex.PrintSerie = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("Name", 80, 1, 390)
                self.TextIndex.PrintSerie.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(170, 1, 399)
                self.EntryIndex.PrintSerie.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.PrintSerie.Name].config(width=15)


            def PrintAnimeList(self):
                self.Gui.Button.CreateBut('PrintAnimeList', self.Gui.WatchaExec.PrintAnimeList , 1200, 1 , 200)
                self.ButtonIndex.PrintAnimeList = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.PrintAnimeList].config(width=14)
                

            def PrintSerieList(self):
                self.Gui.Button.CreateBut('PrintSerieList', self.Gui.WatchaExec.PrintSerieList , 1200, 1 , 350)
                self.ButtonIndex.PrintSerieList = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.PrintSerieList].config(width=14)


            def OpenMyAnimeList(self):
                self.Gui.Button.CreateBut('OpenMyAnimeList', self.Gui.WatchaExec.OpenMyAnimeList , 700, 1 , 20)
                self.ButtonIndex.OpenMyAnimeList = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.OpenMyAnimeList].config(width=16)


            def PrintCalendar(self):
                self.Gui.Button.CreateBut('PrintCalendar', self.Gui.WatchaExec.PrintSeasonCalendar, 700, 1 , 680)
                self.ButtonIndex.PrintCallendar = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.PrintCallendar].config(width=13)
                self.Gui.Presets.CreateTooltip(self.Gui.ButList[self.ButtonIndex.PrintCallendar], "Show season calendar")

                self.Gui.Texto.CreateText("SeasonID", 600, 1, 630)
                self.TextIndex.PrintCallendar.SeasonID = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.PrintCallendar.SeasonID], "File name containing season data")

                self.Gui.Entry.CreateEntry(700, 1, 639)
                self.EntryIndex.PrintCallendar.SeasonID = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.PrintCallendar.SeasonID].config(width=12)
            

            def OpenSeasonLink(self):
                self.Gui.Button.CreateBut('OpenSeasonLink', self.Gui.WatchaExec.OpenSeasonLink , 170, 1 , 680)
                self.ButtonIndex.OpenSeasonLink = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.OpenSeasonLink].config(width=16)

                self.Gui.Texto.CreateText("SeasonID", 80, 1, 630)
                self.TextIndex.OpenSeasonLink.SeasonID = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(170, 1, 639)
                self.EntryIndex.OpenSeasonLink.SeasonID = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.OpenSeasonLink.SeasonID].config(width=12)

        class MangaPresetSet:
            def __init__(self, SetGUI):
                self.Gui:SalameGUI = SetGUI
                self.ButtonIndex = MangaSet.ButtonIndex()
                self.EntryIndex = MangaSet.EntryIndex()
                self.TextIndex = MangaSet.TextIndex()


            def AddNewManga(self):
                self.Gui.Button.CreateBut('AddNewManga', self.Gui.MangaExec.AddNewManga , 350, 1 , 110)
                self.ButtonIndex.AddNewManga = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.AddNewManga].config(width=12)

                self.Gui.Texto.CreateText("Name", 100, 1, 30)
                self.TextIndex.AddNewManga.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(200, 1, 37)
                self.EntryIndex.AddNewManga.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddNewManga.Name].config(width=25)

                self.Gui.Texto.CreateText("Chapters", 100, 2)
                self.TextIndex.AddNewManga.Chapters = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(200, 2)
                self.EntryIndex.AddNewManga.Chapters = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddNewManga.Chapters].config(width=4)

                self.Gui.Texto.CreateText("Status", 100, 3)
                self.TextIndex.AddNewManga.Status = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.AddNewManga.Status], "Can be Reading, PlanToRea, Completed or Dropped.")
                self.Gui.Entry.CreateEntry(200, 3)
                self.EntryIndex.AddNewManga.Status = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.AddNewManga.Status].config(width=10)
            

            def RemoveManga(self):
                self.Gui.Button.CreateBut('RemoveManga', self.Gui.MangaExec.DeleteManga , 1290, 1 , 634)
                self.ButtonIndex.DeleteManga = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.DeleteManga].config(width=12)

                self.Gui.Texto.CreateText("Name", 1080, 1, 580)
                self.TextIndex.DeleteManga.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(1180, 1, 589)
                self.EntryIndex.DeleteManga.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.DeleteManga.Name].config(width=25)
            

            def SetLink(self):
                self.Gui.Button.CreateBut('SetLink', self.Gui.MangaExec.SetLink , 325, 1 , 324)
                self.ButtonIndex.SetLink = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.SetLink].config(width=12)

                self.Gui.Texto.CreateText("Name", 100, 1, 220)
                self.TextIndex.SetLink.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(200, 1, 229)
                self.EntryIndex.SetLink.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetLink.Name].config(width=25)

                self.Gui.Texto.CreateText("Link", 100, 2)
                self.TextIndex.SetLink.Link = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(200, 2)
                self.EntryIndex.SetLink.Link = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetLink.Link].config(width=25)


            def EditFavorites(self):
                self.Gui.Button.CreateBut('AddFavorite', self.Gui.MangaExec.AddFavorite , 120, 1 , 470)
                self.ButtonIndex.AddFavorite = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.AddFavorite].config(width=12)

                self.Gui.Button.CreateBut('RemoveFavorite', self.Gui.MangaExec.DeleteFavorite , 320, 1 , 470)
                self.ButtonIndex.DeleteFavorite = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.DeleteFavorite].config(width=14)

                self.Gui.Texto.CreateText("Name", 100, 1, 420)
                self.TextIndex.EditFavorites.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(200, 1, 429)
                self.EntryIndex.EditFavorites.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.EditFavorites.Name].config(width=25)
            

            def EditChapters(self):
                self.Gui.Button.CreateBut('AddChapters', self.Gui.MangaExec.AddChapters , 1180, 1 , 150)
                self.ButtonIndex.AddChapters = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Button.CreateBut('SetChapters', self.Gui.MangaExec.SetChapters , 1315, 1 , 150)
                self.ButtonIndex.SetChapters = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("EditChapters", 1250, 1, 25)
                self.TextIndex.UpdateChapters.Title = self.Gui.Presets.UpdateTextIndex()
                self.Gui.TextList[self.TextIndex.UpdateChapters.Title].config(width=12, height= 3, font=('Arial', 13))

                self.Gui.Texto.CreateText("Name", 1072, 1, 102)
                self.TextIndex.UpdateChapters.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.TextIndex.UpdateChapters.Name], "Can be simplified.")
                self.Gui.Entry.CreateEntry(1168, 1, 110)
                self.EntryIndex.UpdateChapters.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.UpdateChapters.Name].config(width=25)     
                
                self.Gui.Entry.CreateEntry(1355, 1, 226)
                self.EntryIndex.UpdateChapters.Chapters = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.UpdateChapters.Chapters].config(width=4)
        

            def SetStatus(self):
                self.Gui.Button.CreateBut('SetStatus', self.Gui.MangaExec.SetStatus , 1290, 1 , 500)
                self.ButtonIndex.SetStatus = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.SetStatus].config(width=12)

                self.Gui.Texto.CreateText("Name", 1080, 1, 450)
                self.TextIndex.SetStatus.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(1180, 1, 460)
                self.EntryIndex.SetStatus.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetStatus.Name].config(width=25)

                self.Gui.Texto.CreateText("Status", 1080, 2)
                self.TextIndex.SetStatus.Status = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(1180, 2)
                self.EntryIndex.SetStatus.Status = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.SetStatus.Status].config(width=8)
            

            def EditScore(self):
                self.Gui.Button.CreateBut('UpdateScore', self.Gui.MangaExec.EditScore , 1290, 1 , 350)
                self.ButtonIndex.EditScore = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("Name", 1080, 1, 300)
                self.TextIndex.EditScore.Name = self.Gui.Presets.UpdateTextIndex()

                self.Gui.Entry.CreateEntry(1180, 1, 310)
                self.EntryIndex.EditScore.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.EditScore.Name].config(width=25)
                
                self.Gui.Entry.CreateEntry(1480, 1, 310)
                self.EntryIndex.EditScore.Score = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.EditScore.Score].config(width=3)

        class MangaPresetGet:
            def __init__(self, SetGUI):
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
                self.Gui.EntryList[self.EntryIndex.PrintCurrentStatus.Status].config(width=8)
            
            def OpenLink(self):
                self.Gui.Button.CreateBut('OpenLink', self.Gui.MangaExec.OpenLink , 230, 1 , 320)
                self.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()

                self.Gui.Texto.CreateText("Name", 80, 1, 270)
                self.TextIndex.OpenLink.Name = self.Gui.Presets.UpdateTextIndex()
                self.Gui.Entry.CreateEntry(180, 1, 280)
                self.EntryIndex.OpenLink.Name = self.Gui.Presets.UpdateEntryIndex()
                self.Gui.EntryList[self.EntryIndex.OpenLink.Name].config(width=25)
            
            def PrinFavorites(self):
                self.Gui.Button.CreateBut('PrintFavorites', self.Gui.MangaExec.PrintFavorites , 1200, 1, 90)
                self.ButtonIndex.PrintFavorites = self.Gui.Presets.UpdateButtonIndex()
                self.Gui.ButList[self.ButtonIndex.PrintFavorites].config(width=15)
            


    class JanelaModels:
        def __init__(self):      
            self.PerfilList:list[Enum] = [self.Presets.Default, self.Presets.AnimeSet, self.Presets.AnimeGet]
            self.SelectedPreset:Enum = self.Presets.Default
        
        def GuiInit(self, SetGUI):
            self.Gui:SalameGUI = SetGUI
            self.Gui.janela.configure(bg='#000000')
            self.Gui.janela.title('Janela Edit')
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
            self.Gui.Texto.GetList = [tk.Text(self.Gui.janela), tk.Scrollbar(self.Gui.janela)]

        
        
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

                self.SelectedPreset = self.Presets.MangaGet
            else:
                print("Already in MangaGet")
                
        
        class Presets(Enum):
            Default = 0
            AnimeSet = 1
            AnimeGet = 2
            MangaSet = 3
            MangaGet = 4
        

#ExternalClasses
def InicializeGUI():
    return SalameGUI()

    