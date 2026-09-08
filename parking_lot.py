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

    def is_available(self):
        pass

class BikeParking(Parking_spot):
    def __init__(self):
        self.parking = parking

    def is_available(self):
        for i in parking:
            if parking[i]["BIKE"]>0:
                return True

        return False



class Vehicle(ABC):
    def __init__(self,owner_name,num_plate):
        self.owner_name = owner_name
        self.num_plate = num_plate

    @abstractmethod
    def get_type(self):
        pass

    def __repr__(self):
        return f"{self.get_type()} -> {self.num_plate} enters at {datetime.now()}"

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
    def __init__(self,vehicle : Vehicle):
        self.name = vehicle.owner_name
        self.num_plate = vehicle.num_plate
        self.vehicle_type = vehicle.get_type()
        self.entry_time = datetime.now()
        self.exit_time = None
        self.type = vehicle.get_type()
        self.fee = None
        self.spot = None

    def calc_fee(self):
        if self.exit_time != None:
            total_time = self.exit_time - self.entry_time 
            total_hours = total_time.total_seconds() / 3600 # convert time series to hrs 
            if self.type == "BIKE":
                return f"Total fee will be -> {total_hours*10}"

            elif self.type == "CAR":
                return f"Total fee will be -> {total_hours*20}"

            else:
                return f"Total fee will be -> {total_hours*30}"

    def exit_fun(self):
        self.exit_time =  datetime.now()

    def is_available(self):
        pass
