from characters import Character

class Nahida(Character):
    def __init__(self):
        super().__init__("Nahida", "Dendro", 90, 9140, 718, 556, 715, 5, 50, 100, "C0")

    def use_ability(self):
        print("Nahida uses All Schemes to Know!")

    def use_burst(self):
        print("Nahida uses Illusory Heart!")