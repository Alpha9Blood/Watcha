
class AnimeSet:
    class EntryIndex(int):

        class AddAnime(int):
            Name = 0
            MaxEp = 1
            Status = 2
            Season = 3
            Serie = 4
        class DeleteAnime(int):
            Name = 5
        class AddEpisode(int):
            Name = 6
            Ep = 7
        class UpdateNota(int):
            Name = 8
            Nota = 9
        class SetCurrentStatus(int):
            Name = 10
            Status = 11
        class MyAnimeListLink(int):
            Name = 12
            Link = 13
        class AddToCallendar(int):
            Name = 14
            Day = 15

    class TextIndex(int):
        class AddAnime(int):
            Name = 0
            MaxEp = 1
            Status = 2
            Season = 3
            Serie = 4
        class DeleteAnime(int):
            Name = 5
        class AddEpisode(int):
            AddEpisode = 6
            Name = 7
        class UpdateNota(int):
            Name = 8
        class SetCurrentStatus(int):
            Name = 9
            SetStatus = 10
        class MyAnimeListLink(int):
            Name = 11
            Link = 12
        class AddToCallendar(int):
            Name = 13
            Day = 14

    class ButtonIndex(int):
        AddAnime = 0
        DeleteAnime = 1
        AddEp = 2
        SetEp = 3
        UpdateNota = 4
        RemoveLeastAdded = 5
        SetCurrentStatus = 6
        SetMyAnimeListLink = 7
        AddToCallendar = 8

class AnimeGet:
    class EntryIndex(int):
        class GetStatus(int):
            Name = 0
        class PrintSeason(int):
            SeasonID = 1     
        class PrintStatusList(int):
            StatusID = 2
        class OpenLink(int):
            Name = 3
        class PrintSerie(int):
            Name = 4
        class PrintCallendar(int):
            SeasonID = 5

    class TextIndex(int):
        class GetStatus(int):
            Name = 0
        class PrintSeason(int):
            SeasonID = 1     
        class PrintStatusList(int):
            StatusID = 2
        class OpenLink(int):
            Name = 3
        class PrintSerie(int):
            Name = 4
        class PrintCallendar(int):
            SeasonID = 5
    
    class ButtonIndex(int):
        GetStatus = 0
        PrintSeason = 1
        PrintStatusList = 2
        OpenLink = 3
        PrintSerie = 4
        PrintAnimeList = 5
        PrintSerieList = 6
        OpenMyAnimeList = 7
        PrintCallendar = 8

