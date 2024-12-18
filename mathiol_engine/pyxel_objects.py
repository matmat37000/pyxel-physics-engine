import pyxel

from mathiol_engine.maths import Maths


class PyxelObject:
    """
    Basic Pyxel Object
    """

    def __init__(self) -> None: ...

    def update(self) -> None:
        """
        Logic loop, called every frame
        """
        ...

    def draw(self) -> None:
        """
        Draw loop, called every frame
        """
        ...

    def __str__(self) -> str:
        return f"PyxelObject.{self.__module__}#{id(self)}"


class PyxelKinematicBody(PyxelObject):
    """
    PyxelObject with physics
    """

    def __init__(self) -> None:
        super().__init__()

        # Transform
        self.position: Maths.Vector2 = Maths.Vector2()
        self.velocity: Maths.Vector2 = Maths.Vector2()

        # Flags
        self.is_in_air_flags: bool = False
        self.is_bonked_flags: bool = False

    def __str__(self) -> str:
        return f"PyxelKinematicBody.{self.__module__}#{id(self)}"

    def update(self) -> None:
        self.is_in_air_flags = not self.is_on_floor()

    def is_colliding(self, x: float, y: float) -> bool:
        """
        Check if the player is colliding with tilemap

        Args:
            x (float): Player X coordinate
            y (float): Player Y coordinate

        Returns:
            bool: If is colliding
        """

        # Snap or x, y position to the grid of tilemap
        x1: int = pyxel.floor(x) // 8
        y1: int = pyxel.floor(y) // 8
        # Add +7 for our player hight
        x2: int = (pyxel.ceil(x) + 7) // 8
        y2: int = (pyxel.ceil(y) + 7) // 8

        for yi in range(y1, y2 + 1):
            for xi in range(x1, x2 + 1):
                # print(pyxel.tilemaps[2].pget(xi, yi))
                if pyxel.tilemaps[2].pget(xi, yi) == (2, 0):
                    return True

        return False

    def is_on_floor(self) -> bool:
        """
        Return if the body is on the floor

        Returns:
            bool: Is on the floor ?
        """
        if self.is_colliding(self.position.x, self.position.y + 0.2):
            return True
        else:
            return False

    def is_bonked(self) -> bool:
        """
        Return if the body hit the ceiling (maybe too hard)

        Returns:
            bool: BONKED ?
        """
        if self.is_colliding(self.position.x, self.position.y - 0.8):
            self.is_bonked_flags = True
            return True
        else:
            self.is_bonked_flags = False
            return False

    def move_and_slide(self, dx: float, dy: float) -> None:
        """
        Move the body in the space

        Args:
            dx (float): X Axis input movement
            dy (float): Y Axis input movement
        """

        # Update the velocity
        self.position.y += self.velocity.y

        # Check if on the ground to stop building the velocity
        if self.is_on_floor():
            self.velocity.y = 0
            # Snap the body to avoid clipping
            self.is_in_air_flags = True
            self.position.y = ((self.position.y + 1) // 8) * 8
            self.is_in_air_flags = False
        elif self.is_bonked():
            self.velocity.y *= -1
            # Snap the body to avoid clipping
            self.position.y = ((self.position.y) // 8) * 8
            self.is_in_air_flags = True
        elif not self.is_on_floor():
            # Build the velocity
            self.velocity.y -= Maths.GRAVITY * Maths.DELTA

        # Check for Y collision (if hit a tile)
        for _ in range(pyxel.ceil(abs(dy))):
            step: float = max(-1, min(1, dy))

            if self.is_colliding(self.position.x, self.position.y + step):
                break
            self.position.y += step
            dy -= step

        # Check for X collision (if hit a tile)
        for _ in range(pyxel.ceil(abs(dx))):
            step: float = max(-1, min(1, dx))

            if self.is_colliding(self.position.x + step, self.position.y):
                break
            self.position.x += step
            dx -= step
