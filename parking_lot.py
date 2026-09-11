from abc import ABC, abstractmethod
from datetime import datetime
import math
import time 

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
    def __init__(self,floors):
        self.floors = floors
        self.tickets = {}

    def is_available(self,vehicle : Vehicle):
        vehicle_type = vehicle.get_type()
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

    def park(self,vehicle : Vehicle):
        spot = self.is_available(vehicle)
        if spot is None:
            print("No parking spot available")
            return
        floor, position = spot

        ticket = Ticket(vehicle)
        ticket.spot = spot 

        self.tickets[vehicle.num_plate] = ticket   # ← add to register
    
        self.floors[floor][position] = vehicle.get_type()[0]  # "B", "C", "T"
        
        print(f"{vehicle.get_type()} parked at spot {position+1}, floor {floor+1}")
        return ticket


    def unpark(self, num_plate: str):            # ← take num_plate instead of ticket
        ticket = self.tickets.pop(num_plate, None)  # ← remove from register + get ticket
        
        if ticket is None:
            print("Ticket not found!")
            return
        
        floor, position = ticket.spot
        self.floors[floor][position] = "-"       # ← free the spot
        
        ticket.exit_time = datetime.now()        # ← set exit time
        print(ticket.calc_fee())                 # ← calculate and show fee


class Floor:
    def __init__(self,no_floors:int):
        self.no_floors = no_floors

    def create(self):
        floors = []

        for i in range(self.no_floors):
            floors.append(["-"] * 15)
        return floors 


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
                self.fee = round(total_hours*10,2)
                return f"Total fee will be -> {self.fee}"

            elif self.type == "CAR":
                self.fee = round(total_hours*20,2)
                return f"Total fee will be -> {self.fee}"

            else:
                self.fee = round(total_hours*30,2)
                return f"Total fee will be -> {self.fee}"



floors = Floor(4).create()
lot = ParkingLot(floors)

car = Car("RAJ","UP79X6626")
bike = Bike("AMAN","UP79X1124")

lot.park(car)
lot.park(bike)

time.sleep(10)

lot.unpark("UP79X6626")
lot.unpark("UP79X1124")