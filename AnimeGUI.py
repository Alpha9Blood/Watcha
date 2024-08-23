import os
import sys
import tkinter as tk
sys.path.append(os.getcwd())
from tktooltip.tooltip import ToolTip
from enum import Enum
from WatchaScript import ExecuteFunctions
from GUI_Index import * 
import json




class SalameGUI:
    
    def __init__(self):
        
        
       
        self.ButList:list[tk.Button] = []
        self.TextList:list[tk.Label] = []
        self.EntryList:list[tk.Entry] = []
        self.janela = tk.Tk()
        self.ExecFunc = ExecuteFunctions(self)
        

        self.Models = self.JanelaModels(self)
        self.Models.__init__(self)

        self.Menu = tk.Menu(self.janela)
        self.Button = self.ButtonManager(self)
        self.Entry = self.EntryManager(self)
        self.Texto = self.TextManager(self)


        submenu = tk.Menu(self.Menu, tearoff=0)
        submenu.add_command(label='AnimeSet', command=self.Models.AnimeSet)
        submenu.add_command(label='AnimeGet', command=self.Models.AnimeGet)
        submenu.add_command(label='DeletePreset', command=self.Models.DeletePreset)
        submenu.add_command(label='SwitchBackgrounColor', command=self.Models.SwitchModels)
        self.Menu.add_cascade(label='Salame', menu=submenu)

        self.Menu.add_command(label='Reset', command=self.DeleteAll)
        self.Menu.add_command(label='Quit w', command=self.janela.destroy)
        
        
        self.janela.config(menu=self.Menu)
        self.janela.mainloop()


    #Funções
    
    def DefaultList(self):
        self.ButList:list[tk.Button] = []
        self.TextList:list[tk.Label] = []
        self.EntryList:list[tk.Entry] = []

        
    def DeleteAll(self):
        if (len(self.janela.winfo_children()) > 0):
            for widget in self.janela.winfo_children():
                if (widget != self.Menu):
                    widget.destroy()
            self.DefaultList()

    def ClearEntry(self, EntryIndex:int):
        if (len(self.EntryList) > 0):
            self.EntryList[EntryIndex].delete(0, 'end')
    

    #Classes

    class TextManager:

        def __init__(self, SetGUI):
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
            
        def PrintDisplay(self, Info):
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
        def __init__(self, SetGUI):
            self.Gui:SalameGUI = SetGUI
            self.janela = self.Gui.janela
        
        def PresetEntryPosition(self,Entry:tk.Entry, PositionX:int, PositionTag:int, DefaultPos:int = 0):           
            CutYPos:int = ((PositionTag - 1) * 50)
            if (PositionTag == 1):
                Entry.place(x=PositionX, y=DefaultPos)
                self.EntrySpaceY = DefaultPos
            else:
                Entry.place(x=PositionX, y=DefaultPos + self.EntrySpaceY + CutYPos)

        def CreateEntry(self, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):

            EntryToCreate:tk.Entry = tk.Entry(self.janela)
            EntryToCreate.configure(font=('Arial', 14))
            EntryToCreate.config(width=6, border=1, relief="groove")
            if (CustomYPosition > 0):
                EntryToCreate.place(x=PositionX, y=CustomYPosition)
            else:
                self.PresetEntryPosition(EntryToCreate, PositionX, PositionTag, DefaultPos)
            if (self.Gui.EntryList.count(EntryToCreate) == 0):
                self.Gui.EntryList.append(EntryToCreate)



    class ButtonManager():

        def __init__(self, SetGUI):
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

    class JanelaModels:
        def __init__(self , SetGui):
            self.Gui:SalameGUI = SetGui
            SetGui.janela.configure(bg='#000000')
            SetGui.janela.title('Janela Edit')
            SetGui.janela.geometry('1600x800')
            self.PerfilList:list[Enum] = [self.Presets.Default, self.Presets.AnimeSet, self.Presets.AnimeGet]
            self.SelectedPreset = self.Presets.Default
        
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
                - Selected preset

            """
            if (len(self.Gui.janela.winfo_children()) > 1):      
                for i in range(len(self.Gui.ButList)):
                    self.Gui.ButList[i].destroy()
                for i in range(len(self.Gui.EntryList)):
                    self.Gui.EntryList[i].destroy()
                for i in range(len(self.Gui.TextList)):
                    self.Gui.TextList[i].destroy()
                for i in self.Gui.Texto.GetList:
                    i.destroy()
                self.Gui.ButList = []
                self.Gui.EntryList = []
                self.Gui.TextList = []
                self.SelectedPreset = self.Presets.Default
            
            
        
        def AnimeSet(self):
            """
            Sets up the AnimeSet GUI.

            This function creates and configures the necessary GUI elements for the AnimeSet preset.
            If the selected preset is not the AnimeSet, it deletes the existing preset and creates
            the AnimeSet preset.

            """
            ButtonIndex = AnimeSet.ButtonIndex()
            EntryIndex = AnimeSet.EntryIndex()
            TextIndex = AnimeSet.TextIndex()
            

            if (self.SelectedPreset != self.Presets.AnimeSet):
                self.DeletePreset()

                #AddAnime
                self.Gui.Button.CreateBut('AddAnime',self.Gui.ExecFunc.Add , 350, 1 , 123)
                
                #Name
                self.Gui.Entry.CreateEntry(200, 1, 39)
                self.Gui.EntryList[EntryIndex.AddAnime.Name].config(width=25)
                #MaxEp
                self.Gui.Entry.CreateEntry(200, 2)
                self.Gui.EntryList[EntryIndex.AddAnime.MaxEp].config(width=2)
                #Status
                self.Gui.Entry.CreateEntry(200, 3)
                self.Gui.EntryList[EntryIndex.AddAnime.Status].config(width=11)
                #Season
                self.Gui.Entry.CreateEntry(200, 4)
                self.Gui.EntryList[EntryIndex.AddAnime.Season].config(width=12)
                #Serie
                self.Gui.Entry.CreateEntry(200, 5)
                self.Gui.EntryList[EntryIndex.AddAnime.Serie].config(width=15)

                #Name
                self.Gui.Texto.CreateText("Name", 100, 1, 30)
                #MaxEp
                self.Gui.Texto.CreateText("MaxEp", 100, 2)
                #Status
                self.Gui.Texto.CreateText("Status", 100, 3)
                ToolTip(self.Gui.TextList[TextIndex.AddAnime.Status], "Can be Watching, Completed, Dropped, or PlanToWatch.", delay=0.1)
                #Season
                self.Gui.Texto.CreateText("Season", 100, 4)
                #Serie
                self.Gui.Texto.CreateText("Serie", 100, 5)
                ToolTip(self.Gui.TextList[TextIndex.AddAnime.Serie], "Is optional.", delay=0.1)


                #DeleteAnime
                self.Gui.Button.CreateBut('DeleteAnime',self.Gui.ExecFunc.RemoveAnime , 1100, 1 , 670)

                self.Gui.Texto.CreateText("Name", 1100, 1, 612)

                self.Gui.Entry.CreateEntry(1200, 1, 620)
                self.Gui.EntryList[EntryIndex.DeleteAnime.Name].config(width=25)


                #AddEpp
                self.Gui.Button.CreateBut('AddEp',self.Gui.ExecFunc.AddEppisode , 1180, 1 , 150)
                self.Gui.Button.CreateBut('SetEp',self.Gui.ExecFunc.SetEpisode , 1315, 1 , 150)

                self.Gui.Texto.CreateText("AddEpisode", 1250, 1, 25)
                self.Gui.TextList[TextIndex.AddEpisode.AddEpisode].config(width=12, height= 3, font=('Arial', 13))


                self.Gui.Texto.CreateText("Name", 1072, 1, 102)
                ToolTip(self.Gui.TextList[TextIndex.AddEpisode.Name], "Can be simplified.", delay=0.1)
                self.Gui.Entry.CreateEntry(1168, 1, 110)
                self.Gui.EntryList[EntryIndex.AddEpisode.Name].config(width=25)

                
                
                self.Gui.Entry.CreateEntry(1355, 1, 226)
                self.Gui.EntryList[EntryIndex.AddEpisode.Ep].config(width=2)


                #UpdateScore
                self.Gui.Button.CreateBut('UpdateScore',self.Gui.ExecFunc.UpdateScore , 1230, 1 , 360)

                self.Gui.Texto.CreateText("Name", 1062, 1, 318)

                self.Gui.Entry.CreateEntry(1155, 1, 326)
                self.Gui.EntryList[EntryIndex.UpdateScore.Name].config(width=25)
                
                self.Gui.Entry.CreateEntry(1455, 1, 326)
                self.Gui.EntryList[EntryIndex.UpdateScore.Score].config(width=3)


                #RemoveLeastAdded
                self.Gui.Button.CreateBut('RemoveLeastAdded',self.Gui.ExecFunc.RemoveLeastAdded , 1300, 1 , 670)
                self.Gui.ButList[ButtonIndex.RemoveLeastAdded].config(width=17)


                #SetCurrentStatus
                self.Gui.Button.CreateBut('SetCurrentStatus', self.Gui.ExecFunc.OverrideCurrentStatus, 1340, 1 , 500)
                self.Gui.ButList[ButtonIndex.SetCurrentStatus].config(width=14)
                

                self.Gui.Texto.CreateText("Name", 1080, 1, 450)

                self.Gui.Entry.CreateEntry(1180, 1, 460)
                self.Gui.EntryList[EntryIndex.SetCurrentStatus.Name].config(width=25)
                
                self.Gui.Texto.CreateText("SetStatus", 1080, 2)
                self.Gui.TextList[TextIndex.SetCurrentStatus.SetStatus].config(width=10)
                ToolTip(self.Gui.TextList[TextIndex.SetCurrentStatus.SetStatus], "Can be Watching, Completed, Dropped, or PlanToWatch.", delay=0.1)
   
                self.Gui.Entry.CreateEntry(1180, 2)
                self.Gui.EntryList[EntryIndex.SetCurrentStatus.Status].config(width=11)

                #SetMyAnimeListLink
                self.Gui.Button.CreateBut('SetMyAnimeListLink', self.Gui.ExecFunc.AddMyAnimeListLink, 250, 1 , 420)
                self.Gui.ButList[ButtonIndex.SetMyAnimeListLink].config(width=16)

                self.Gui.Texto.CreateText("Name", 100, 1, 320)

                self.Gui.Entry.CreateEntry(200, 1, 330)
                self.Gui.EntryList[EntryIndex.MyAnimeListLink.Name].config(width=25)

                self.Gui.Texto.CreateText("MyAnimeListLink", 40, 2)
                self.Gui.TextList[TextIndex.MyAnimeListLink.Link].config(width=16, font=('Arial', 13))

                self.Gui.Entry.CreateEntry(200, 2)
                self.Gui.EntryList[EntryIndex.MyAnimeListLink.Link].config(width=25)

                #AddToCalendar
                self.Gui.Button.CreateBut('AddToCalendar', self.Gui.ExecFunc.AddToCalendar, 700, 1 , 660)
                self.Gui.ButList[ButtonIndex.AddToCallendar].config(width=13)

                self.Gui.Texto.CreateText("Name", 600, 1, 550)

                self.Gui.Entry.CreateEntry(700, 1, 559)
                self.Gui.EntryList[EntryIndex.AddToCallendar.Name].config(width=25)

                self.Gui.Texto.CreateText("Day", 600, 2)
                ToolTip(self.Gui.TextList[TextIndex.AddToCallendar.Day], "Can be one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday.", delay=0.1)

                self.Gui.Entry.CreateEntry(700, 2)
                self.Gui.EntryList[EntryIndex.AddToCallendar.Day].config(width=10)

                #SetSeasonLink
                self.Gui.Button.CreateBut('SetSeasonLink', self.Gui.ExecFunc.SetSeasonLink, 200, 1 , 610)
                self.Gui.ButList[ButtonIndex.SetSeasonLink].config(width=13)

                self.Gui.Texto.CreateText("SeasonID", 100, 1, 510)

                self.Gui.Entry.CreateEntry(200, 1, 519)
                self.Gui.EntryList[EntryIndex.SetSeasonLink.SeasonID].config(width=12)

                self.Gui.Texto.CreateText("Link", 100, 2)

                self.Gui.Entry.CreateEntry(200, 2)
                self.Gui.EntryList[EntryIndex.SetSeasonLink.Link].config(width=25)




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

            ButtonIndex = AnimeGet.ButtonIndex()
            EntryIndex = AnimeGet.EntryIndex()
            TextIndex = AnimeGet.TextIndex()
                
            

            if (self.SelectedPreset != self.Presets.AnimeGet):
                
                self.DeletePreset()
                self.InitDisplay()

                #GetStatus        
                self.Gui.Button.CreateBut('GetStatus',self.Gui.ExecFunc.GetAnimeStatus , 230, 1 , 80)
                self.Gui.ButList[ButtonIndex.GetStatus].config(width=12)
                ToolTip(self.Gui.ButList[ButtonIndex.GetStatus], "Print the data of the selected anime.", delay=0.1)
                
                self.Gui.Texto.CreateText("Name", 80, 1, 30)
                ToolTip(self.Gui.TextList[TextIndex.GetStatus.Name], "Can be simplified.", delay=0.1)

                self.Gui.Entry.CreateEntry(170, 1, 39)
                self.Gui.EntryList[EntryIndex.GetStatus.Name].config(width=25)


                #PrintSeason
                self.Gui.Button.CreateBut('PrintSeason',self.Gui.ExecFunc.PrintSeason , 170, 1 , 200)
                self.Gui.ButList[ButtonIndex.PrintSeason].config(width=12)

                self.Gui.Texto.CreateText("SeasonID", 80, 1, 150)
                ToolTip(self.Gui.TextList[TextIndex.PrintSeason.SeasonID], "File name containing season data.", delay=0.1)

                self.Gui.Entry.CreateEntry(170, 1, 159)
                self.Gui.EntryList[EntryIndex.PrintSeason.SeasonID].config(width=12)

                
                #PrintStatusList
                self.Gui.Button.CreateBut('PrintStatusList',self.Gui.ExecFunc.PrintStatusList , 170, 1 , 320)
                self.Gui.ButList[ButtonIndex.PrintStatusList].config(width=14)
                ToolTip(self.Gui.ButList[ButtonIndex.PrintStatusList], "If StatusID is empty, all statuses will be printed.", delay=0.1)

                self.Gui.Texto.CreateText("StatusID", 80, 1, 270)
                ToolTip(self.Gui.TextList[TextIndex.PrintStatusList.StatusID], "Can be Watching, Completed, Dropped, or PlanToWatch.", delay=0.1)
                self.Gui.Entry.CreateEntry(170, 1, 279)
                self.Gui.EntryList[EntryIndex.PrintStatusList.StatusID].config(width=11)


                #OpenLink
                self.Gui.Button.CreateBut('OpenLink',self.Gui.ExecFunc.OpenLink , 170, 1 , 560)

                self.Gui.Texto.CreateText("Name", 80, 1, 510)
                self.Gui.Entry.CreateEntry(170, 1, 519)
                self.Gui.EntryList[EntryIndex.OpenLink.Name].config(width=25)


                #PrintSerie
                self.Gui.Button.CreateBut('PrintSerie',self.Gui.ExecFunc.PrintSerie , 170, 1 , 440)

                self.Gui.Texto.CreateText("Name", 80, 1, 390)
                self.Gui.Entry.CreateEntry(170, 1, 399)
                self.Gui.EntryList[EntryIndex.PrintSerie.Name].config(width=15)


                #PrintAnimeList
                self.Gui.Button.CreateBut('PrintAnimeList',self.Gui.ExecFunc.PrintAnimeList , 1200, 1 , 200)
                self.Gui.ButList[ButtonIndex.PrintAnimeList].config(width=14)
                

                #PrintSerieList
                self.Gui.Button.CreateBut('PrintSerieList',self.Gui.ExecFunc.PrintSerieList , 1200, 1 , 350)
                self.Gui.ButList[ButtonIndex.PrintSerieList].config(width=14)


                #OpenMyAnimeList
                self.Gui.Button.CreateBut('OpenMyAnimeList',self.Gui.ExecFunc.OpenMyAnimeList , 700, 1 , 20)
                self.Gui.ButList[ButtonIndex.OpenMyAnimeList].config(width=16)


                #PrintCalendar
                self.Gui.Button.CreateBut('PrintCalendar', self.Gui.ExecFunc.PrintSeasonCalendar, 700, 1 , 680)
                self.Gui.ButList[ButtonIndex.PrintCallendar].config(width=13)
                ToolTip(self.Gui.ButList[ButtonIndex.PrintCallendar], "Show season calendar", delay=0.1)

                self.Gui.Texto.CreateText("SeasonID", 600, 1, 630)
                ToolTip(self.Gui.TextList[TextIndex.PrintCallendar.SeasonID], "File name containing season data", delay=0.1)

                self.Gui.Entry.CreateEntry(700, 1, 639)
                self.Gui.EntryList[EntryIndex.PrintCallendar.SeasonID].config(width=12)

                #OpenSeasonLink
                self.Gui.Button.CreateBut('OpenSeasonLink',self.Gui.ExecFunc.OpenSeasonLink , 170, 1 , 680)
                self.Gui.ButList[ButtonIndex.OpenSeasonLink].config(width=16)

                self.Gui.Texto.CreateText("SeasonID", 80, 1, 630)
                self.Gui.Entry.CreateEntry(170, 1, 639)
                self.Gui.EntryList[EntryIndex.OpenSeasonLink.SeasonID].config(width=12)


                self.SelectedPreset = self.Presets.AnimeGet
            else:
                print("Already in AnimeGet")
        
        class Presets(Enum):
            Default = 0
            AnimeSet = 1
            AnimeGet = 2
        

#ExternalClasses

class DataConverter:

    def __init__(self):
        pass
        

Gui = SalameGUI()
    