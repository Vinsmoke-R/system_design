from characters import Character

class Nefer(Character): 
    def __init__(self): 
        super().__init__( "Nefer", "Dendro", 90, 344, 799, 100, 5, 50, 100, "C0" ) 

    def use_ability(self):
        print("Nefer uses Senet Strategy: Dance of a Thousand Nights!")

    def use_burst(self):
        print("Nefer uses Sacred Vow: True Eye's Phantasm!")