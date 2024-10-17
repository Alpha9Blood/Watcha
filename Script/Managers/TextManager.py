import tkinter as tk
from Script.Utils import JsonUtils

JsonUtil:JsonUtils = JsonUtils()

class TextManager:

    def GuiInit(self, SetGUI):
        from AnimeGUI import SalameGUI
        self.Gui:SalameGUI = SetGUI         
        self.janela = self.Gui.janela
        self.GetList:list = [tk.Text(self.janela), tk.Scrollbar(self.janela)]

    def PresetTextPosition(self, Text:tk.Label, PositionX:int, PositionTag:int, DefaultPos:int = 0):
        CutYPos:int = ((PositionTag - 1) * 50)
        if (PositionTag == 1):
            Text.place(x=PositionX, y=DefaultPos)
            self.TextSpaceY = DefaultPos
        else:
            Text.place(x=PositionX, y=DefaultPos + self.TextSpaceY + CutYPos)

    def ResetText(self):
        if (len(self.Gui.EntryList) > 0):        
            for i in range(len(self.Gui.EntryList)):
                self.Gui.EntryList[i].delete(0, 'end')
    
    def UpdateDisplay(self):
        self.Display:tk.Text = self.GetList[0]
        self.DisplayScrollbar:tk.Scrollbar = self.GetList[1]
        
    def PrintDisplay(self, Info:dict | list | str):
        """
        Prints the given information to the display text box.

        Automatically turn the text to ident 4.

        Args:
            Info (dict | list | str): The information to be printed to the display text box.
        """
        self.UpdateDisplay()
        self.Display.place(x=550, y=150)
        self.Display.config(width=50, height=20, font=('Arial', 15), bg="gray")

        self.DisplayScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.Display.config(yscrollcommand=self.DisplayScrollbar.set)
        self.DisplayScrollbar.config(command=self.Display.yview)

        self.Display.delete(1.0, tk.END)
        self.Display.config(cursor="arrow", takefocus=True)
        self.Display.insert(tk.END, JsonUtil.TurnIndent(Info))



    
    def CreateText(self, Text:str, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):
        
        TextToCreate:tk.Label = tk.Label(self.janela)
        TextToCreate.configure(text=Text, font=('Arial', 13))
        TextToCreate.config(width=8, height=2, bg= "lightgray", border=1, relief="groove")
        if (CustomYPosition > 0):
            TextToCreate.place(x=PositionX, y=CustomYPosition)
        else:
            self.PresetTextPosition(TextToCreate, PositionX, PositionTag, DefaultPos)
        if (self.Gui.TextList.count(TextToCreate) == 0):
            self.Gui.TextList.append(TextToCreate)
