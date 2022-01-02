import unittest
from common import rectangle, square


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.rect = rectangle.Rectangle(3, 6)
        self.sq = square.Square(5)

    def test_subclass(self):
        actual = issubclass(square.Square, rectangle.Rectangle)
        expected = True
        self.assertEqual(
            actual,
            expected,
            "Expected Square class to be a subclass of the Rectangle class.",
        )

    def test_distinct_classes(self):
        actual = square.Square is not rectangle.Rectangle
        expected = True
        self.assertEqual(
            actual,
            expected,
            "Expected Square class to be a distinct class from the Rectangle class.",
        )

    def test_square_is_square_and_rectangle(self):
        actual = isinstance(self.sq, square.Square) and isinstance(
            self.sq, rectangle.Rectangle
        )
        expected = True
        self.assertEqual(
            actual,
            expected,
            "Expected square object to be an instance of the Square class and the Rectangle class.",
        )

    def test_rectangle_string(self):
        actual = str(self.rect)
        expected = "Rectangle(width=3, height=6)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of rectangle to be "Rectangle(width=3, height=6)"',
        )

    def test_square_string(self):
        actual = str(self.sq)
        expected = "Square(side=5)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of square to be "Square(side=5)"',
        )

    def test_area(self):
        actual = self.rect.get_area()
        expected = 18
        self.assertEqual(actual, expected, "Expected area of rectangle to be 18")
        actual = self.sq.get_area()
        expected = 25
        self.assertEqual(actual, expected, "Expected area of square to be 25")

    def test_perimeter(self):
        actual = self.rect.get_perimeter()
        expected = 18
        self.assertEqual(actual, expected, "Expected perimeter of rectangle to be 18")
        actual = self.sq.get_perimeter()
        expected = 20
        self.assertEqual(actual, expected, "Expected perimeter of square to be 20")

    def test_diagonal(self):
        actual = self.rect.get_diagonal()
        expected = 6.708203932499369
        self.assertEqual(
            actual, expected, "Expected diagonal of rectangle to be 6.708203932499369"
        )
        actual = self.sq.get_diagonal()
        expected = 7.0710678118654755
        self.assertEqual(
            actual, expected, "Expected diagonal of square to be 7.0710678118654755"
        )

    def test_set_attributes(self):
        self.rect.set_width(7)
        self.rect.set_height(8)
        self.sq.set_side(2)
        actual = str(self.rect)
        expected = "Rectangle(width=7, height=8)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"',
        )
        actual = str(self.sq)
        expected = "Square(side=2)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of square after setting new values to be "Square(side=2)"',
        )
        self.sq.set_width(4)
        actual = str(self.sq)
        expected = "Square(side=4)"
        self.assertEqual(
            actual,
            expected,
            'Expected string representation of square after setting width to be "Square(side=4)"',
        )

    def test_rectangle_picture(self):
        self.rect.set_width(7)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "*******\n*     *\n*******\n"
        self.assertEqual(
            actual, expected, "Expected rectangle picture to be different."
        )

    def test_square_picture(self):
        self.sq.set_side(2)
        actual = self.sq.get_picture()
        expected = "**\n**\n"
        self.assertEqual(actual, expected, "Expected square picture to be different.")

    def test_big_picture(self):
        self.rect.set_width(51)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "Too big for picture. Try something smaller than 50."
        self.assertEqual(
            actual,
            expected,
            'Expected message: "Too big for picture. Try something smaller than 50."',
        )


if __name__ == "__main__":
    unittest.main()
