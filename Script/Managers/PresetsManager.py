from tktooltip.tooltip import ToolTip

class PresetsManager:

    def __init__(self):
        self.EntryIndex = 0
        self.TextIndex = 0
        self.ButtonIndex = 0
        

    def GuiInit(self, SetGUI):
        from AnimeGUI import SalameGUI
        from Script.Presets.AnimePresetSet import AnimePresetSet
        from Script.Presets.AnimePresetGet import AnimePresetGet
        from Script.Presets.MangaPresetSet import MangaPresetSet
        from Script.Presets.MangaPresetGet import MangaPresetGet
        self.AnimeSet = AnimePresetSet(SetGUI)
        self.AnimeGet = AnimePresetGet(SetGUI)
        self.MangaSet = MangaPresetSet(SetGUI)
        self.MangaGet = MangaPresetGet(SetGUI)
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