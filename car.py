class Vehicle:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"This vehicle is {self.color}"

class Car(Vehicle):
    def __init__(self, color, has_winter_tires=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires

    def __str__(self):
        vehicle_str = super().__str__()
        return f"{vehicle_str}\nHas winter tires: {self.has_winter_tires}"

my_car = Car("blue", True)
print(my_car.getColor())  
print(my_car)             
