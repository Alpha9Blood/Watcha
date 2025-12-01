
class AnimeI:
    class AddAnime():
        class ButtonIndex():
            AddAnime = 0

        class EntryIndex():
            Name = 0
            MaxEp = 1
            Status = 2
            SeasonName = 3
            SeasonYear = 4
            Serie = 5
        
        class TextIndex():
            Name = 0
            MaxEp = 1
            Status = 2
            Season = 3
            Year = 4
            Serie = 5


    class SetMyAnimeListLink():  
        class ButtonIndex():
            MyAnimeListLink = 0

        class EntryIndex():
            Name = 0
            Link = 1

        class TextIndex():
            Name = 0
            Link = 1
    

    class SetWatchLink():
        class ButtonIndex():
            WatchLink = 0
        
        class EntryIndex():
            Name = 0
            Link = 1
        
        class TextIndex():
            Name = 0
            Link = 1
    
    class AddToCallendar():
        class ButtonIndex():
            AddToCallendar = 0

        class EntryIndex():
            Name = 0
            Day = 1
        
        class TextIndex():
            Name = 0
            Day = 1
    
    class DeleteAnime():
        class EntryIndex():
            Name = 0
        class ButtonIndex():
            DeleteAnime = 1
        class TextIndex():
            Name = 0
    
    class UpdateEpisode():
        class EntryIndex():
            Name = 0
            Ep = 1
        class ButtonIndex():
            AddEpisode = 0
            SetEpisode = 1
        class TextIndex():
            Title = 0
            Name = 1
    
    class UpdateScore():
        class EntryIndex():
            Name = 8
            Score = 9
        class ButtonIndex():
            UpdateScore = 3
        class TextIndex():
            Name = 8
            Score = 9

    class RemoveLeastAdded():
        class ButtonIndex():
            RemoveLeastAdded = 0

    
    class EditInfo():
        class EntryIndex():
            Name = 0
            MaxEp = 1
            Status = 2
            Serie = 3
            Score = 4
        class ButtonIndex():
            UpdateInfo = 0
        class TextIndex():
            Name = 0
            MaxEp = 1
            Status = 2
            Serie = 3
            Score = 4
    

    class OpenMyAnimeListLink():
        class ButtonIndex():
            OpenLink = 0

        class EntryIndex():
            Name = 0
            Link = 1

        class TextIndex():
            Name = 0
            Link = 1

    class OpenMyAnimeListHomePage():
        class ButtonIndex():
            OpenLink = 0

    
    class OpenWatchLink():
        class ButtonIndex():
            OpenLink = 0

        class EntryIndex():
            Name = 0
        
        class TextIndex():
            Name = 0
    
    class OpenSeasonLink():
        class ButtonIndex():
            OpenLink = 0

        class EntryIndex():
            SeasonID = 0
        
        class TextIndex():
            SeasonID = 0
    class PrintInfo():
        class ButtonIndex():
            GetInfo = 0

        class EntryIndex():
            Name = 0
        
        class TextIndex():
            Name = 0
        
        class LabelIndex():
            Image = 0
    
    class PrintSeason():
        class ButtonIndex():
            PrintSeason = 0

        class EntryIndex():
            SeasonID = 0
        
        class TextIndex():
            SeasonID = 0

    class PrintStatusList():
        class ButtonIndex():
            PrintStatusList = 0

        class EntryIndex():
            StatusID = 0
        
        class TextIndex():
            StatusID = 0

    class PrintAnimeList():
        class ButtonIndex():
            PrintList = 0
        
    class PrintSerieList():
        class ButtonIndex():
            PrintList = 0
    
    class PrintCallendar():
        class ButtonIndex():
            PrintCallendar = 0
        
        class EntryIndex():
            SeasonID = 0
        
        class TextIndex():
            SeasonID = 0
    
    class PrintSerie():
        class ButtonIndex():
            PrintSerie = 0
        
        class EntryIndex():
            SerieID = 0
        
        class TextIndex():
            SerieID = 0
    
    class ViewAllAnimes():
        class ButtonIndex():
            ViewAllAnimes = 0

class MangaI():
    class AddNewManga():
        class ButtonIndex():
            AddNewManga = 0

        class EntryIndex():
            Name = 0
            Chapter = 1
            Status = 2
        
        class TextIndex():
            Name = 0
            Chapter = 1
            Status = 2
    
    class SetLink():
        class ButtonIndex():
            SetLink = 0

        class EntryIndex():
            Name = 0
            Link = 1

        class TextIndex():
            Name = 0
            Link = 1
    
    class SetMyAnimeListLink():
        class ButtonIndex():
            AddLink = 0

        class EntryIndex():
            Name = 0
            Link = 1

        class TextIndex():
            Name = 0
            Link = 1
    
    class EditChapters():
        class ButtonIndex():
            AddChapters = 0
            SetChapters = 1

        class EntryIndex():
            Name = 0
            Chapter = 1
        
        class TextIndex():
            Name = 0
            Chapter = 1
            Title = 2
        
    class RemoveManga():
        class ButtonIndex():
            RemoveManga = 0

        class EntryIndex():
            Name = 0
        
        class TextIndex():
            Name = 0
    
    class EditInfo():
        class ButtonIndex():
            SetStatus = 0

        class EntryIndex():
            Name = 0
            Status = 1
            Score = 2
        
        class TextIndex():
            Name = 0
            Status = 1
            Score = 2
    
    class EditFavorites():
        class ButtonIndex():
            AddFavorites = 0
            DeleteFavorites = 1

        class EntryIndex():
            Name = 0
            Favorites = 2
        
        class TextIndex():
            Name = 0
            Favorites = 2
    
    class OpenLink():
        class ButtonIndex():
            OpenLink = 0

        class EntryIndex():
            Name = 0

        class TextIndex():
            Name = 0
    
    class OpenMyAnimeListLink():
        class ButtonIndex():
            OpenLink = 0
        
        class EntryIndex():
            Name = 0
        
        class TextIndex():
            Name = 0
    
    class PrintInfo():
        class ButtonIndex():
            PrintInfo = 0

        class EntryIndex():
            Name = 0
        
        class TextIndex():
            Name = 0
        
        class LabelIndex():
            Image = 0
    
    class PrintCurrentStatus():
        class ButtonIndex():
            PrintCurrentStatus = 0

        class EntryIndex():
            Status = 0
        
        class TextIndex():
            Status = 0
        
    class PrintFavorites():
        class ButtonIndex():
            PrintFavorites = 0
        
    class ViewAll():
        class ButtonIndex():
            ViewAll = 0    

class MenuI():
    class Anime():
        class ButtonIndex():
            AddInfo = 0
            EditInfo = 1
            OpenLink = 2
            ViewInfo = 3
    
        class TextIndex():
            Anime = 0
    
    class Manga():
        class ButtonIndex():
            AddInfo = 0
            EditInfo = 1
            OpenLink = 2
            ViewInfo = 3
    
        class TextIndex():
            Manga = 0

class CustomI():
    class Filter():
        class EntryIndex():
            Selected = 0
                
        class TextIndex():
            Selected = 0  
    
    class ReturnToMenu():
        class ButtonIndex():
            Menu = 0