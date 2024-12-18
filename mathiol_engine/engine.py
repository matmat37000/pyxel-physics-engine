class ObjectTree:
    def __init__(self) -> None:
        self.object_tree: dict[int, Parent] = {}

    def add_object_to_scene(self, new_object: object):
        new_parent: Parent = Parent(new_object)
        self.object_tree[new_parent.id] = new_parent


class Child:
    def __init__(self, parent_id: int, base_object: object) -> None:
        self.parent_id: int = parent_id
        self.base_object: object = base_object
        self.id = id(base_object)


class Parent:
    def __init__(self, base_object: object) -> None:
        self.child: dict[int, Child] = {}
        self.base_object: object = base_object
        self.id = id(self)

    def add_child(self, child: object) -> None:
        new_child = Child(id(self), child)
        self.child[new_child.id] = new_child
