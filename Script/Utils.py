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
    
    def TurnIndent(self, content: str | list | dict) -> str:
        return json.dumps(content, indent=4)
    
    def AddToDictJson(self, content: dict, path:str):
        Info:dict = json.load(open(path))
        Info.update(content)
        json.dump(Info, open(path, "a"), indent=4)
    
    def TrueName(self, Name:str) -> str:
        """
        Returns a string with all occurrences of ':' replaced with '_'.
        
        Parameters:
            Name (str): The string to replace ':' with '_'.
        
        Returns:
            str: The modified string.
        """


        CursedChars:list[str] = ["/", ":", "*", "?", "<", ">", "|", "!", "'", '"']
        for curse in CursedChars:
            if (curse in Name):
                Name = Name.replace(curse, "_")
        return Name

    def CursedStoreName(self, Name:str) -> str:
        CursedList:list[str] = ["’"]
        
        for curse in CursedList:
            if (curse in Name):
                Name = Name.replace(curse, "_")

        return Name

JsonUtil = JsonUtils()