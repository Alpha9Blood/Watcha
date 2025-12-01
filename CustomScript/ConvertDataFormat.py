import os
import time
from Script.Utils import JsonUtil
from Script.ManageData.Anime.AnimeLists import GetAnimeList
from Script.ManageData.Manga.MangaLists import GetMangaList
from Script.ManageData.Anime.AnimeObj import Anime
from Script.ManageData.Manga.MangaObj import Manga

class ChangeDataFormat():

    def __init__(self):
        pass
        
    def OverrideAnimeDataFormat(self):
        FullList:list[str] = GetAnimeList.AnimeList()
        Selected:Anime = Anime()
        for anime in FullList:
            Selected.UpdateData(anime)
            Data:dict = {
                "Anime": {
                    "Name": Selected.Name,
                    "EpisodeStatus": Selected.EpisodeStatus, 
                    "Status": Selected.CurrentStatus,
                    "Season": Selected.Season,
                    "MaxEpisodes": Selected.MaxEpisodes,
                    "Episode": Selected.Episode,
                    "SerieName": Selected.SerieName,
                    "Score": Selected.Score,
                    "Path": Selected.Path 
                }
                
            }
            JsonUtil.UpdateJson(Data, Selected.Path)
    
    

    def MoveLinks(self):
        FullList:list[str] = GetAnimeList.AnimeList()
        MyAnimeListLinks:dict[str, str] = {}
        WatchLinks:dict[str, str] = {}
        for anime in FullList:
            if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")):
                Selected:dict[str, str] = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")["Anime"]
                if (Selected["WatchLink"]):
                    if (Selected["WatchLink"] != ""):
                        WatchLinks.update({Selected["Name"]: Selected["WatchLink"]})
                    Selected.pop("WatchLink")
                if (Selected["MyAnimeListLink"]):
                    if (Selected["MyAnimeListLink"] != ""):
                        MyAnimeListLinks.update({Selected["Name"]: Selected["MyAnimeListLink"]})
                    Selected.pop("MyAnimeListLink")

                JsonUtil.UpdateJson({"Anime": Selected}, f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")
        
        if (os.path.exists("./Data/AnimeLinks.json")):
            AnimeLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/AnimeLinks.json")
            for key in AnimeLinks:
                if (key == "MyAnimeListLink"):
                    for name in AnimeLinks[key]:
                        if (name not in AnimeLinks[key]):
                            AnimeLinks[key].update({name: AnimeLinks[key][name]})
                        elif (AnimeLinks[key][name] != ""):
                            AnimeLinks[key][name] = MyAnimeListLinks[name]
                elif (key == "WatchLinks"):
                    for name in AnimeLinks[key]:
                        if (name not in AnimeLinks[key]):
                            AnimeLinks[key].update({name: AnimeLinks[key][name]})
                        elif (AnimeLinks[key][name] != ""):
                            AnimeLinks[key][name] = WatchLinks[name]
                else:
                    raise Exception(f"Unknown key {key}")
                
            JsonUtil.UpdateJson(AnimeLinks, "./Data/AnimeLinks.json")
        else:
            JsonUtil.CreateJson({"MyAnimeListLinks": MyAnimeListLinks, "WatchLinks": WatchLinks}, "./Data/AnimeLinks.json")

        FullList = GetMangaList.MangaList()
        MyAnimeListLinks = {}
        WatchLinks = {}
        for manga in FullList:
            if (os.path.exists(f"./Data/MangaData/{JsonUtil.TrueName(manga)}.json")):
                Selected:dict[str, str] = JsonUtil.LoadJson(f"./Data/MangaData/{JsonUtil.TrueName(manga)}.json")["Manga"]
                if (Selected["MangaLink"]):
                    if (Selected["MangaLink"] != ""):
                        WatchLinks.update({Selected["Name"]: Selected["MangaLink"]})
                    Selected.pop("MangaLink")
                if (Selected["MyAnimeListLink"]):
                    if (Selected["MyAnimeListLink"] != ""):
                        MyAnimeListLinks.update({Selected["Name"]: Selected["MyAnimeListLink"]})
                    Selected.pop("MyAnimeListLink")

                JsonUtil.UpdateJson({"Manga": Selected}, f"./Data/MangaData/{JsonUtil.TrueName(manga)}.json")

        if (os.path.exists("./Data/MangaLinks.json")):
            MangaLinks:dict[str, dict[str, str]] = JsonUtil.LoadJson("./Data/MangaLinks.json")
            for key in MangaLinks:
                if (key == "MyAnimeListLink"):
                    for name in MangaLinks[key]:
                        if (name not in MangaLinks[key]):
                            MangaLinks[key].update({name: MangaLinks[key][name]})
                        elif (MangaLinks[key][name] != ""):
                            MangaLinks[key][name] = MyAnimeListLinks[name]
                elif (key == "WatchLinks"):
                    for name in MangaLinks[key]:
                        if (name not in MangaLinks[key]):
                            MangaLinks[key].update({name: MangaLinks[key][name]})
                        elif (MangaLinks[key][name] != ""):
                            MangaLinks[key][name] = WatchLinks[name]
                else:
                    raise Exception(f"Unknown key {key}")
                
            JsonUtil.UpdateJson(MangaLinks, "./Data/MangaLinks.json")
        else:
            JsonUtil.CreateJson({"MyAnimeListLinks": MyAnimeListLinks, "WatchLinks": WatchLinks}, "./Data/MangaLinks.json")
                
        
        


Exec = ChangeDataFormat()


print("Done")
time.sleep(30)