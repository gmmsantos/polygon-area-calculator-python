from common import rectangle, square
from unittest import main

print("Welcome to Polygon Calculator")

width = int(input("Please inform the WIDTH of the polygon: "))
height = int(input("Please inform the HEIGHT of the polygon: "))

while True:

    action = input(
        "Please, Choose one option: "
        + "\n"
        + "[1] - Set a new Width"
        + "\n"
        + "[2] - Set a new Height"
        + "\n"
        + "[3] - Calculate Area"
        + "\n"
        + "[4] - Calculate Perimeter"
        + "\n"
        + "[5] - Calculate Diagonal"
        + "\n"
        + "[6] - Display Polygon Picture"
        + "\n"
    )

    if width == height:
        sq = square.Square(width)

    rect = rectangle.Rectangle(width, height)

    if action == "1":
        w = int(input("Set the new value: "))
        rect.set_width(w)
        print(rect)
    elif action == "2":
        h = int(input("Set the new value: "))
        rect.set_height(h)
        print(rect)
    elif action == "3":
        print("\n")
        print(rect.get_area())
    elif action == "4":
        print("\n")
        print(rect.get_perimeter())
    elif action == "5":
        print("\n")
        print(rect.get_diagonal())
    elif action == "6":
        print("\n")
        print(rect.get_picture())

    new_calc = input("Would you like to choose another action? Enter 'y' or 'n' ")

    if new_calc[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks!")
        break

# Run unit tests automatically
main(
    module="tests.test_module",
    exit=False,
)
