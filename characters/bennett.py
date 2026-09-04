from characters import Character

class Bennett(Character):
    def __init__(self): 
        super().__init__( "Bennett", "Pyro", 90, 191, 771, 0, 5, 50, 100, "C0" ) 

    def use_ability(self):
        print("Bennett uses Passion Overload!")

    def use_burst(self):
        print("Bennett uses Fantastic Voyage!")