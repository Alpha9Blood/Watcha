from Script.Utils import JsonUtil
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.ManageData.Manga.MangaLists import GetMangaList
from Script.ManageData.ImageExtractor import ImageControler

class ImportImages:
    
    def GetImage(self):
        AnimeList:list[str] = GetAnimeList.AnimeList()
        MangaList: list[str] = GetMangaList.MangaList()

        ImageControl:ImageControler = ImageControler()

        Selected:str = ""

        for anime in AnimeList:
            try:
                Selected = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")["Anime"]["MyAnimeListLink"]

                if (Selected != ""):
                    ImageControl.StoreExtractedImage(anime, Selected)
            except Exception as e:
                print(f"Error occurred in {anime}: {e}. Retrying...")
                AnimeList = AnimeList[AnimeList.index(anime):]
                if (len(AnimeList) == 0):
                    break
                continue

        for manga in MangaList:
            try:
                Selected = JsonUtil.LoadJson(f"./Data/MangaData/{JsonUtil.TrueName(manga)}.json")["Manga"]["MyAnimeListLink"]

                if (Selected != ""):
                    ImageControl.StoreExtractedImage(manga, Selected)
            except Exception as e:
                print(f"Error occurred in {manga}: {e}. Retrying...")
                MangaList = MangaList[MangaList.index(manga):]
                if (len(MangaList) == 0):
                    break
                continue

Exec = ImportImages()
Exec.GetImage()
