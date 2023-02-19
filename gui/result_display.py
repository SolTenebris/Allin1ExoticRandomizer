from tkinter import *

class ResultsDisplay(Frame):

    def __init__(self):
        
        super().__init__()

        self._randomizer_results_display = Text(width= 30, height=10, font=("Arial", 14), wrap= "none")
        self._randomizer_results_display['state'] = DISABLED
        self._randomizer_results_display.pack(side=RIGHT, fill=BOTH)

        #self._randomizer_results_display.configure(yscrollcommand=self.Window_Results_Scroll.set)
        
        Window_Results_Scroll = Scrollbar(command=self._randomizer_results_display.yview)
        #Window_Results_Scroll.pack(side=RIGHT, fill=Y)
    
    def override_display(self, results):
        
        self.clear_display()
        self._randomizer_results_display.insert(INSERT, results)
        self._lock_display()

    
    def clear_display(self):
        self._randomizer_results_display['state'] = NORMAL
        self._randomizer_results_display.delete("1.0", "end")
    
    def _lock_display(self):
        self._randomizer_results_display['state'] = DISABLED