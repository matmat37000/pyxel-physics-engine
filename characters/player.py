import pyxel
from mathiol_engine.pyxel_objects import PyxelKinematicBody
from mathiol_engine.maths import Maths


class Player(PyxelKinematicBody):
    def __init__(self) -> None:
        super().__init__()
        # self.player_sprite

    def update(self) -> None:
        super().update()

        pyxel.camera(self.position.x - pyxel.width / 2, 0)
        dx, dy = 0, 0

        # if pyxel.btn(pyxel.KEY_Z):
        #     dy = -1
        # if pyxel.btn(pyxel.KEY_S):
        #     dy = 1
        if pyxel.btn(pyxel.KEY_Q):
            dx = -1
        elif pyxel.btn(pyxel.KEY_D):
            dx = 1
        if pyxel.btn(pyxel.KEY_SPACE):
            if not self.is_in_air_flags:
                self.velocity.y += 16 * Maths.GRAVITY * Maths.DELTA
                self.is_in_air_flags = True

        self.move_and_slide(dx, dy)
        self.is_colliding(self.position.x, self.position.y)

    def draw(self) -> None:
        # pyxel.rect(self.position.x, self.position.y, 8, 8, 9)
        coeff: int = pyxel.frame_count // 4 % 4
        pyxel.blt(20, 20, 0, 16 * coeff, 16, 16, 16, 0)

        pyxel.text(
            self.position.x + 1 - pyxel.width / 2, 1, f"{self.velocity=}", 6, None
        )
        pyxel.text(
            self.position.x + 1 - pyxel.width / 2,
            8,
            f"{self.is_in_air_flags=} | {pyxel.frame_count=}",
            6,
            None,
        )
        # if self.is_bonked_flags and pyxel.frame_count % 10 != 0:
        #     pyxel.text(self.position.x - 8, self.position.y - 8, "BONKED !", 9, None)
