import pyxel
from mathiol_engine.pyxel_objects import PyxelKinematicBody
from mathiol_engine.maths import Maths


class Player(PyxelKinematicBody):
    """
    Player object
    """

    def __init__(self) -> None:
        super().__init__()

        self.object_height = 16
        self.object_width = 8
        self.sprite_offset_x = 4
        self.object_weight = 4
        self.jump_strength: int = 26

        # Flags
        self.is_walking_flags: bool = False

        # In format (offset, frame_count)
        self.sprites_sheet: dict[str, tuple[int, int]] = {
            "IDLE": (32, 1),
            "WALKING": (16, 3),
            "MAGIC": (0, 4),
        }
        self.current_anim: str = ""

    def update(self) -> None:
        super().update()

        pyxel.camera(self.position.x - pyxel.width / 2, 0)
        dx, dy = 0, 0

        # if pyxel.btn(pyxel.KEY_Z):
        #     dy = -1
        # if pyxel.btn(pyxel.KEY_S):
        #     dy = 1
        dx: int = -pyxel.btn(pyxel.KEY_Q) + pyxel.btn(pyxel.KEY_D)

        self.is_walking_flags = bool(abs(dx))
        if self.is_walking_flags and not self.is_in_air_flags:
            self.current_anim = "WALKING"
        elif pyxel.btn(pyxel.KEY_P) and not self.is_in_air_flags:
            self.current_anim = "MAGIC"
        else:
            self.current_anim = "IDLE"

        if pyxel.btn(pyxel.KEY_SPACE) and not self.is_bonked():
            if not self.is_in_air_flags:
                self.velocity.y += 18 * Maths.GRAVITY * Maths.DELTA
                self.is_in_air_flags = True

        self.move_and_slide(dx, dy)
        # print(self.is_bonked() and self.is_on_floor())
        if self.is_on_floor() and self.is_in_air_flags:
            print("FLOATING")

    def draw(self) -> None:
        pyxel.rect(
            self.position.x + self.sprite_offset_x,
            self.position.y + self.sprite_offset_y,
            self.object_width,
            self.object_height,
            8,
        )
        if self.is_bonked() and not self.is_on_floor():
            pyxel.rect(
                self.position.x + self.sprite_offset_x,
                self.position.y + self.sprite_offset_y - self.object_height,
                self.object_width,
                self.object_height,
                6,
            )
        anim: tuple[int, int] = self.sprites_sheet[self.current_anim]
        coeff: int = (pyxel.frame_count // anim[1]) % anim[1]
        pyxel.blt(
            self.position.x,
            self.position.y,
            1,
            16 * coeff,
            anim[0],
            16,
            16,
            7,
        )

        pyxel.text(
            self.position.x + 1 - pyxel.width / 2, 1, f"{self.velocity=}", 6, None
        )
        pyxel.text(
            self.position.x + 1 - pyxel.width / 2,
            8,
            f"({self.position.x}, {self.position.y}) ; {self.velocity}",
            6,
            None,
        )
        # if self.is_bonked_flags and pyxel.frame_count % 10 != 0:
        #     pyxel.text(self.position.x - 8, self.position.y - 8, "BONKED !", 9, None)

    # def is_bonked(self) -> bool:
    #     if super().is_bonked():
    #         print("BONKED !")
    #         return True
    #     else:
    #         return False
