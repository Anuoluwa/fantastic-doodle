"""
OOP = modeling object 
"""

""" 
Challenge
Use the planning strategy and process demonstrated above to design a parking lot. This is a common OOP interview question and the time you spend thoughtfully thinking through this problem will be helpful.

As you design your solution, and think through all of the necessary objects, attributes, methods, and relationships, keep the following in mind:

Payments
What methods are allowed?
Where do customers pay?
Capacity
How does the system respond when the lot is full?
How does the system know when the lot is full?
Vehicles
Is capacity allocated differently depending on what type of vehicle enters the lot? How so?
Pricing
Are there different rates for different times of day? How will this be handled?
Is there a discount for purchasing a longer total time?

++++++++
Nouns(Classes) : User, Payments, Capacity, Vehicles, Pricing
Adverbs(Attributes):  
Payments
    vehicles details()
    channels: cash, card, e-transfer
    amount: 

Capacity:
    total_lots
    entry_time
    exit_time

Vehicles:
    VIN
    color
    license
    brand
    Type
Pricing:
    duration:
    price_per_durations:
    Capacity()

Methods:
Vehicles:
    drive_in
    drive_out
Relationships
vehicle car 


"""

from datetime import datetime

class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Staff(User):
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.pricing = Pricing.rate_per_min * (Capacity.entry_time - Capacity.exit_time)
        self.channel = ['Card', 'Cash']
    
    def create_park_lot(self,  total_lots):
        capacity = Capacity(total_lots, self, self)


    def get_vehicle_details(self, license, color, maker, brand):
        vehicle = Vehicle(self, license, color, maker, brand)

class Driver(User):
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.park_lot = Capacity.total_lots - 1

    def park(self, lot_number,  capacity):
        lot_number = Capacity.total_lots [-1]


class Capacity:
    def __init__(self, total_lots, entry_time, exit_time):
        self.total_lots = total_lots
        self.entry_time = datetime.now()
        self.exit_time = datetime.now()

class Vehicle:
    def __init__(self, license, color, maker, brand):
        self.license = license
        self.color = color
        self.maker = maker
        self.brand = brand

class Pricing:
    def  __init__(self, rate_per_min):
        self.rate_per_min = rate_per_min


class Payment:
    def __init__(self, channel):
        self.channel = channel
