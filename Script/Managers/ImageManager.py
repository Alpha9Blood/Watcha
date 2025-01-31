from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO
from Script.ManageData.Anime.AnimeObj import Anime
from Script.ManageData.Manga.MangaObj import Manga
from Script.ManageData.Manga.MangaLists import GetMangaList
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.Utils import JsonUtil
from Script.GUI_Index import AnimeI
from Script.GUI_Index import MangaI

class ImageManager():

    def __init__(self):
        self.Photo:ImageTk.PhotoImage
        self.AnimeLabelIndex = AnimeI()
        self.MangaLabelIndex = MangaI()
        self.LabelIndex:AnimeI | MangaI

    def GuiInit(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.janela = self.Gui.janela

    def __GetCover(self, img:BytesIO) -> ImageTk.PhotoImage:
        image = Image.open(img)
        image = image.resize((200, 300))
        return ImageTk.PhotoImage(image)
    
    def __NoImage(self):
        try:
            image:BytesIO = JsonUtil.LoadImage("./Data/NoImage.png")
            self.Photo = self.__GetCover(image)
            self.Gui.ImageSlot.CreateImage(self.Photo, 1170, 1, 220)
        except Exception as e:
            print("ProcessPhoto:", e)
    
    def ProcessPhoto(self, Obj:Anime | Manga):
        self.ClearImages()
        
        
        AnimeOrManga:str = list(JsonUtil.LoadJson(Obj.Path).keys())[0].lower()

    
        if (AnimeOrManga == "manga"):
            List:list[str] = GetMangaList.MangaList()
            self.LabelIndex = self.MangaLabelIndex
        elif (AnimeOrManga == "anime"):
            List:list[str] = GetAnimeList.AnimeList()
            self.LabelIndex = self.AnimeLabelIndex
        else:
            print("ProcessPhoto: Invalid MAL link")
            return
        
        

        if (Obj.MyAnimeListLink == ""):
            self.__NoImage()
            self.Gui.Presets.CreateTooltip(self.Gui.LabelList[self.LabelIndex.PrintInfo.LabelIndex.Image], "Missing MyAnimeListLink or alike.")
            print("ProcessPhoto: Empty MAL Link")
            return

        if (Obj.Name in List):
            self.Photo = self.__GetCover(self.Gui.ImageExtractor.GetImage(Obj))
            self.Gui.ImageSlot.CreateImage(self.Photo, 1170, 1, 220)
            
        else:
            print("ProcessPhoto: Invalid Name")

    def ClearImages(self):
        if (len(self.Gui.LabelList) == 0): 
            return
        for image in self.Gui.LabelList:
            image.destroy()
        self.Gui.LabelList.clear()
    
    
    def __PresetImagePosition(self, Entry:tk.Label, PositionX:int, PositionTag:int, DefaultPos:int = 0):           
        CutYPos:int = ((PositionTag - 1) * 50)
        if (PositionTag == 1):
            Entry.place(x=PositionX, y=DefaultPos)
            self.EntrySpaceY = DefaultPos
        else:
            Entry.place(x=PositionX, y=DefaultPos + self.EntrySpaceY + CutYPos)

    def CreateImage(self, Image:ImageTk.PhotoImage, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):
        ImageLabel = tk.Label(self.janela, image=Image) # type: ignore
        if (CustomYPosition > 0):
            ImageLabel.place(x=PositionX, y=CustomYPosition)
        else:
            self.__PresetImagePosition(ImageLabel, PositionX, PositionTag, DefaultPos)
        if (ImageLabel not in self.Gui.LabelList):
            self.Gui.LabelList.append(ImageLabel)
            