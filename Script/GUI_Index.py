
class AnimeSet:
    class EntryIndex():

        class AddAnime():
            Name = 5
            MaxEp = 4
            Status = 2
            Season = 3
            Serie = 4
        class DeleteAnime():
            Name = 5
        class AddEpisode():
            Name = 6
            Ep = 7
        class UpdateScore():
            Name = 8
            Score = 9
        class SetCurrentStatus():
            Name = 10
            Status = 11
        class MyAnimeListLink():
            Name = 12
            Link = 13
        class AddToCallendar():
            Name = 14
            Day = 15
        class SetSeasonLink():
            SeasonID = 16
            Link = 17
        

    class TextIndex():
        class AddAnime():
            Name = 0
            MaxEp = 1
            Status = 2
            Season = 3
            Serie = 4
        class DeleteAnime():
            Name = 5
        class AddEpisode():
            Title = 6
            Name = 7
        class UpdateScore():
            Name = 8
        class SetCurrentStatus():
            Name = 9
            SetStatus = 10
        class MyAnimeListLink():
            Name = 11
            Link = 12
        class AddToCallendar():
            Name = 13
            Day = 14
        class SetSeasonLink():
            SeasonID = 15

    class ButtonIndex():
        AddAnime = 0
        DeleteAnime = 1
        AddEpisode = 2
        SetEpisode = 3
        UpdateScore = 4
        RemoveLeastAdded = 5
        SetCurrentStatus = 6
        SetMyAnimeListLink = 7
        AddToCallendar = 8
        SetSeasonLink = 9

class AnimeGet:
    class EntryIndex():
        class GetStatus():
            Name = 0
        class PrintSeason():
            SeasonID = 1     
        class PrintStatusList():
            StatusID = 2
        class OpenLink():
            Name = 3
        class PrintSerie():
            SerieID = 4
        class PrintCallendar():
            SeasonID = 5
        class OpenSeasonLink():
            SeasonID = 6
        class FilterOptions():
            Selected = 7

    class TextIndex():
        class GetStatus():
            StatusID = 0
        class PrintSeason():
            SeasonID = 1     
        class PrintStatusList():
            StatusID = 2
        class OpenLink():
            Name = 3
        class PrintSerie():
            SerieID = 4
        class PrintCallendar():
            SeasonID = 5
        class OpenSeasonLink():
            SeasonID = 6
        class Filter():
            Selected = 7
    
    class ButtonIndex():
        GetStatus = 0
        PrintSeason = 1
        PrintStatusList = 2
        OpenLink = 3
        PrintSerie = 4
        PrintAnimeList = 5
        PrintSerieList = 6
        OpenMyAnimeList = 7
        PrintCallendar = 8
        OpenSeasonLink = 9

class MangaSet():
    class EntryIndex():
        class AddNewManga():
            Name = 0
            Chapters = 1
            Status = 2
        class DeleteManga():
            Name = 3
        class SetStatus():
            Name = 4
            Status = 5
        class SetLink():
            Name = 6
            Link = 7
        class EditFavorites():
            Name = 8
        class UpdateChapters():
            Name = 8
            Chapters = 9
        
        class EditScore():
            Name = 10
            Score = 11

    class TextIndex():
        class AddNewManga():
            Name = 0
            Chapters = 1
            Status = 2
        class DeleteManga():
            Name = 3
        class SetStatus():
            Name = 4
            Status = 5
        class SetLink():
            Name = 6
            Link = 7
        class EditFavorites():
            Name = 8
        class UpdateChapters():
            Name = 8
            Title = 9
        
        class EditScore():
            Name = 10
        
    class ButtonIndex():
        AddNewManga = 0
        DeleteManga = 1
        SetStatus = 2
        SetLink = 3
        AddFavorite = 4
        DeleteFavorite = 5
        AddChapters = 6
        SetChapters = 7
        EditScore = 8

class MangaGet():
    class EntryIndex():
        class PrintManga():
            Name = 0
        class PrintCurrentStatus():
            Status = 1
        class OpenLink():
            Name = 2

    class TextIndex():
        class PrintManga():
            Name = 0
        class PrintCurrentStatus():
            Status = 1
        class OpenLink():
            Name = 2

    class ButtonIndex():
        PrintManga = 0
        PrintCurrentStatus = 1
        OpenLink = 2
        PrintFavorites = 3
