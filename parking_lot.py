from abc import ABC, abstractmethod
from datetime import datetime
import math

vehicle_type = ["BIKE","CAR","TRUCK"]

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
    def __init__(self, vehicle: Vehicle,floors: list[list[str]]):
        self.vehicle = vehicle
        self.num_plate = vehicle.num_plate
        self.name = vehicle.owner_name
        self.floors = floors

    def is_available(self):
        vehicle_type = self.vehicle.get_type()
        if vehicle_type == "BIKE":
            for i in range(len(self.floors)):
                for j in range(0,7):
                    if self.floors[i][j]=="-":
                        print(f"There is a spot B{j+1} available for bike on floor {i+1}")
                        return i,j

        elif vehicle_type == "CAR":
            for i in range(len(self.floors)):
                for j in range(7,13):
                    if self.floors[i][j]=="-":
                        print(f"There is a spot C{j+1} available for car on floor {i+1}")
                        return i,j

        elif vehicle_type == "TRUCK":
            for i in range(len(self.floors)):
                for j in range(13,15):
                    if self.floors[i][j]=="-":
                        print(f"There is a spot T{j+1} available for Truck on floor {i+1}")
                        return i,j
        return None 

    def park(self):
        spot = self.find_available_spot()
        if spot is None:
            print("No parking spot available")
            return
        floor, position = spot

        ticket = Ticket()

        vehicle_type = self.vehicle.get_type()

        if vehicle_type == "BIKE":
            self.floors[floor][position] = "B"
        elif vehicle_type == "CAR":
            self.floors[floor][position] = "C"
        elif vehicle_type == "TRUCK":
            self.floors[floor][position] = "T"

        print(
            f"{vehicle_type} parked at position {position + 1} "
            f"on floor {floor + 1}"
        )


    def unpark(self,ticket):
        floor = ticket.spot[0]
        position = ticket.spot[1]

        self.floors[floor][position] = "-"

        ticket.exit_time = datetime.now()

        print {
            f"{ticket.vehicle.get_type()}"
            f"{ticket.vehicle.num_plate} has left the parking lot"
        }


        

class floor:
    def __init__(self,no_floors:int):
        self.no_floors = no_floors

    def parking(self):
        floors = []

        for i in range(self.no_floors):
            floors.append(["-"] * 15)
        return floors 

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
