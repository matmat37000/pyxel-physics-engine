class Maths:
    GRAVITY: float = -9.8

    DELTA: float = 1 / 60

    class Vector2:
        """
        Simple Vector 2D
        """

        def __init__(self, x: float = 0, y: float = 0) -> None:
            self.x: float = x
            self.y: float = y

        def __eq__(self, value: object) -> bool:
            if type(value) is type(self):
                return value.x == self.x and value.y == self.y
            else:
                return False

        def __bool__(self) -> bool:
            if self.x != 0 and self.y != 0:
                return True
            else:
                return False

        def __mul__(self, value: object):
            if type(value) is type(self):
                return (value.x * self.x) + (value.y * self.y)

            elif type(value) is float or type(value) is int:
                return Maths.Vector2(self.x * value, self.y * value)
            else:
                raise ValueError(f"Can't multiply {type(value)} and {type(self)}")

        def __add__(self, value: object):
            if type(value) is type(self):
                return Maths.Vector2(self.x + value.x, self.y + value.y)
            else:
                raise ValueError(f"Can't add {type(value)} and {type(self)}")

        def __sub__(self, value: object):
            if type(value) is type(self):
                return Maths.Vector2(self.x - value.x, self.y - value.y)
            else:
                raise ValueError(f"Can't add {type(value)} and {type(self)}")

        def __str__(self) -> str:
            return f"Vector2({self.x}, {self.y})"

        def __repr__(self) -> str:
            return f"Vector2({self.x}, {self.y})"

        def __getitem__(self, index: int):
            if index == 0:
                return self.x
            elif index == 1:
                return self.y
            else:
                raise IndexError(f"Index out of range, expected 0 or 1, got {index}.")


if __name__ == "__main__":
    a = Maths.Vector2(4, 8)
    b = Maths.Vector2(5, 2)
    c = a + b
    print(c[0])
    print(c[1])
    print(c[3])
