from Script.GUI_Index import CustomI

class CustomPresets:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.CustomIndex = CustomI()

    def Filter(self):
        self.Gui.Text.CreateLabel("Filter", 920, 1, 20)
        self.CustomIndex.Filter.TextIndex.Selected = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(1000, 1, 25)
        self.CustomIndex.Filter.EntryIndex.Selected = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.CustomIndex.Filter.EntryIndex.Selected].AddList(self.Gui.AnimeDataLists.GetList, True)
        self.Gui.EntryList[self.CustomIndex.Filter.EntryIndex.Selected].SetActiveSwitch(self.Gui.Entry.UpdateFilterEntrys)
        self.Gui.EntryList[self.CustomIndex.Filter.EntryIndex.Selected].config(width=12)
    
    def ReturnToMenu(self):
        self.Gui.Button.CreateBut('Menu', self.Gui.Models.MenuPreset , 650, 1 , 20)
        self.CustomIndex.ReturnToMenu.ButtonIndex.Menu = self.Gui.Presets.UpdateButtonIndex()