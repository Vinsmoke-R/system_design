from abc import ABC, abstractmethod
from datetime import datetime
import math

vehicle_type = ["BIKE","CAR","TRUCK"]
floors = 4 # each floor has 7 bikes 6 cars and 2 truck space = 15 
floors = 4

class Vehicle(ABC):
    def __init__(self,owner_name,num_plate):
        self.owner_name = owner_name
        self.num_plate = num_plate

    @abstractmethod    
    def get_type(self):    # this function can't be called by Vehicle class
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


class ParkingLot:
    def __init__(self, vehicle: Vehicle,floors: list[list[str]], no_floors:int):
        self.vehicle = vehicle
        self.num_plate = vehicle.num_plate
        self.name = vehicle.owner_name

    def is_available(self,floors):
        type = self.vehicle.get_type()
        if type=="BIKE":
            for i in floors:
                for j in range(0,7):
                    if floors[i][j]=="-":
                        print(f"There is a spot B{j+1} available for bike on floor {i+1}")
                        return True

        elif type == "CAR":
            for i in floors:
                for j in range(7,13):
                    if floors[i][j]=="-":
                        print(f"There is a spot C{j+1} available for car on floor {i+1}")
                        return True

        elif type == "TRUCK":
            for i in floors:
                for j in range(13,16):
                    if floors[i][j]=="-":
                        print(f"There is a spot T{j+1} available for Truck on floor {i+1}")
                        return True
        return False
    
            

    def park(self,):
        pass

    def unpark(self):
        pass

class Parking_spot:
    def __init__(self,parking):
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
