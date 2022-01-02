from common.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side) -> None:
        super().__init__(width=side, height=side)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, new_value):
        return super().__init__(new_value, new_value)
