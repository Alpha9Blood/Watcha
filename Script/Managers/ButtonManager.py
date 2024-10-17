import tkinter as tk
from Script.Managers.CustomTypes.CustomButton import CustomButton

class ButtonManager():

        def GuiInit(self, SetGUI):
            from AnimeGUI import SalameGUI
            self.Gui:SalameGUI = SetGUI
            self.janela = self.Gui.janela
        
        def PresetButPosition(self,But:tk.Button, PositionX:int, PositionTag:int, DefaultPos:int = 0):
            CutYPos:int = ((PositionTag - 1) * 50)
            if (PositionTag == 1):
                But.place(x=PositionX, y=DefaultPos)
                self.ButSpaceY = DefaultPos
            else:
                But.place(x=PositionX, y=DefaultPos + self.ButSpaceY + CutYPos)

        def CreateBut(self, Name:str, Function, PositionX:int, PositionTag:int, DefaultPos:int = 0, CustomYPosition:int = 0):

            ButToCreate:tk.Button = CustomButton(self.janela)
            ButToCreate.configure(text=Name, font=('Arial', 14), command=Function)
            ButToCreate.config(width=10, height=2, bg= "red", border=1, relief="groove")
            if (CustomYPosition > 0):
                ButToCreate.place(x=PositionX, y=CustomYPosition)
            else:
                self.PresetButPosition(ButToCreate, PositionX, PositionTag, DefaultPos)
            if (self.Gui.ButList.count(ButToCreate) == 0):
                self.Gui.ButList.append(ButToCreate)