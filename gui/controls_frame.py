from tkinter import Frame, Label, Spinbox, ttk, IntVar, Checkbutton, Button, BOTTOM, Tk

from gear_randomizer import GearRandomizer

class ControlsFrame(Frame):

    def __init__(self, parent: Tk, on_randomizer_button_clicked: callable, types: list):
        
        super().__init__(master=parent)

        amount_input_label = Label(self, text="Amount to generate:")
        self._amount_input_box = Spinbox(master=self, from_=1, to=100)
        amount_input_label.pack()
        self._amount_input_box.pack()

        #Randomizer Selection
        randomize_button_label = Label(master=self, text="Select Randomizer")
        randomize_button_label.pack()

        self._type_select_box = ttk.Combobox(master=self, values=types)
        self._type_select_box['state'] = 'readonly'
        self._type_select_box.current(0)
        self._type_select_box.pack()

        self._allow_duplicates = IntVar()
        
        allow_duplicates_checkbox = Checkbutton(master=self, text="Allow Duplicates?", onvalue=1, offvalue=0, variable=self._allow_duplicates)
        allow_duplicates_checkbox.pack()

        randomize_button = Button(master=self, width=10, height=1, text = "Randomize", command=on_randomizer_button_clicked)
        randomize_button.pack(side=BOTTOM)

    def is_duplicates_allowed_checked(self) -> bool:
        return self._allow_duplicates

    def get_selected_type(self) -> str:
        return self._type_select_box.get()

    def get_amount_to_generate(self) -> int:
        return self._amount_input_box.get()
