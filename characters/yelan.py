from characters import Character 

class Yelan(Character):
    def __init__(self):
        super().__init__(
            "Yelan",
            "Hydro",
            90,
            244,
            548,
            0,
            5,
            50,
            100,
            "C0"
        )

    def use_ability(self):
        print("Yelan uses Lingering Lifeline!")

    def use_burst(self):
        print("Yelan uses Depth-Clarion Dice!")