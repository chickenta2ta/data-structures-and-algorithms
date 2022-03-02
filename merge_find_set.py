class Node:
    def __init__(self, object):
        self.parent = None
        self.object = object


class Set:
    def __init__(self, root: Node):
        self.root = root
        self.size = 1


class MergeFindSet:
    def __init__(self, objects: list):
        self.object_to_node = {}

        for object in objects:
            node = Node(object)
            node.parent = Set(node)
            self.object_to_node[object] = node

    def merge(self, set0, set1):
        if set0 == set1:
            return
        if set0.size > set1.size:
            set1.root.parent = set0.root
            set0.size += set1.size
        else:
            set0.root.parent = set1.root
            set1.size += set0.size

    def find(self, object):
        node = self.object_to_node[object]
        while isinstance(node.parent, Node):
            node = node.parent
        return node.parent
