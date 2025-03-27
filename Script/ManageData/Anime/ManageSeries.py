import os
from Script.ManageData.Anime.AnimeObj import Anime
from Script.Utils import JsonUtil
class ManageSeries:
    def __init__(self):
        self.selected:Anime = Anime()

    def EditAnimeSerie(self, Name:str, NewSerieName:str):
        if (NewSerieName == ""):
            print("EditAnimeSerie NewSerieName is empty")
            return
        
        if (not os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            print(f"EditAnimeSerie: {Name = } path not found")
            return
        
        self.selected.UpdateData(Name)
        
        if (not os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")):
            print("EditAnimeSerie serie not found")
            return
        
        if (not os.path.exists("./Data/ListedSeries.json")):
            print("EditAnimeSerie series file not found")
            return
        
        Serie:list[str] = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")
        Series:list[str] = JsonUtil.LoadJson("./Data/ListedSeries.json")

        if (NewSerieName in Series):
            print("EditAnimeSerie newname already in series")
            return
        
        #Remove name or delete 
        
        if (self.selected.Name in Serie):   
            if (len(Serie) == 1):
                os.remove(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")       
                Series.pop(Series.index(self.selected.SerieName))
            else:
                Serie.pop(Serie.index(self.selected.Name))
                JsonUtil.UpdateJson(Serie, f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")
        else:
            print(f"EditAnimeSerie selected {self.selected.Name = } not found in serie file: {Serie}.")
        
        #Update series

        Series.append(NewSerieName)
        JsonUtil.UpdateJson(Series, "./Data/ListedSeries.json")
   
        self.selected.SerieName = NewSerieName

        #Update or add serie
        if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json")):
            Serie = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json")
            if (self.selected.Name not in Serie):
                Serie.append(self.selected.Name)
                JsonUtil.UpdateJson(Serie, f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json")
            else:
                print(f"EditAnimeSerie {NewSerieName = } already in {Serie = }")
        else:
            NewSerie:list[str] = [self.selected.Name]
            JsonUtil.CreateJson(NewSerie, f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json") 
        
        self.selected.StoreData()

SerieManager:ManageSeries = ManageSeries()