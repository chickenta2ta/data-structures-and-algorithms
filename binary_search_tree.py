class Node:
    def __init__(self, object):
        self.object = object
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, object):
        if not self.root:
            self.root = Node(object)
        else:
            self.insert_(self.root, object)

    def insert_(self, node, object):
        if object < node.object:
            if not node.left:
                node.left = Node(object)
            else:
                self.insert_(node.left, object)
        else:
            if not node.right:
                node.right = Node(object)
            else:
                self.insert_(node.right, object)

    def delete(self, object):
        self.root = self.delete_(self.root, object)

    def delete_(self, node, object):
        if not node:
            return None
        if object < node.object:
            node.left = self.delete_(node.left, object)
            return node
        elif object > node.object:
            node.right = self.delete_(node.right, object)
            return node
        else:
            if not node.left and not node.right:
                return None
            elif node.left and not node.right:
                return node.left
            elif not node.left and node.right:
                return node.right
            else:
                right, min = self.deletemin(node.right)
                min.right = right
                min.left = node.left
                return min

    def deletemin(self, node):
        if node.left:
            node.left, min = self.deletemin(node.left)
            return node, min
        else:
            return node.right, node
