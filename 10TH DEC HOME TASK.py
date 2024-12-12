class Vehicle: 
    def __init__(self, make, model, year): 
        self.make = make 
        self.model = model 
        self.year = year 
    def display(self): 
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}") 
class Car(Vehicle): 
    def __init__(self, make, model, year, doors, trunk_capacity): 
        Vehicle.__init__(self, make, model, year)   
        self.doors = doors 
        self.trunk_capacity = trunk_capacity
    def display(self): 
        Vehicle.display(self)   
        print(f"Doors: {self.doors}, Trunk Capacity: {self.trunk_capacity}") 
class Truck(Vehicle): 
    def __init__(self, make, model, year, cargo_capacity, axles): 
        Vehicle.__init__(self, make, model, year)   
        self.cargo_capacity = cargo_capacity 
        self.axles = axles 
    def display(self): 
        Vehicle.display(self)   
        print(f"Cargo Capacity: {self.cargo_capacity} tons, Axles: {self.axles}") 
class PickupTruck(Car, Truck): 
    def __init__(self, make, model, year, doors, trunk_capacity, cargo_capacity, axles): 
        Vehicle.__init__(self, make, model, year)   
        self.doors = doors 
        self.trunk_capacity = trunk_capacity 
        self.cargo_capacity = cargo_capacity 
        self.axles = axles 
    def display(self): 
        Vehicle.display(self)   
        print(f"Doors: {self.doors}, Trunk Capacity: {self.trunk_capacity}") 
        print(f"Cargo Capacity: {self.cargo_capacity} tons, Axles: {self.axles}") 
 
pickup_truck = PickupTruck("Ford", "F-150", 2022, 4, 14.0, 1.5, 2) 
pickup_truck.display()
