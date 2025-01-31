from tkinter import ttk
import tkinter as tk
from typing import Callable

class CustomEntry(ttk.Combobox):
    def __init__(self, master:tk.Tk, Custom:bool = False):
        self.Style()
        self.IsCustom:bool = False
        super().__init__(master)
        if (Custom):                
            self.options:list[str] = []
            self['values'] = []
            self.IsCustom = True
        else:       
            self.config(style='DefaultEntry')
        self.GetOptions:Callable[[], list[str]] = lambda: []

    def AddList(self, Options: Callable[[], list[str]], readonly: bool = False):
        self.IsCustom = True
        if (self.cget('style') != 'TCombobox'):
            self.config(style='TCombobox')
        self.GetOptions = Options
        self.UpdateOptions()
        if (readonly):
            self.Readonly()
            self.set(self.options[0])
        else:
            self.SetAutoComplete()
    
    def UpdateOptions(self):
        new_options = self.GetOptions()
        self.options:list[str] = new_options
        self["values"] = new_options
        
    def SetActiveSwitch(self, Filter: Callable):
        self.bind('<<ComboboxSelected>>', lambda event: Filter())
    
    def UpdateOnPress(self, Func: Callable):
        self.bind('<Return>', lambda event: Func())


    def SetAutoComplete(self):
        def autocomplete(event):
            current_value = self.get()
            matching_options = [option for option in self.options if current_value.lower() in option.lower()]
            self['values'] = matching_options
        self.bind("<KeyRelease>", autocomplete)
    
    def Readonly(self):
        self.state(['readonly'])

    def Style(self):
        style = ttk.Style()
        style.layout('DefaultEntry', [('Combobox.field', {'children': [('Combobox.padding', 
            {'children': [('Combobox.textarea', {'sticky': 'nswe'})], 'sticky': 'nswe'})], 'sticky': 'nswe'})])
        