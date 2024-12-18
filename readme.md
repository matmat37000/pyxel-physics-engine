# Pyxel Physics Engine

Small physics engine for the python module [pyxel](https://github.com/kitao/pyxel) !

## Documentation of the MathiolEngine

### Introduction

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

You can add object to the scene with

```python
self.object_tree.add_object_to_scene("object_name", object_type)
```

> See [ObjectTree().add_object_to_scene()](#objecttreeadd_object_to_scene)

#### ObjectTree().add_object_to_scene()

```python
ObjectTree().add_object_to_scene("object_name", object_type, "parent_name", *args, **kwargs)
```

##### Fields

`object_name` (`str`) is for retrieving the object, this must be a unique identifier.

`new_object` (`type`) is the type of the object, not the instance, for example:

```python
class Player: ...

player_type = Player
player_object = Player()
```

`parent_id` (`str`) by default is none, this is field is for (not implemented) parent/child system in the tree

`*args`, `**kwargs` are for the `object_type` constructor is there any.

##### Exception

`KeyError`: Object with this name already exist

> You're trying to add an object with an `object_name` already used

`KeyError`: Parent does not exist

> You're trying to parent your object to an `object_name` that doesn't exist
