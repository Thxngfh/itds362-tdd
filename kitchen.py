class Quantity:
    def __init__(self, amount, unit="g"):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)

    def __eq__(self, other):
        return (
            isinstance(other, Quantity)
            and self.amount == other.amount
            and self.unit == other.unit
        )

    def __repr__(self):
        return f"Quantity({self.amount}, '{self.unit}')"


class Converter:
    def reduce(self, quantity, unit):
        return quantity.reduce(unit)


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, unit):
        return Quantity(
            self.left.amount + self.right.amount,
            unit
        )