from Script.GUI_Index import AnimeI
from Script.ManageData.Anime.AnimeLists import GetAnimeList
class OpenLinks:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.AnimeIndex = AnimeI()

    def OpenMyAnimeListLink(self):
        self.Gui.Button.CreateBut('OpenMyAnimeListLink', self.Gui.AnimeExec.OpenMyAnimeListLink , 170, 1 , 560)
        self.AnimeIndex.OpenMyAnimeListLink.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.OpenMyAnimeListLink.ButtonIndex.OpenLink].config(width=19)

        self.Gui.Text.CreateText("Name", 80, 1, 510)
        self.AnimeIndex.OpenMyAnimeListLink.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.OpenMyAnimeListLink.TextIndex.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 519)
        self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name].AddList(GetAnimeList.HasMAL_LinkList)
        self.Gui.EntryList[self.AnimeIndex.OpenMyAnimeListLink.EntryIndex.Name].config(width=25)

    def OpenWatchLink(self):
        self.Gui.Button.CreateBut('OpenWatchLink', self.Gui.AnimeExec.OpenWatchLink , 170, 1 , 440)
        self.AnimeIndex.OpenWatchLink.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.OpenWatchLink.ButtonIndex.OpenLink].config(width=14)

        self.Gui.Text.CreateText("Name", 80, 1, 390)
        self.AnimeIndex.OpenWatchLink.TextIndex.Name = self.Gui.Presets.UpdateTextIndex()
        self.Gui.Presets.CreateTooltip(self.Gui.TextList[self.AnimeIndex.OpenWatchLink.TextIndex.Name], "Can be simplified.")

        self.Gui.Entry.CreateEntry(170, 1, 399)
        self.AnimeIndex.OpenWatchLink.EntryIndex.Name = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.OpenWatchLink.EntryIndex.Name].AddList(GetAnimeList.HasWatchLinkList)
        self.Gui.EntryList[self.AnimeIndex.OpenWatchLink.EntryIndex.Name].config(width=25)

    def OpenMyAnimeListHomePage(self):
        self.Gui.Button.CreateBut('OpenMALHomePage', self.Gui.AnimeExec.OpenMALHomePage , 100, 1 , 20)
        self.AnimeIndex.OpenMyAnimeListHomePage.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.OpenMyAnimeListHomePage.ButtonIndex.OpenLink].config(width=16)

    def OpenSeasonLink(self):
        self.Gui.Button.CreateBut('OpenSeasonLink', self.Gui.AnimeExec.OpenSeasonLink , 170, 1 , 680)
        self.AnimeIndex.OpenSeasonLink.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.AnimeIndex.OpenSeasonLink.ButtonIndex.OpenLink].config(width=16)

        self.Gui.Text.CreateText("SeasonID", 80, 1, 630)
        self.AnimeIndex.OpenSeasonLink.TextIndex.SeasonID = self.Gui.Presets.UpdateTextIndex()

        self.Gui.Entry.CreateEntry(170, 1, 639)
        self.AnimeIndex.OpenSeasonLink.EntryIndex.SeasonID = self.Gui.Presets.UpdateEntryIndex()
        self.Gui.EntryList[self.AnimeIndex.OpenSeasonLink.EntryIndex.SeasonID].AddList(GetAnimeList.GetListedSeasons, True)
        self.Gui.EntryList[self.AnimeIndex.OpenSeasonLink.EntryIndex.SeasonID].config(width=12)