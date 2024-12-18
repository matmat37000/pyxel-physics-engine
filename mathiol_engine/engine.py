from typing import Any


class Child:
    def __init__(self, parent_id: str, child_name: str, base_object: Any) -> None:
        self.parent_id: str = parent_id
        self.name: str = parent_id
        self.base_object: Any = base_object
        self.id = id(base_object)

    def __str__(self) -> str:
        return str(self.base_object)

    def __repr__(self) -> str:
        return self.__str__()


class Parent:
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
    def __init__(self) -> None:
        super().__init__()

    def add_object_to_scene(
        self,
        object_name: str,
        new_object: type,
        parent_id: str | None = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        if self.__contains__(object_name):
            raise KeyError("Object with this name already exist")
        if parent_id is None:
            new_instance = new_object(*args, **kwargs)
            new_parent: Parent = Parent(object_name, new_instance)
            self.update({object_name: new_parent})
        else:
            parent: Parent | None = self.get(parent_id)
            if parent is not None:
                parent.child[object_name] = Child(
                    parent_id, object_name, new_object(*args, **kwargs)
                )
            else:
                raise KeyError("Parent does not exist")

    def __getitem__(self, key: str) -> Any:
        return super().__getitem__(key).base_object

    def __setitem__(self, key: str, value: Any) -> None:
        super().__getitem__(key).base_object = value


if __name__ == "__main__":
    tree = ObjectTree()
    tree.add_object_to_scene("test", int, None, 5)
    tree.add_object_to_scene("test2", str, None, "By !")
    tree.add_object_to_scene("child1", str, "test", "I'm a child")
    print(tree)
    print(tree["test"])
