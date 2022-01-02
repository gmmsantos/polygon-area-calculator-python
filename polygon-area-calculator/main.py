from common import rectangle, square
from unittest import main

rect = rectangle.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = square.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

# Run unit tests automatically
main(
    module="tests.test_module",
    exit=False,
)
