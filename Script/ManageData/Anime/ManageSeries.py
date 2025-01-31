import os
from Script.ManageData.Anime.AnimeObj import Anime
from Script.Utils import JsonUtil
class ManageSeries:
    def __init__(self):
        self.selected:Anime = Anime()

    def EditAnimeSerie(self, Name:str, NewSerieName:str):
        if (NewSerieName == ""):
            return
        
        if (os.path.exists(f"./Data/AnimeData/{JsonUtil.TrueName(Name)}.json")):
            self.selected.UpdateData(Name)
            
            if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")):
                Serie:list[str] = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")
                Series:list[str] = JsonUtil.LoadJson("./Data/ListedSeries.json")
                
                #Remove name or delete 
                if (self.selected.Name in Serie):
                    if (len(Serie) == 1):
                        os.remove(f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")
                    else:
                        Serie.pop(Serie.index(self.selected.Name))
                        JsonUtil.UpdateJson(Serie, f"./Data/SerieData/{JsonUtil.TrueName(self.selected.SerieName)}.json")     
                else:
                    print("EditAnimeSerie selected name not found in serie file.")
                
                #Update series
                if (os.path.exists(f"./Data/ListedSeries.json")):
                    if (self.selected.SerieName in Series):
                        Series.pop(Series.index(self.selected.SerieName))
                        if (NewSerieName not in Series):
                            Series.append(NewSerieName)
                            JsonUtil.UpdateJson(Series, "./Data/ListedSeries.json")
                        else:
                            print("EditAnimeSerie newname already in series")
                    else:
                        print("EditAnimeSerie selected serie name not found in series file.")
                else:
                    print("EditAnimeSerie series file not found")
                
                self.selected.SerieName = NewSerieName

                #Update or add serie
                if (os.path.exists(f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json")):
                    Serie = JsonUtil.LoadJson(f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json")
                    if (self.selected.Name not in Serie):
                        Serie.append(self.selected.Name)
                        JsonUtil.UpdateJson(Serie, f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json")
                    else:
                        print("EditAnimeSerie newname already in serie")
                else:
                    NewSerie:list[str] = [self.selected.Name]
                    JsonUtil.CreateJson(NewSerie, f"./Data/SerieData/{JsonUtil.TrueName(NewSerieName)}.json")
                
                self.selected.StoreData()
            else:
                print("EditAnimeSerie serie not found")
                return    
        else:
            print("EditAnimeSerie not found")

SerieManager:ManageSeries = ManageSeries()