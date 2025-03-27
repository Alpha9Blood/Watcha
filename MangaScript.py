import os
import webbrowser as web
from tkinter import ttk
from Script.ManageData.Manga.MangaObj import Manga
from Script.Managers.CustomTypes.CustomEntry import CustomEntry
from Script.GUI_Index import MangaI
from Script.Utils import JsonUtil
from Script.ManageData.Manga.MangaLists import GetMangaList
from Script.ManageData.Manga.MangaWatcha import Watch


class MangaExecute:
    def __init__(self):    
        self.MangaIndex = MangaI()

    def GuiInit(self, Gui):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = Gui

    #Tools

    def __GetEntry(self, index:int) -> str:
        """
        Retrieves the text from the entry field at the given index in the GUI.

        Args:
            index (int): The index of the entry field to retrieve the text from.

        Returns:
            str: The text from the entry field at the given index.
        """
        EntryList:list[CustomEntry] = self.Gui.EntryList
        return EntryList[index].get()
    
    def __ClearEntry(self, Index:int = -1, IndexList:list = []):  
        """
        Clears the entry fields in the GUI.

        Args:
            Index (int): The index of the entry field to clear. Defaults to -1.
            IndexList (list): A list of indices of entry fields to clear. Defaults to an empty list.

        """
        EntryList:list[CustomEntry] = self.Gui.EntryList

        if (Index > -1):
            EntryList[Index].delete(0, 'end')

        if (IndexList != []):
            for i in IndexList:
                Entry:ttk.Combobox = EntryList[i]
                Entry.delete(0, 'end')
    
    def __FindName(self, Name:str, CustomData:list[str] = []) -> str:
        
        if (Name == ""):
            raise Exception("__FindName: name is empty")
        
        Name = Name.lower()

        if (not CustomData):
            MangaList:list[str] = GetMangaList.MangaList()
        else:
            MangaList:list[str] = CustomData

        if (Name in MangaList):
            return Name

        for var in MangaList:
            if (Name in var.lower()):
                Name = var
                return Name
        
        raise Exception(f"__FindName: Manga name not found: {Name} in {MangaList}")



    #Set


    def AddNewManga(self):
        Name:str = self.__GetEntry(self.MangaIndex.AddNewManga.EntryIndex.Name)
        
        if (Name == ""):
            print("AddNewManga manga name is empty")
            return

        if (Name in GetMangaList.MangaList()):
            print("AddNewManga manga already exists")
            return
        
        Status:str = self.__GetEntry(self.MangaIndex.AddNewManga.EntryIndex.Status)

        if (Status not in GetMangaList.CurrentStatusTypeList()):
            print("AddNewManga invalid status")
            return

        Chapters:str = self.__GetEntry(self.MangaIndex.AddNewManga.EntryIndex.Chapters)
        
        if (Chapters != ""):
            try:
                ChaptersI = int(Chapters)
                if (ChaptersI < 0):
                    ChaptersI = 0
            except:
                raise ValueError(f"AddNewManga: {Chapters = } must be a integer number.")
        else:
            ChaptersI = 0

        Watch.AddManga(Name, ChaptersI, Status)
        self.__ClearEntry(self.MangaIndex.AddNewManga.EntryIndex.Name)
        self.__ClearEntry(self.MangaIndex.AddNewManga.EntryIndex.Chapters)
        self.__ClearEntry(self.MangaIndex.AddNewManga.EntryIndex.Status)
    
    def DeleteManga(self):
        Name:str = self.__GetEntry(self.MangaIndex.RemoveManga.EntryIndex.Name)

        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("DeleteManga manga name is empty")
            return
        
        Watch.RemoveManga(Name)
        self.__ClearEntry(self.MangaIndex.RemoveManga.EntryIndex.Name)

    def SetLink(self):
        Name:str = self.__GetEntry(self.MangaIndex.SetLink.EntryIndex.Name)

        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("AddLink manga not found")
            return
        else:
            Link:str = self.__GetEntry(self.MangaIndex.SetLink.EntryIndex.Link)
        
        if (Link == ""):
            print("SetLink manga link is empty")
            return
        
        Watch.AddLink(Name, Link)
        self.__ClearEntry(self.MangaIndex.SetLink.EntryIndex.Name)
        self.__ClearEntry(self.MangaIndex.SetLink.EntryIndex.Link)

    def EditFavorite(self, Add:bool):
        Name:str = self.__GetEntry(self.MangaIndex.EditFavorites.EntryIndex.Name)
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("EditFavorite manga not found")
            return
        
        if (Add):
            Watch.EditFavorite(Name)
            self.__ClearEntry(self.MangaIndex.EditFavorites.EntryIndex.Name)
        else:
            Watch.EditFavorite(Name, Add)
            self.__ClearEntry(self.MangaIndex.EditFavorites.EntryIndex.Name)
    
    def AddFavorite(self):
        self.EditFavorite(True)

    def DeleteFavorite(self):
        self.EditFavorite(False)
    
    def EditChapters(self, Set:bool):
        Name:str = self.__GetEntry(self.MangaIndex.EditChapters.EntryIndex.Name)
        
        if (Name == ""):
            print("EditChapters manga name is empty")
            return

        OnGoingList:list[str] = GetMangaList.OnGoingList()
        Name = self.__FindName(Name, OnGoingList)
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("SetChapters manga not found")
            return
        
        Chapters:str = self.__GetEntry(self.MangaIndex.EditChapters.EntryIndex.Chapters)   
        if (Set):
            if (Chapters == ""):
                print("EditChapters manga chapters is empty")
                return
            
            Watch.EditChapters(Name, Set, Chapters)
            self.__ClearEntry(self.MangaIndex.EditChapters.EntryIndex.Name)
            self.__ClearEntry(self.MangaIndex.EditChapters.EntryIndex.Chapters)
        else:
            Watch.EditChapters(Name)
            self.__ClearEntry(self.MangaIndex.EditChapters.EntryIndex.Name)
            
    def SetChapters(self):
        self.EditChapters(True)

    def AddChapters(self):
        self.EditChapters(False)
    
    def EditInfo(self):
        Name:str = self.__GetEntry(self.MangaIndex.EditInfo.EntryIndex.Name)
        
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("SetStatus manga name not found")
            return
        
        Status:str = self.__GetEntry(self.MangaIndex.EditInfo.EntryIndex.Status)
        if (Status != ""):
            Watch.SetCurrentStatus(Name, Status)
            self.__ClearEntry(self.MangaIndex.EditInfo.EntryIndex.Status)
        
        Score:str = self.__GetEntry(self.MangaIndex.EditInfo.EntryIndex.Score)
        if (Score != ""):
            Watch.EditScore(Name, Score)
            self.__ClearEntry(self.MangaIndex.EditInfo.EntryIndex.Score)

        self.__ClearEntry(self.MangaIndex.EditInfo.EntryIndex.Name)
            

    def AddMyAnimeListLink(self):
        Name = self.__GetEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name)
        
        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print(f"AddMyAnimeListLink path not found: {Name = }")
            return
        
        Link = self.__GetEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Link)
        if (Link == ""):
            print("AddMyAnimeListLink link is empty")
            return
        
        if ("https://myanimelist.net/manga/" not in Link):
            print("AddMyAnimeListLink link is not myanimelist")
            return
        
        Watch.UpdateMyAnimeListLink(Name, Link)
        self.Gui.ImageExtractor.StoreExtractedImage(Name, Link)
        self.__ClearEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name)
        self.__ClearEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Link)
    

    #Get

    def __LoadImage(self, Name:str):
        Selected:Manga = Manga()
        Selected.UpdateData(Name)
        self.Gui.ImageSlot.ProcessPhoto(Selected)

    def PrintManga(self):
        Name:str = self.__GetEntry(self.MangaIndex.PrintInfo.EntryIndex.Name)

        if (Name == ""):
            print("SetEpisode: name is empty")
            return
        
        Name = self.__FindName(Name)

        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("PrintManga manga not found")
            return
        
        if (Name not in self.Gui.EntryList[self.MangaIndex.PrintInfo.EntryIndex.Name].options):
            print(f"PrintManga {Name = } not found in options")
            return
            
        self.Gui.Text.PrintDisplay(Watch.GetStatus(Name))
        self.__LoadImage(Name)
        self.__ClearEntry(self.MangaIndex.PrintInfo.EntryIndex.Name)

    def PrintCurrentStatus(self):
        Status:str = self.__GetEntry(self.MangaIndex.PrintCurrentStatus.EntryIndex.Status)

        if (not os.path.exists(f"./Data/MangaStatusList.json")):
            print("MangaStatusList not found")
            return
        
        if (Status == ""):
            self.Gui.Text.PrintDisplay(Watch.GetCurrentStatus(Status))
            self.__ClearEntry(self.MangaIndex.PrintCurrentStatus.EntryIndex.Status)
        else:
            if (Status not in GetMangaList.CurrentStatusTypeList()):
                print("PrintCurrentStatus status not found")
                return
            
            Info:dict = JsonUtil.LoadJson(f"./Data/MangaStatusList.json")[Status]
            NewInfo:list[str] = []
            for i in range(len(Info)):
                SelectedManga:Manga = Watch.SelectManga(Info[i])
                NewInfo.append(SelectedManga.Name)
                NewInfo.append(f"Chapters:{SelectedManga.Chapters}, Updated:{SelectedManga.LeastTimeUpdated}")

            self.Gui.Text.PrintDisplay(NewInfo)
            self.__ClearEntry(self.MangaIndex.PrintCurrentStatus.EntryIndex.Status)
                
        

    def OpenLink(self):
        Name:str = self.__GetEntry(self.MangaIndex.OpenLink.EntryIndex.Name)

        if (Name == ""):
            print("SetEpisode: name is empty")
            return
        
        Name = self.__FindName(Name)

        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("OpenLink manga not found")
            return
        else:
            SelectedManga:Manga = Watch.SelectManga(Name)

        if (Name not in GetMangaList.MangaList()):
            print("OpenLink manga not found in mangalist")
            return
                
        if (SelectedManga.MangaLink == ""):
            print("OpenLink manga link is empty")
            return
                    
        web.open(SelectedManga.MangaLink)
        self.__ClearEntry(self.MangaIndex.OpenLink.EntryIndex.Name)
            
    
    def OpenMAL_Link(self):
        Name:str = self.__GetEntry(self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name)

        if (Name == ""):
            print("SetEpisode: name is empty")
            return
        
        Name = self.__FindName(Name)

        if (not os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            print("OpenMAL_Link: manga not found")
            return
        if (Name not in self.Gui.EntryList[self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name].options):
            print(f"OpenMAL_Link: manga name: {Name}")
            return
        
        SelectedManga:Manga = Watch.SelectManga(Name)
        web.open(SelectedManga.MyAnimeListLink)
        self.__ClearEntry(self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name)
            

    def PrintFavorites(self):
        if (not os.path.exists(f"./Data/FavoriteMangaList.json")):
            print("PrintFavorites favorites not found")
            return
        
        self.Gui.Text.PrintDisplay(JsonUtil.LoadJson(f"./Data/FavoriteMangaList.json"))