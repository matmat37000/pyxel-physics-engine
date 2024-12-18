# Pyxel Physics Engine

Small physics engine for the python module [pyxel](https://github.com/kitao/pyxel) !

# Documentation of the MathiolEngine

First, you need a main file to handle pyxel.

You can create a basic class for this:

```python
import pyxel
from mathiol_engine.engine import ObjectTree

class Game:
    def __init__(self):
        pyxel.init(240, 160)
        self.object_tree: ObjectTree = ObjectTree()
        pyxel.run(self.update, self.draw)

    def update(self):
        ...

    def draw(self):
        # Clear the screen
        pyxel.cls(0)


if __name__ == "__main__":
    Game()
```

To 
