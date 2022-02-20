# Represents the dimension Length for Dimension Analysis

class Length:
    def __init__(self, quantity):
        self.quantity = quantity

    def area(self):
        return self.quantity*2

    def volume(self):
        return self.quantity*3

    def speed(self, time):
        return self.quantity/time

    def acceleration(self, time):
        return self.quantity/(time**2)

