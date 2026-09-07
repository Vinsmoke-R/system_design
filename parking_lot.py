from abc import ABC, abstractmethod
from datetime import datetime
import math

vehicle_type = ["BIKE","CAR","TRUCK"]
floors = 4 # each floor has 7 bikes 6 cars and 2 truck space = 15 
parking = {'floor_1' : {
    "BIKE" : 7,
    "CAR" : 6,
    "TRUCK" :2
},
'floor_2' : {
    "BIKE" : 7,
    "CAR" : 6,
    "TRUCK" :2
},
'floor_3' : {
    "BIKE" : 7,
    "CAR" : 6,
    "TRUCK" :2
},
'floor_4' : {
    "BIKE" : 7,
    "CAR" : 6,
    "TRUCK" :2
},
}

class ParkingLot:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.address = ""
        self.floors = []

class Parking_spot:
    def __init__(self,parking,Vehicle):
        self.parking = parking

    def is_available():
        pass

class BikeParking(Parking_spot):
    def __init__(self):
        self.parking = parking

    def is_available():
        for i in parking:
            if parking[i]["BIKE"]>0:
                return True

        return False



class Vehicle:
    def __init__(self):
        self.owner_name = ""
        self.num_plate = ""

    @abstractmethod
    def get_type(self):
        pass

class Bike(Vehicle):
    def get_type(self):
        return "BIKE"

class Car(Vehicle):
    def get_type(self):
        return "CAR"

class Truck(Vehicle):
    def get_type(self):
        return "TRUCK"


class Ticket():
    def __init__(self,Vehicle):
        self.name = Vehicle.name
        self.num_plate = Vehicle.num_plate
        self.vehicle_type = Vehicle.get_type()
        self.entry_time = datetime.now
        self.exit_time = None
        self.type = self.get_type()
        self.fee = None
        self.spot = None

    def calc_fee(self):
        if self.type == "BIKE":
            pass

        elif self.type == "CAR":
            pass

        else:
            pass
