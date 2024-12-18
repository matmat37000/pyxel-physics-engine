from typing import Union
from mathiol_engine import engine
from mathiol_engine import maths
from mathiol_engine import pyxel_objects

__all__: list[str] = ["maths", "pyxel_objects", "engine"]

GameObjects = Union[pyxel_objects.PyxelObject, pyxel_objects.PyxelKinematicBody]
