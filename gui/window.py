# intialization
from tkinter import *
from tkinter import ttk
from gear_randomizer import GearRandomizer
from gui.controls_frame import ControlsFrame
from gui.result_display import ResultsDisplay


class Window(Tk):
    def __init__(self, gear_randomizer: GearRandomizer):
        
        super().__init__()

        self._gear_randomizer = gear_randomizer

        # Window metadata
        self.title("Destiny 2 Exotic Randomizer")
        self.geometry("550x224")

        # Setting the control panel on the left side of the window
        self._controls_frame = ControlsFrame(self, self._on_randomizer_button_click, gear_randomizer.get_available_types())
        self._controls_frame.pack(side=LEFT)

        # Setting the display panel on the right side of the window
        self._results_display = ResultsDisplay()
        self._results_display.pack(side=RIGHT)

    def _on_randomizer_button_click(self):
        
        selected_type = self._controls_frame.get_selected_type()
        amount_to_generate = self._controls_frame.get_amount_to_generate()
        duplicates_allowed = self._controls_frame.is_duplicates_allowed_checked()

        randomized_suggestions = self._gear_randomizer.get_random_selection_by_type(selected_type, int(amount_to_generate), duplicates_allowed)
        
        self._results_display.override_display("\n".join(randomized_suggestions))


    #Sol - Writer
    #ClevQC - Sherpa
    #Futile - Help with OG code