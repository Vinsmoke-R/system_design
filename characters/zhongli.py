from characters import Character

class Zhongli(Character): 
    def __init__(self): 
        super().__init__( "Zhongli", "Geo", 90, 251, 738, 0, 5, 50, 100, "C0" ) 

    def use_ability(self):
        print("Zhongli uses Dominus Lapidis!")

    def use_burst(self):
        print("Zhongli uses Planet Befall!")