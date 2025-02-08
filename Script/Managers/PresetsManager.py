from tktooltip.tooltip import ToolTip

class PresetsManager:

    def __init__(self):
        self.EntryIndex = 0
        self.TextIndex = 0
        self.ButtonIndex = 0
        self.LabelIndex = 0
        

    def GuiInit(self, SetGUI):
        from WatchaGUI import WatchaGUI

        from Script.Presets.Anime.AddInfoPreset import AddInfo as AnimeAddInfo
        from Script.Presets.Anime.EditInfoPreset import EditInfo as AnimeEditInfo
        from Script.Presets.Anime.OpenLinksPreset import OpenLinks as AnimeOpenLinks
        from Script.Presets.Anime.ViewInfoPreset import ViewInfo as AnimeViewInfo

        from Script.Presets.Manga.AddInfoPreset import AddInfo as MangaAddInfo
        from Script.Presets.Manga.EditInfoPreset import EditInfo as MangaEditInfo
        from Script.Presets.Manga.OpenLinksPreset import OpenLinks as MangaOpenLinks
        from Script.Presets.Manga.ViewInfoPreset import ViewInfo as MangaViewInfo

        from Script.Presets.CustomPresets import CustomPresets
        from Script.Presets.Menu import Menu

        self.AnimeAddInfo = AnimeAddInfo(SetGUI)
        self.AnimeEditInfo = AnimeEditInfo(SetGUI)
        self.AnimeOpenLinks = AnimeOpenLinks(SetGUI)
        self.AnimeViewInfo = AnimeViewInfo(SetGUI)

        self.MangaAddInfo = MangaAddInfo(SetGUI)
        self.MangaEditInfo = MangaEditInfo(SetGUI)
        self.MangaOpenLinks = MangaOpenLinks(SetGUI)
        self.MangaViewInfo = MangaViewInfo(SetGUI)

        self.CustomPresets = CustomPresets(SetGUI)
        self.MenuPreset = Menu(SetGUI)

        self.Gui:WatchaGUI = SetGUI
    
    def CreateTooltip(self, widget, text, delay = 0.1):
        tooltip = ToolTip(widget, text, delay)
        
        self.Gui.ToolTipList.append(tooltip)

    def ResetIndex(self):
        self.EntryIndex = 0
        self.TextIndex = 0
        self.ButtonIndex = 0
    
    def UpdateEntryIndex(self):
        Index = self.EntryIndex
        if (len(self.Gui.EntryList) - 1 > self.EntryIndex): 
            self.EntryIndex += 1
            Index = self.EntryIndex
        return Index
        
    def UpdateTextIndex(self):
        Index = self.TextIndex
        if (len(self.Gui.TextList) - 1 > self.TextIndex): 
            self.TextIndex += 1
            Index = self.TextIndex
        return Index

    def UpdateButtonIndex(self):
        Index = self.ButtonIndex
        if (len(self.Gui.ButList) - 1 > self.ButtonIndex): 
            self.ButtonIndex += 1
            Index = self.ButtonIndex
        return Index

    def UpdateLabelIndex(self):
        Index = self.LabelIndex
        if (len(self.Gui.LabelList) - 1 > self.LabelIndex): 
            self.LabelIndex += 1
            Index = self.LabelIndex
        return Index