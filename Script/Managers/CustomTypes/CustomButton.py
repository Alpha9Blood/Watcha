import tkinter as tk
from typing import Callable

class CustomButton(tk.Button):
    def UpdateOnPress(self, Func: Callable):
        self.bind('<ButtonRelease>', lambda event: self.after(500, Func))
