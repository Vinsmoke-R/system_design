class Traveller():

    def __init__(self):
        self.name = ""
        self.gender = ""
        self.health = ""
        self.id = ""
        self.pwd = ""
        self.element = ""
        self.login_screen()

    def login_screen(self):
        choice = int(input("""
Press 1. to sign up
Press 2. to login
"""))
        if choice == 1:
            self.signup()
        if choice == 2:
            self.signin()

    def signup(self):
        id = input("Enter your id -> ")
        pwd = input("Enter your password -> ")
        self.id = id
        self.pwd = pwd
        print("Hello! Traveller")
        self.main_menu()

    def signin(self):
        if self.id == "":
            print("You need to signup first")
            self.login_screen()
            return
        id = input("Enter your id -> ")
        pwd = input("Enter your password -> ")
        if id == self.id and pwd == self.pwd:
            print("Welcome Traveller")
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
        elements = ["Anemo","Geo","Electro","Dendro","Hydro","Pyro","Cryo"]
        if user_input >= 1 and user_input <= 7:
            self.element = elements[user_input-1]
            print(f"Hello {self.name}! You have aquired the power of {self.element}")
        else:
            print("Please Press the right button")

baji = Traveller()
print(baji.name)
print(baji.gender)
print(baji.health)