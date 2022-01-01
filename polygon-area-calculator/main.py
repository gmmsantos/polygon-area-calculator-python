from common import rectangle, square
from unittest import main

rect = rectangle.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = square.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

# Run unit tests automatically
main(
    module="/Users/gabrielsantos/polygon-area-calculator-python/tests/test_module.py",
    exit=False,
)
