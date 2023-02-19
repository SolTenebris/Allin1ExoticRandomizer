from GearRandomizer import GearRandomizer
from Window import Window

# Program entrypoint
if __name__ == "__main__":
    gear_randomizer = GearRandomizer('./data')
    window = Window(gear_randomizer)
    window.mainloop()