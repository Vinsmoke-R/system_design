# creating a class 
class car: 
    # special method 
    def __init__(self):
        print("Creating an object")
        self.id = 123
        self.color = "White"
        self.wheels = 4
        print("Object is created")

    def travel(self):
        print(f"This car is ready to travel")

# creating an object 
tesla = car()
audi = car()

# both will have same id (we can overwrite by creating tesla and audi class seperately)
print(tesla.id)
print(audi.id)