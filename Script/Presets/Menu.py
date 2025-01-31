from Script.GUI_Index import MenuI

class Menu:
    def __init__(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.MenuIndex = MenuI()

    
    def Geral(self):
        #Anime
        self.Gui.Text.CreateText('Anime', 180, 1, 80)
        self.MenuIndex.Anime.TextIndex.Anime = self.Gui.Presets.UpdateTextIndex()
        self.Gui.TextList[self.MenuIndex.Anime.TextIndex.Anime].config(font=('Arial', 31))

        self.Gui.Button.CreateBut('Add', self.Gui.Models.AnimeAddPreset , 150, 1, 220)
        self.MenuIndex.Anime.ButtonIndex.AddInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Anime.ButtonIndex.AddInfo].config(width=8, font=('Arial', 16))

        self.Gui.Button.CreateBut('Edit', self.Gui.Models.AnimeEditPreset , 300, 1 , 220)
        self.MenuIndex.Anime.ButtonIndex.EditInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Anime.ButtonIndex.EditInfo].config(width=8, font=('Arial', 16))

        self.Gui.Button.CreateBut('Open', self.Gui.Models.AnimeOpenPreset , 150, 1, 300)
        self.MenuIndex.Anime.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Anime.ButtonIndex.OpenLink].config(width=8, font=('Arial', 16))

        self.Gui.Button.CreateBut('View', self.Gui.Models.AnimeViewPreset , 300, 1, 300)
        self.MenuIndex.Anime.ButtonIndex.ViewInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Anime.ButtonIndex.ViewInfo].config(width=8, font=('Arial', 16))

        #Manga
        self.Gui.Text.CreateText('Manga', 1180, 1, 80)
        self.MenuIndex.Manga.TextIndex.Manga = self.Gui.Presets.UpdateTextIndex()
        self.Gui.TextList[self.MenuIndex.Manga.TextIndex.Manga].config(font=('Arial', 31))

        self.Gui.Button.CreateBut('Add', self.Gui.Models.MangaAddPreset , 1150, 1 , 220)
        self.MenuIndex.Manga.ButtonIndex.AddInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Manga.ButtonIndex.AddInfo].config(width=8, font=('Arial', 16))

        self.Gui.Button.CreateBut('Edit', self.Gui.Models.MangaEditPreset , 1300, 1 , 220)
        self.MenuIndex.Manga.ButtonIndex.EditInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Manga.ButtonIndex.EditInfo].config(width=8, font=('Arial', 16))

        self.Gui.Button.CreateBut('Open', self.Gui.Models.MangaOpenPreset , 1150, 1, 300)
        self.MenuIndex.Manga.ButtonIndex.OpenLink = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Manga.ButtonIndex.OpenLink].config(width=8, font=('Arial', 16))

        self.Gui.Button.CreateBut('View', self.Gui.Models.MangaViewPreset , 1300, 1, 300)
        self.MenuIndex.Manga.ButtonIndex.ViewInfo = self.Gui.Presets.UpdateButtonIndex()
        self.Gui.ButList[self.MenuIndex.Manga.ButtonIndex.ViewInfo].config(width=8, font=('Arial', 16))

        """ self.Gui.Text.CreateText('Settings', 1400, 1, 500) """
        