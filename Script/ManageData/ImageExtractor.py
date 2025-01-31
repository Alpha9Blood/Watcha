from io import BytesIO
import os
import requests
from Script.Utils import JsonUtil
from Script.ManageData.Anime.AnimeObj import Anime
from Script.ManageData.Manga.MangaObj import Manga

class ImageControler():

    def AnimeOrManga(self, url:str) -> str:
        if ("/anime/" in url):
            return "anime"
        elif ("/manga/" in url):
            return "manga"
        else:
            raise Exception("AnimeOrManga: Invalid url")

    def __GetImageLink(self, url:str, AnimeOrManga:str) -> str:
        MAL_Link:str = f"https://myanimelist.net/{AnimeOrManga}/" 

        if (MAL_Link != url[:len(MAL_Link)]):
            raise Exception(f"GetImageLink: Invalid url MAL_Link: {MAL_Link} url: {url[:len(MAL_Link)]}")
        
        if (AnimeOrManga == "manga"):
            IdVar:str = "<img class=\"lazyload\" data-src=\""
        elif (AnimeOrManga == "anime"):
            IdVar:str = "\n      <img class=\"lazyload\" data-src=\""
        else:
            raise Exception(f"GetImageLink: Invalid url MAL_Link: {MAL_Link} url: {url[:len(MAL_Link)]}")
        
        RequestLink:str = f"{url}/pics"
        Id:str = f"<a href=\"{RequestLink}\">{IdVar}"

        try:
            response = requests.get(f"{url}/pics")
            result:str = response.text
        except:
            raise requests.exceptions.HTTPError("Http Error.")

        if (Id not in result):
            raise Exception(f"GetImageLink: Invalid url MAL_Link: {MAL_Link} / ID: {RequestLink}")
        
        result = result.split(Id)[1]
        result = result.split(".jpg")[0] + ".jpg"

        return result

    def StoreExtractedImage(self, Name:str, MAL_Link:str):
        AnimeOrManga:str = self.AnimeOrManga(MAL_Link)
        
        if (AnimeOrManga == "" or "%" in  MAL_Link):
            raise Exception(f"StoreImage: Invalid url: MAL_Link: {MAL_Link}.")
            
        
        AnimeOrManga = AnimeOrManga[0].upper() + AnimeOrManga[1:]
        
        StorePath:str = f"./Data/{AnimeOrManga}Images/{JsonUtil.TrueName(Name)}.png"
        
        ImageLink:str = self.__GetImageLink(MAL_Link, AnimeOrManga.lower())

        if (ImageLink != ""):
            response = requests.get(ImageLink)
            image:bytes = response.content
            JsonUtil.StoreImage(image, StorePath)
        else:
            raise Exception(f"StoreImage: Empty link or path already exists: MAL_Link: {MAL_Link}, StorePath: {StorePath}.")

    def GetImage(self, Obj:Anime | Manga) -> BytesIO:
        AnimeOrManga:str = list(JsonUtil.LoadJson(Obj.Path).keys())[0].lower()
        ImagePath:str = f"./Data/{AnimeOrManga}Images/{JsonUtil.TrueName(Obj.Name)}.png"
            
        
        try:
            if not os.path.exists(ImagePath):
                raise FileNotFoundError(f"GetImage: Image not found at {ImagePath}")
            
            ImageBytes:BytesIO = JsonUtil.LoadImage(ImagePath)
            return ImageBytes
        except Exception as e:
            print("GetImage: ", e)
            raise
            
