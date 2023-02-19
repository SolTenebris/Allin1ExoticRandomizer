# intialization
from logging import root
import random
from tkinter import *
from tkinter import ttk


# opening the file in read mode
with open(r"ExoticWeaponList.txt", "r") as f:
    exotic_Weapon_list = f.read().splitlines()
with open(r"ExoticWarlockArmorList.txt", "r") as f:
    exotic_Warlock_list = f.read().splitlines()
with open(r"ExoticHunterArmorList.txt", "r") as f:
    exotic_Hunter_list = f.read().splitlines()
with open(r"ExoticTitanArmorList.txt", "r") as f:
    exotic_Titan_list = f.read().splitlines()    

#Dictionary
    
Equipment_List = {
    "Hunter":exotic_Hunter_list,
    "Titan":exotic_Titan_list,
    "Warlock":exotic_Warlock_list,
    "Weapon":exotic_Weapon_list
}

#temp printing to terminal
#print(exotic_Weapon_list)
print(len(exotic_Weapon_list))
#print(exotic_Warlock_list)
print(len(exotic_Warlock_list))
#print(exotic_Hunter_list)
print(len(exotic_Hunter_list))
#print(exotic_Titan_list)
print(len(exotic_Titan_list))


class d2ExoticRandomizer(object):
    def __init__(self):
        # Window Config

        # Main Window Parameters

        Main_Window = Tk()
        Main_Window.title("Destiny 2 Exotic Randomizer")
        Main_Window.geometry("550x224")
        Main_Window.resizable(width=False, height=False)

        # Number Input

        #Window_Input_Label = Label(Main_Window, text="Number of Rolls")
        #Window_Input_Label.place(x=0, y=5)
        self.Window_Input = Entry(Main_Window, bd=2, width=15, )
        self.Window_Input.insert(END, "Number of Rolls")
        self.Window_Input.place(x=4, y=30)
        Window_Input_Button = Button(width=10, height=1, text = "Randomize", command=self.Exotic_Randomizer)
        Window_Input_Button.place(x=6, y=56)

        #Randomizer Selection
        Window_Class_Select_Label = Label(Main_Window, text="Select Randomizer")
        Window_Class_Select_Label.place(x=4, y=81)
        self.Window_Class_Select = ttk.Combobox(Main_Window, values=['Weapon', 'Warlock', 'Hunter', 'Titan'], width= 10,)
        self.Window_Class_Select.insert(0, 'Weapon')
        self.Window_Class_Select['state'] = 'readonly'
        self.Window_Class_Select.place(x=6, y=101)
        self.Dupe_is_Checked = IntVar()
        Window_Checkbox = Checkbutton(Main_Window, text="Allow Duplicates?", onvalue=1, offvalue=0, variable=self.Dupe_is_Checked)
        Window_Checkbox.place(x=0, y=0)
        

        #Results Field
        self.Window_Results = Text(width= 30, height=10, font=("Arial", 14), wrap= "none")
        self.Window_Results.place(x=204, y=0)
        self.Window_Results['state'] = DISABLED

        #Results Scroll Bar

        Window_Results_Scroll = Scrollbar(command=self.Window_Results.yview)
        self.Window_Results.configure(yscrollcommand=Window_Results_Scroll.set)
        Window_Results_Scroll.pack(side=RIGHT, fill=Y)

        Main_Window.mainloop()

        #Randomizer Input

    def Exotic_Randomizer(self):
        self.Window_Results['state'] = NORMAL
        self.Window_Results.delete("1.0", "end")
        Input_Number = self.Window_Input.get()

        if Input_Number == 'pee pee poo poo':
            self.Window_Results.insert(INSERT, 'poo poo pee pee\n')
            return
        if Input_Number == 'sex':
            self.Window_Results.insert(INSERT, '69\n')
            return
        if Input_Number == '5318008':
            self.Window_Results.insert(INSERT, '（• ㅅ •）\n')
            return 
            
        if Input_Number.isnumeric():
            Input_Number = int(Input_Number)
        else:
            Input_Number = 1

        #Randomizer  
        List_Selection = self.Window_Class_Select.get()
        Current_Selected_List = Equipment_List[List_Selection]
        List_Length = int(len(Current_Selected_List))
        print(List_Length)
        if self.Dupe_is_Checked.get() == 1:
            for pick in range(Input_Number):
                Random_Number = random.randint(0, List_Length)
                Chosen_Weapon = Current_Selected_List[Random_Number]
                self.Window_Results.insert(INSERT, f'{Chosen_Weapon}\n')
        else:
            check_list = []
            while len(check_list) !=Input_Number:
                if Input_Number > List_Length:
                    Input_Number = List_Length
                Random_Number = random.randint(0, List_Length)
                Chosen_Weapon = Current_Selected_List[Random_Number]
                if Chosen_Weapon not in check_list:
                    check_list.append(Chosen_Weapon)
                    self.Window_Results.insert(INSERT, f'{Chosen_Weapon}\n')

        self.Window_Results['state'] = DISABLED

if __name__ == '__main__':
    d2ExoticRandomizer()


    #Sol - Writer
    #ClevQC - Sherpa
    #Futile - Help with OG code
    #peepeepoopoo