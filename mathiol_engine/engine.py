from typing import Any


class Child:
    """
    Child object for the ObjectTree
    """

    def __init__(self, parent_id: str, child_name: str, base_object: Any) -> None:
        self.parent_id: str = parent_id
        self.name: str = child_name
        self.base_object: Any = base_object
        self.id = id(base_object)

    def __str__(self) -> str:
        return str(self.base_object)

    def __repr__(self) -> str:
        return self.__str__()


class Parent:
    """
    Parent object for the ObjectTree
    """

    def __init__(self, name: str, base_object: Any) -> None:
        self.child: dict[str, Child] = {}
        self.name: str
        self.base_object: Any = base_object
        self.id = id(self)

    def add_child(self, child_name: str, child: Any) -> None:
        new_child = Child(self.name, child_name, child)
        self.child[child_name] = new_child

    def __setitem__(self, key: str, value: Any) -> None:
        new_child = Child(self.name, key, value)
        self.child[key] = new_child

    def __getitem__(self, key: str) -> dict[str, Child]:
        return self.child

    def __str__(self) -> str:
        return f"{self.base_object} > {self.child}"

    def __repr__(self) -> str:
        return self.__str__()


class ObjectTree(dict[str, Parent]):
    """
    Tree system for object in the scene
    """

    def update_tree_objects(self) -> None:
        for pyxel_object in self.values():
            update_f = getattr(pyxel_object.base_object, "update", None)
            if callable(update_f):
                update_f()
                # pyxel_object.base_object.update()

    def draw_tree_objects(self) -> None:
        for pyxel_object in self.values():
            update_f = getattr(pyxel_object.base_object, "draw", None)
            if callable(update_f):
                update_f()

    def add_object_to_scene(
        self,
        object_name: str,
        new_object: object,
        parent_id: str | None = None,
    ) -> None:
        """
        Add an object to the scene tree

        Args:
            object_name (str): Name of the object, must be an unique identifier
            new_object (type): The new object
            parent_id (str | None, optional): Parent id (object_name). Defaults to None.

        Raises:
            KeyError: An object with the same id (name) already exist
            KeyError: Parent doesn't exist
        """
        if object_name in self:
            raise KeyError("Object with this name already exist")
        if parent_id is None:
            new_parent: Parent = Parent(object_name, new_object)
            self.update({object_name: new_parent})
        else:
            parent: Parent | None = self.get(parent_id)
            if parent is not None:
                parent.child[object_name] = Child(parent_id, object_name, new_object)
            else:
                raise KeyError("Parent does not exist")

    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(key).base_object

    def __setitem__(self, key: str, value: Any) -> None:
        super().__getitem__(key).base_object = value


if __name__ == "__main__":
    tree = ObjectTree()
    tree.add_object_to_scene("test", 5, None)
    tree.add_object_to_scene("test2", "By !", None)
    tree.add_object_to_scene("child1", "I'm a child", "test")
    print(tree)
    print(tree["test"])
