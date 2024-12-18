import pyxel

from characters.player import Player
from mathiol_engine.engine import ObjectTree


class COLOR:
    BLACK: int = 0
    DARK_BLUE: int = 1
    PURPLE: int = 2
    CYAN: int = 3
    BROWN: int = 4
    BLUE: int = 5
    LIGHT_BLUE: int = 6
    WHITE: int = 7
    PINK: int = 8
    ORANGE: int = 9
    YELLOW: int = 10
    LIGHT_GREEN: int = 11
    OCEAN_BLUE: int = 12
    GREY: int = 13
    PASTEL_PINK: int = 14
    PASTEL: int = 15


class Game:
    def __init__(self):
        pyxel.init(240, 160)

        self.object_tree = ObjectTree()
        self.player: Player = Player()
        self.player2: Player = Player()
        self.object_tree.add_object_to_scene(self.player)
        self.object_tree.add_object_to_scene(self.player)
        self.player.position.x = 15
        self.player2.position.x = 45

        # Flags
        self.debug_flags: bool = False

        # Load assets
        pyxel.load("assets/assets.pyxres")
        pyxel.images[0] = pyxel.Image.from_image(
            filename="assets/tileset_24x32.png", incl_colors=False
        )

        # Load the maps
        for i in range(3):
            pyxel.tilemaps[i] = pyxel.Tilemap.from_tmx(  # type: ignore
                filename="assets/maps.tmx", layer=i
            )

        pyxel.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        # Clear the screen
        pyxel.cls(COLOR.BLUE)
        # Load the tilemap
        pyxel.bltm(0, 0, 0, 0, 0, pyxel.width, pyxel.height, COLOR.PURPLE)
        pyxel.bltm(0, 0, 1, 0, 0, pyxel.width, pyxel.height, COLOR.PURPLE)
        if self.debug_flags:
            pyxel.bltm(0, 0, 2, 0, 0, pyxel.width, pyxel.height, COLOR.PURPLE)

        # Call the player draw
        self.player.draw()


if __name__ == "__main__":
    Game()
