import tkinter as tk
from Script.Utils import JsonUtil

class TextManager:

    def GuiInit(self, SetGUI):
        from WatchaGUI import WatchaGUI
        self.Gui:WatchaGUI = SetGUI         
        self.GetList:list = [tk.Text(self.Gui.window), tk.Scrollbar(self.Gui.window)]

    def PresetTextPosition(self, Text:tk.Label | tk.Text, PositionX:int, PositionTag:int, DefaultPos:int = 0):
        if (PositionTag < 1):
            raise Exception("PositionTag must be greater than 0")
        
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
        self.Gui.ImageSlot.ClearImages()
        self.Display:tk.Text = self.GetList[0]
        self.DisplayScrollbar:tk.Scrollbar = self.GetList[1]
        
    def PrintDisplay(self, Info:dict | list | str):

        self.UpdateDisplay()     
        self.Display.place(x=550, y=150)
        self.Display.config(width=50, height=20, font=('Arial', 15), bg="gray")

        self.DisplayScrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.Display.config(yscrollcommand=self.DisplayScrollbar.set)
        self.DisplayScrollbar.config(command=self.Display.yview)

        self.Display.config(cursor="arrow", takefocus=True, state="normal")
        self.Display.delete(1.0, tk.END)
        self.Display.insert(tk.END, JsonUtil.TurnIndent(Info))
        self.Display.config(state="disabled") 


    def CreateText(self, Text:str, PositionX:int, PositionTag:int = 1, DefaultPos:int = 0, CustomYPosition:int = 0, WidthHeight:tuple[int, int] = (24, 1)):
        
        TextToCreate:tk.Text = tk.Text(self.Gui.window)
        TextToCreate.insert(tk.END, Text)
        TextToCreate.config(width=WidthHeight[0], height=WidthHeight[1], bg= "lightgray", state="disabled")
        TextToCreate.bind("<Button-1>", lambda event: TextToCreate.tag_add("sel", "0.0", "end"))
        if (CustomYPosition > 0):
            TextToCreate.place(x=PositionX, y=CustomYPosition)
        else:
            self.PresetTextPosition(TextToCreate, PositionX, PositionTag, DefaultPos)
        if (TextToCreate not in self.Gui.TextList):
            self.Gui.TextList.append(TextToCreate)
        

    
    def CreateLabel(self, Text:str, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0, WidthHeight:tuple[int, int] = (8, 2)):
        
        LabelToCreate:tk.Label = tk.Label(self.Gui.window)
        LabelToCreate.configure(text=Text, font=('Arial', 13))
        LabelToCreate.config(width=WidthHeight[0], height=WidthHeight[1], bg= "lightgray", border=1, relief="groove")
        if (CustomYPosition > 0):
            LabelToCreate.place(x=PositionX, y=CustomYPosition)
        else:
            self.PresetTextPosition(LabelToCreate, PositionX, PositionTag, DefaultPos)
        if (LabelToCreate not in self.Gui.LabelList):
            self.Gui.LabelList.append(LabelToCreate)
    
    def ReplaceText(self):
        pass
