class Traveller():

    def __init__(self):
        self.name = ""
        self.gender = ""
        self.health = ""
        self.main_menu()

    def main_menu(self):
        name = input("Enter your name -> ")
        self.name = name

        gender = int(input("""
        Pick your Character
        Press 1 for Aether
        Press 2 for Lumine
                        """))
        if(gender==1):
            self.gender = "Male"
        if(gender==2):
            self.gender = "Female"

        user_input = int(input("""
        Hello Traveller! Welcome to Teyvat 
        Choose your powers
        1 - Anemo — power of wind
        2 - Geo — power of earth
        3 - Electro — power of lightning
        4 - Dendro — power of nature
        5 - Hydro — power of water
        6 - Pyro — power of fire
        7 - Cryo — power of ice
                                        """))

        if user_input == 1:
            pass
        if user_input == 2:
            pass
        if user_input == 3:
            pass
        if user_input == 4:
            pass
        if user_input == 5:
            pass
        if user_input == 6:
            pass
        if user_input == 7:
            pass
        else : 
            exit

baji = Traveller()
print(baji.name)
print(baji.gender)
print(baji.health)