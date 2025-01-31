from Script.Managers.CustomTypes.CustomEntry import CustomEntry

class EntryFilterList():
    def __init__(self) -> None:
        self.AnimeList:list[CustomEntry] = []
        self.MangaList:list[CustomEntry] = []
        self.UpdateList:list[CustomEntry] = []