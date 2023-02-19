# intialization
from logging import root
import random
from tkinter import *
from tkinter import ttk
from GearRandomizer import GearRandomizer


class Window(Tk):
    def __init__(self, gear_randomizer: GearRandomizer):
        
        super().__init__()

        self._gear_randomizer = gear_randomizer
        
        # Window Config
        
        # Main Window Parameters
        self.title("Destiny 2 Exotic Randomizer")
        self.geometry("550x224")

        # Number Input
        self.amount_input = Spinbox(from_=1, to=100)
        self.amount_input.pack()
        self.randomize_button = Button(width=10, height=1, text = "Randomize", command=self.on_randomizer_button_click)
        self.randomize_button.pack()

        #Randomizer Selection
        self.randomize_button_label = Label(text="Select Randomizer")
        self.randomize_button_label.pack()

        types_list = self._gear_randomizer.get_available_types()
        self.type_select_box = ttk.Combobox(values=types_list)
        self.type_select_box['state'] = 'readonly'
        self.type_select_box.current(0)
        self.type_select_box.pack()

        self.allow_duplicates = None
        self.allow_duplicates_checkbox = Checkbutton(text="Allow Duplicates?", onvalue=1, offvalue=0, variable=self.allow_duplicates)
        self.allow_duplicates_checkbox.pack()

        #Results Field
        self.Window_Results = Text(width= 30, height=10, font=("Arial", 14), wrap= "none")
        self.Window_Results['state'] = DISABLED
        self.Window_Results.pack(fill=X)

        #Results Scroll Bar
        self.Window_Results_Scroll = Scrollbar(command=self.Window_Results.yview)
        self.Window_Results.configure(yscrollcommand=self.Window_Results_Scroll.set)
        self.Window_Results_Scroll.pack(side=RIGHT, fill=Y)

    def on_randomizer_button_click(self):
        
        self.Window_Results['state'] = NORMAL
        self.Window_Results.delete("1.0", "end")
        
        amount = int(self.amount_input.get())

        randomized_suggestions = self._gear_randomizer.get_random_selection_by_type(self.type_select_box.get(), amount, self.allow_duplicates)
        
        self.Window_Results.insert(INSERT, f'{randomized_suggestions}\n')

        self.Window_Results['state'] = DISABLED


    #Sol - Writer
    #ClevQC - Sherpa
    #Futile - Help with OG code