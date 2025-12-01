from io import BytesIO
import json
import os

class JsonUtils:

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
        json.dump(Info, open(path, "w"), indent=4)
    
    def TrueName(self, Name:str) -> str:
        """
        Returns a string with all occurrences of certain characters that cannot be used in file names replaced with '_'.
        
        Parameters:
            Name (str): The string to replace certain characters with '_'.
        
        Returns:
            str: The modified string.
        """


        CursedChars:list[str] = ["/", ":", "*", "?", "<", ">", "|", '"', "＿"]
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

    def StoreImage(self, content: bytes, path:str):
        parhdir:str = os.path.dirname(path)
        os.makedirs(parhdir, exist_ok=True)
        open(path, "wb").write(content)

    def LoadImage(self, path:str) -> BytesIO:
        return BytesIO(open(path, "rb").read())

JsonUtil = JsonUtils()


class MathUtils:

    def RoundUp(self, num, divisor):
        return -(-num // divisor)

Math = MathUtils()