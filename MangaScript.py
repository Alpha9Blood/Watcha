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

        for var in MangaList:
            if (Name in var.lower()):
                Name = var
                return Name
        
        raise Exception("__FindName: Manga name not found: " + Name)



    #Set


    def AddNewManga(self):
        Name:str = self.__GetEntry(self.MangaIndex.AddNewManga.EntryIndex.Name)
        
        if (Name != ""):
            Chapters:str = self.__GetEntry(self.MangaIndex.AddNewManga.EntryIndex.Chapters)
            
            if (Chapters != ""):
                try:
                    ChaptersI = int(Chapters)
                    if (ChaptersI < 0):
                        ChaptersI = 0
                except ValueError:
                    print("AddNewManga Chapters must be a integer number")
                    return
            else:
                ChaptersI = 0

            Status:str = self.__GetEntry(self.MangaIndex.AddNewManga.EntryIndex.Status)

            NameList:list[str] = GetMangaList.MangaList()

            if (Name not in NameList):
                Watch.AddManga(Name, ChaptersI, Status)
                self.__ClearEntry(self.MangaIndex.AddNewManga.EntryIndex.Name)
                self.__ClearEntry(self.MangaIndex.AddNewManga.EntryIndex.Chapters)
                self.__ClearEntry(self.MangaIndex.AddNewManga.EntryIndex.Status)
            else:
                print("AddNewManga manga already exists")
        else:
            print("AddNewManga manga name is empty")
    
    def DeleteManga(self):
        Name:str = self.__GetEntry(self.MangaIndex.RemoveManga.EntryIndex.Name)

        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Watch.RemoveManga(Name)
            self.__ClearEntry(self.MangaIndex.RemoveManga.EntryIndex.Name)
        else:
            print("DeleteManga manga name is empty")
    

    def SetLink(self):
        Name:str = self.__GetEntry(self.MangaIndex.SetLink.EntryIndex.Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Link:str = self.__GetEntry(self.MangaIndex.SetLink.EntryIndex.Link)
            if (Link != ""):
                Watch.AddLink(Name, Link)
                self.__ClearEntry(self.MangaIndex.SetLink.EntryIndex.Name)
                self.__ClearEntry(self.MangaIndex.SetLink.EntryIndex.Link)
            else:
                print("SetLink manga link is empty")
        else:
            print("AddLink manga not found")

    def EditFavorite(self, Add:bool):
        Name:str = self.__GetEntry(self.MangaIndex.EditFavorites.EntryIndex.Name)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            if (Add):
                Watch.EditFavorite(Name)
                self.__ClearEntry(self.MangaIndex.EditFavorites.EntryIndex.Name)
            else:
                Watch.EditFavorite(Name, Add)
                self.__ClearEntry(self.MangaIndex.EditFavorites.EntryIndex.Name)
        else:
            print("EditFavorite manga not found")
    
    def AddFavorite(self):
        self.EditFavorite(True)

    def DeleteFavorite(self):
        self.EditFavorite(False)
    
    def EditChapters(self, Set:bool):
        Name:str = self.__GetEntry(self.MangaIndex.EditChapters.EntryIndex.Name)
        OnGoingList:list[str] = GetMangaList.OnGoingList()

        Name = self.__FindName(Name, OnGoingList)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
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
    
        else:
            print("SetChapters manga not found")

    def SetChapters(self):
        self.EditChapters(True)

    def AddChapters(self):
        self.EditChapters(False)
    
    def EditInfo(self):
        Name:str = self.__GetEntry(self.MangaIndex.EditInfo.EntryIndex.Name)
        
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Status:str = self.__GetEntry(self.MangaIndex.EditInfo.EntryIndex.Status)
            Score:str = self.__GetEntry(self.MangaIndex.EditInfo.EntryIndex.Score)

            if (Status != ""):
                Watch.SetCurrentStatus(Name, Status)
                self.__ClearEntry(self.MangaIndex.EditInfo.EntryIndex.Status)
            
            if (Score != ""):
                Watch.EditScore(Name, Score)
                self.__ClearEntry(self.MangaIndex.EditInfo.EntryIndex.Score)
        else:
            print("SetStatus manga name not found")

    def AddMyAnimeListLink(self):
        Name = self.__GetEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name)
        Link = self.__GetEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Link)
        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            Watch.UpdateMyAnimeListLink(Name, Link)
            self.Gui.ImageExtractor.StoreExtractedImage(Name, Link)
            self.__ClearEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Name)
            self.__ClearEntry(self.MangaIndex.SetMyAnimeListLink.EntryIndex.Link)
        else:
            raise Exception(f"AddMyAnimeListLink not found: Name:{Name}, Path:./Data/MangaData/{JsonUtil.TrueName(Name)}.json")   

    
    #Get

    def __LoadImage(self, Name:str):
        Selected:Manga = Manga()
        Selected.UpdateData(Name)
        self.Gui.ImageSlot.ProcessPhoto(Selected)

    def PrintManga(self):
        Name:str = self.__GetEntry(self.MangaIndex.PrintInfo.EntryIndex.Name)
        Name = self.__FindName(Name)

        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            
            self.Gui.Text.PrintDisplay(Watch.GetStatus(Name))
            self.__LoadImage(Name)
            self.__ClearEntry(self.MangaIndex.PrintInfo.EntryIndex.Name)
        else:
            print("PrintManga manga not found")

    def PrintCurrentStatus(self):
        Status:str = self.__GetEntry(self.MangaIndex.PrintCurrentStatus.EntryIndex.Status)
        if (os.path.exists(f"./Data/MangaStatusList.json")):
            
            if (Status == ""):
                self.Gui.Text.PrintDisplay(Watch.GetCurrentStatus(Status))
                self.__ClearEntry(self.MangaIndex.PrintCurrentStatus.EntryIndex.Status)
            else:
                StatusList:list[str] = ["Reading", "PlanToRead", "Completed", "Dropped"]
                if (Status in StatusList):
                    Info:dict = JsonUtil.LoadJson(f"./Data/MangaStatusList.json")[Status]
                    NewInfo:list[str] = []
                    for i in range(len(Info)):
                        SelectedManga:Manga = Watch.SelectManga(Info[i])
                        NewInfo.append(SelectedManga.Name)
                        NewInfo.append(f"Chapters:{SelectedManga.Chapters}, Updated:{SelectedManga.LeastTimeUpdated}")

                    self.Gui.Text.PrintDisplay(NewInfo)
                    self.__ClearEntry(self.MangaIndex.PrintCurrentStatus.EntryIndex.Status)
                else:
                    print("PrintCurrentStatus status not found")
        else:
            print("MangaStatusList not found")

    def OpenLink(self):
        Name:str = self.__GetEntry(self.MangaIndex.OpenLink.EntryIndex.Name)
        Name = self.__FindName(Name)

        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in GetMangaList.MangaList()):
                SelectedManga:Manga = Watch.SelectManga(Name)
                if (SelectedManga.MangaLink != ""):
                    web.open(SelectedManga.MangaLink)
                    self.__ClearEntry(self.MangaIndex.OpenLink.EntryIndex.Name)
                else:
                    print("OpenLink manga link is empty")
            else:
                print("OpenLink manga not found in mangalist")
        else:
            print("OpenLink manga not found")
    
    def OpenMAL_Link(self):
        Name:str = self.__GetEntry(self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name)
        Name = self.__FindName(Name)

        if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(Name)}.json")):
            if (Name in self.Gui.EntryList[self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name].options):
                SelectedManga:Manga = Watch.SelectManga(Name)
                web.open(SelectedManga.MyAnimeListLink)
                self.__ClearEntry(self.MangaIndex.OpenMyAnimeListLink.EntryIndex.Name)
            else:
                raise Exception("OpenMAL_Link: manga not found in mangalist")
        else:
            raise Exception("OpenMAL_Link: manga not found")

    def PrintFavorites(self):
        if (os.path.exists(f"./Data/FavoriteMangaList.json")):
            self.Gui.Text.PrintDisplay(JsonUtil.LoadJson(f"./Data/FavoriteMangaList.json"))
        else:
            print("PrintFavorites favorites not found")
    