class Vehicle:
    _color = "White"
    def __init__(self,name,max_speed,mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity}"

class Bmw(Vehicle):
    pass

class Bus(Vehicle):
    def fare(self):
        return super().fare() + super().fare() * 10/100


SchoolBus = Bus("Volvo B1", 130, 1000,50)
SchoolBus.fare()


