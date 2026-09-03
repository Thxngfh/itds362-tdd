# kitchen.py
class Quantity:
    def __init__(self, amount):
        self.amount = amount
 
    def times(self, multiplier):
        self.amount = 600

    def times(self, multiplier):
        self.amount = self.amount * multiplier

    def times(self, multiplier):
        return Quantity(self.amount * multiplier)
