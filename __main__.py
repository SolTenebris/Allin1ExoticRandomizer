from gear_randomizer import GearRandomizer
from gui.window import Window

# Program entrypoint
if __name__ == "__main__":
    gear_randomizer = GearRandomizer('./data')
    window = Window(gear_randomizer)
    window.mainloop()