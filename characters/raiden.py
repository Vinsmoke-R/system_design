from characters import Character

class Raiden(Character): 
    def __init__(self): 
        super().__init__( "Raiden", "Electro", 90, 337, 789, 0, 5, 50, 100, "C0" ) 

    def use_ability(self):
        print("Raiden uses Transcendence: Baleful Omen!")

    def use_burst(self):
        print("Raiden uses Secret Art: Musou Shinsetsu!")