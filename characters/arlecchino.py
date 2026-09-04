from characters import Character

class Arlecchino(Character):
    def __init__(self):
        super().__init__(
            "Arlecchino",
            "Pyro",
            90,
            342,
            765,
            0,
            5,
            50,
            100,
            "C0"
        )

    def use_ability(self):
        print("Arlecchino uses All Is Ash!")

    def use_burst(self):
        print("Arlecchino uses Balemoon Rising!")