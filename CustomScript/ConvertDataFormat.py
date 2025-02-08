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
                    "MyAnimeListLink": Selected.MyAnimeListLink,
                    "WatchLink": Selected.WatchLink, 
                    "Score": Selected.Score,
                    "Path": Selected.Path 
                }
                
            }
            JsonUtil.UpdateJson(Data, Selected.Path)
    
    def FixAnimeWatchLink(self):
        FullList:list[str] = GetAnimeList.AnimeList()
        SelectedAnime:dict = {}
        SelectedUpdate = {}
        for anime in FullList:
            SelectedAnime = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")
            if ("WatchLink" in SelectedAnime):
                SelectedUpdate = SelectedAnime["WatchLink"]
                SelectedAnime["Anime"]["WatchLink"] = SelectedUpdate
                SelectedAnime.pop("WatchLink")
                JsonUtil.UpdateJson(SelectedAnime, f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")

    def FixAnimeEpisodeStatus(self):
        FullList:list[str] = GetAnimeList.AnimeList()
        SelectedAnime:dict = {}
        for anime in FullList:
            SelectedAnime = JsonUtil.LoadJson(f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")["Anime"]
            if ("EpisodesStatus" in SelectedAnime):
                print(f"FixEpisodeStatus {SelectedAnime['Name']}")
                NewFormat:dict[str, dict] = {
                    "Anime": {
                        "Name": SelectedAnime["Name"],
                        "EpisodeStatus": SelectedAnime["EpisodesStatus"],
                        "Status": SelectedAnime["Status"],
                        "Season": SelectedAnime["Season"],
                        "MaxEpisodes": SelectedAnime["MaxEpisodes"],
                        "Episode": SelectedAnime["Episode"],
                        "SerieName": SelectedAnime["SerieName"],
                        "MyAnimeListLink": SelectedAnime["MyAnimeListLink"],
                        "WatchLink": SelectedAnime["WatchLink"],
                        "Score": SelectedAnime["Score"]
                    }
                }
                JsonUtil.UpdateJson(NewFormat, f"./Data/AnimeData/{JsonUtil.TrueName(anime)}.json")
    
    def FixAnimeFormat(self):
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
                    "MyAnimeListLink": Selected.MyAnimeListLink,
                    "WatchLink": Selected.WatchLink, 
                    "Score": Selected.Score,
                    "Path": Selected.Path 
                }
                
            }
            JsonUtil.UpdateJson(Data, Selected.Path)

    def AddMALToManga(self):
        FullList:list[str] = GetMangaList.MangaList()
        Selected:Manga = Manga()
        for manga in FullList:
            Selected.UpdateData(manga)
            Data:dict = {
                "Manga": {
                    "Name": Selected.Name,
                    "Chapters": Selected.Chapters,
                    "Status": Selected.Status,
                    "LeastTimeUpdated": Selected.LeastTimeUpdated,
                    "MyAnimeListLink": "",
                    "MangaLink": Selected.MangaLink,
                    "Score": Selected.Score
                }
            }
                
            JsonUtil.UpdateJson(Data, Selected.Path)
                
        
        


Exec = ChangeDataFormat()