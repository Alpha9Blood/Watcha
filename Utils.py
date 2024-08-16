import json
import os
class JsonUtils:
    def __init__(self):
        pass

    def CreateJson(self, content: str | list | dict, path:str):
        parhdir:str = os.path.dirname(path)
        os.makedirs(parhdir, exist_ok=True)
        json.dump(content, open(path, "w"), indent=4)
    
    def UpdateJson(self, content: str | list | dict, path:str):
        json.dump(content, open(path, "w"), indent=4)
    
    def LoadJson(self, path:str):
        return json.load(open(path))