from characters import Character

class Xingqiu(Character): 
    def __init__(self): 
        super().__init__( "Xingqiu", "Hydro", 90, 202, 758, 0, 5, 50, 100, "C0" ) 

    def use_ability(self):
        print("Xingqiu uses Guhua Sword: Fatal Rainscreen!")

    def use_burst(self):
        print("Xingqiu uses Guhua Sword: Raincutter!")