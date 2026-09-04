from characters import Character

class Flins(Character): 
    def __init__(self): 
        super().__init__( "Flins", "Electro", 90, 351.59, 808.52, 0, 5, 50, 100, "C0" ) 

    def use_ability(self):
        print("Flins uses Ancient Rite: Arcane Light!")

    def use_burst(self):
        print("Flins uses Ancient Ritual: Cometh the Night!")