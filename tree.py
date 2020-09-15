# Implement a binary Tree with insert and find method
# Root Node
# (value, leftchild, rightchild)

class Node:
    def __init__(self, val=None, leftChild=None, rightChild=None):
        self.val = val
        self.leftChild = leftChild
        self.rightChild = rightChild


class Tree:

    def __init__(self):
        self.root = Node()

    def insertNode(self, value):
        node = Node(value)
        if self.root.val is None:
            self.root = node
            return

        current = self.root
        while True:
            if value < current.val:
                if current.leftChild is None:
                    current.leftChild = node
                    break
                current = current.leftChild
            elif value > current.val:
                if current.rightChild is None:
                    current.rightChild = node
                    break
                current = current.rightChild

    def find(self, value: int) -> bool:
        current = self.root
        while current is not None:
            if value < current.val:
                current = current.leftChild
            elif value > current.val:
                current = current.rightChild
            else:
                return True
        else:
            return False


tree = Tree()
tree.insertNode(7)
tree.insertNode(4)
tree.insertNode(1)
tree.insertNode(9)
tree.insertNode(8)
tree.insertNode(6)
print(tree.find(6))
