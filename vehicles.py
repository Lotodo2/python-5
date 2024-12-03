import sys

# Ensure UTF-8 encoding for proper emoji display
sys.stdout.reconfigure(encoding='utf-8')

# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Derived classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Polymorphism demonstration
def demonstrate_polymorphism(vehicles):
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__}: {vehicle.move()}")

# Main block
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()
    bicycle = Bicycle()

    vehicles = [car, plane, boat, bicycle]
    demonstrate_polymorphism(vehicles)
