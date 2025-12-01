from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO
import os
from Script.ManageData.Anime.AnimeObj import Anime
from Script.ManageData.Manga.MangaObj import Manga
from Script.ManageData.Manga.MangaLists import GetMangaList
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.Utils import JsonUtil
from Script.GUI_Index import AnimeI
from Script.GUI_Index import MangaI

class ImageManager():

    def __init__(self):
        self.AnimeLabelIndex = AnimeI()
        self.MangaLabelIndex = MangaI()
        self.LabelIndex:AnimeI | MangaI
        self.InstacedPhotos:list[ImageTk.PhotoImage] = []
        

    def GuiInit(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI
        self.window = self.Gui.window


    def __GetCover(self, img:BytesIO , CoverSize:tuple) -> ImageTk.PhotoImage:
        image = Image.open(img)
        image = image.resize(CoverSize)
        return ImageTk.PhotoImage(image)
    
    def __NoImage(self, posXY:tuple[int, int], CoverSizePixels:tuple[int, int]):
        try:
            image:BytesIO = JsonUtil.LoadImage("./Script/Assets/NoImage.png")
            Photo:ImageTk.PhotoImage = self.__GetCover(image, CoverSizePixels)
            self.InstacedPhotos.append(Photo)
            self.Gui.ImageSlot.CreateImage(self.InstacedPhotos[-1], posXY[0], 1, posXY[1])
        except Exception as e:
            print("ProcessPhoto:", e)
    
    def ProcessPhoto(self, Obj:Anime | Manga, posXY:tuple[int, int], CoverSizePixels:tuple[int, int]):
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
        
        if (not os.path.exists(f"./Data/{AnimeOrManga[0].upper() + AnimeOrManga[1:]}Links.json")):
            raise FileNotFoundError(f"ProcessPhoto: {AnimeOrManga[0].upper() + AnimeOrManga[1:]}Links.json not found")

        Links:dict[str, dict[str, str]] = JsonUtil.LoadJson(f"./Data/{AnimeOrManga[0].upper() + AnimeOrManga[1:]}Links.json")
        if (not Links["MyAnimeListLinks"]):
            raise FileNotFoundError(f"ProcessPhoto: {AnimeOrManga[0].upper() + AnimeOrManga[1:]}Links.json MyAnimeListLinks not found")
        
        if (Obj.Name not in Links["MyAnimeListLinks"] or Links["MyAnimeListLinks"][Obj.Name] == ""):
            self.__NoImage(posXY, CoverSizePixels)
            print(f"ProcessPhoto: {Obj.Name} Empty MAL Link")
            return

        if (Obj.Name not in List):
            print("ProcessPhoto: Invalid Name")
            return
        
        Photo:ImageTk.PhotoImage = self.__GetCover(self.Gui.ImageExtractor.GetImage(Obj), CoverSizePixels)
        self.InstacedPhotos.append(Photo)
        self.Gui.ImageSlot.CreateImage(self.InstacedPhotos[-1], posXY[0], 1, posXY[1])

    def ClearImages(self):
        if (len(self.Gui.TextList) == 0): 
            return
        
        for image in self.Gui.TextList:
            image.destroy()
        self.Gui.TextList.clear()
    
    
    def __PresetImagePosition(self, Entry:tk.Label, PositionX:int, PositionTag:int, DefaultPos:int = 0):           
        CutYPos:int = ((PositionTag - 1) * 50)
        if (PositionTag == 1):
            Entry.place(x=PositionX, y=DefaultPos)
            self.EntrySpaceY = DefaultPos
        else:
            Entry.place(x=PositionX, y=DefaultPos + self.EntrySpaceY + CutYPos)

    def CreateImage(self, Image:ImageTk.PhotoImage, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):
        ImageLabel = tk.Label(self.window, image=Image) # type: ignore
        if (CustomYPosition > 0):
            ImageLabel.place(x=PositionX, y=CustomYPosition)
        else:
            self.__PresetImagePosition(ImageLabel, PositionX, PositionTag, DefaultPos)
        if (ImageLabel not in self.Gui.LabelList):
            self.Gui.LabelList.append(ImageLabel)

    def ReplaceImage(self):
        pass
            