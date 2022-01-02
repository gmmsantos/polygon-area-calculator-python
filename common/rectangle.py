class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, new_value):
        self.width = new_value
        return self.width

    def set_height(self, new_value):
        self.height = new_value
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        display = ""
        if (self.height > 50) or (self.width > 50):
            return "Too big for picture. Try something smaller than 50."
        for i in range(0, self.height):
            if i == 0 or i == self.height - 1:
                display += "*" * self.width + "\n"
            else:
                display += ("*" + (" " * (self.width - 2)) + "*") + "\n"
        return display

    def get_amount_inside(self, shape):
        pass
