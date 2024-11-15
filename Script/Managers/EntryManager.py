from tkinter import ttk
from Script.Managers.CustomTypes.CustomEntry import CustomEntry
from Script.Managers.EntryTypeList import EntryTypeList

class EntryManager():

    def GuiInit(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI
        self.janela = self.Gui.janela
        self.EntryType:EntryTypeList = EntryTypeList()

    def PresetEntryPosition(self, Entry:ttk.Combobox, PositionX:int, PositionTag:int, DefaultPos:int = 0):           
        CutYPos:int = ((PositionTag - 1) * 50)
        if (PositionTag == 1):
            Entry.place(x=PositionX, y=DefaultPos)
            self.EntrySpaceY = DefaultPos
        else:
            Entry.place(x=PositionX, y=DefaultPos + self.EntrySpaceY + CutYPos)
    
    def UpdateFilterEntrys(self):
        self.Gui.AnimeDataLists.UpdateList()
        for i in self.Gui.Entry.EntryType.AnimeList:
            i["values"] = self.Gui.AnimeDataLists.SelectedList
    
    def UpdateEntrysOptions(self):
        for i in self.Gui.Entry.EntryType.UpdateList:
            i.UpdateOptions()

    def CreateEntry(self, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):

        EntryToCreate:ttk.Combobox = CustomEntry(self.janela)
        EntryToCreate.configure(font=('Arial', 14))
        EntryToCreate.config(width=6)
        if (CustomYPosition > 0):
            EntryToCreate.place(x=PositionX, y=CustomYPosition)
        else:
            self.PresetEntryPosition(EntryToCreate, PositionX, PositionTag, DefaultPos)
        if (self.Gui.EntryList.count(EntryToCreate) == 0):
            self.Gui.EntryList.append(EntryToCreate)

