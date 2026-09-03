from kitchen import Quantity, Converter


def grams(amount):
    return Quantity(amount, "g")


def ounces(amount):
    return Quantity(amount, "oz")


def test_multiplication():
    flour = Quantity(200)
    result = flour.times(3)
    assert result == Quantity(600)


def test_multiplication_by_two():
    flour = Quantity(200)
    result = flour.times(2)
    assert result == Quantity(400)


def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    result = flour.times(3)

    assert result is not flour


def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)


def test_grams_are_not_ounces():
    assert grams(1) != ounces(1)


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()

    assert converter.reduce(total, "g") == grams(500)