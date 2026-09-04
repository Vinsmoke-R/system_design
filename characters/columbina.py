from characters import Character

class Columbina(Character): 
    def __init__(self): 
        super().__init__( "Columbina", "Hydro", 90, 96, 515, 0, 5, 50, 100, "C0" ) 

    def use_ability(self):
        print("Columbina uses Eternal Tides!")

    def use_burst(self):
        print("Columbina uses Moonlit Melancholy!")