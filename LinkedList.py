class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:

    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.count = 0

    # add Last

    def addLast(self, item):
        node = Node(item)

        # if the list is empty or not
        if self.isEmpty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.count += 1

    # add First

    def addFirst(self, item):
        node = Node(item)

        # check if the list is empty
        if self.isEmpty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node
        self.count += 1

    # remove first
    def removeFirst(self):
        if self.isEmpty():
            raise RuntimeError("The LinkedList is empty")

        elif self.first == self.last:
            self.first = self.last = Node()
        else:
            second = self.first.next
            self.first.next = None
            self.first = second
        self.count -= 1

    # remove Last node
    def removeLast(self):
        if self.isEmpty():
            raise RuntimeError("LinkList is empty")
        elif self.first == self.last:
            self.first = self.last = Node()
        else:
            # [10 -> 20 -> 30]
            current = self.first
            while current is not None:
                if current.next is self.last:
                    break
                current = current.next
            self.last = current
            self.last.next = None
        self.count -= 1

    # find Index of the node

    def indexOf(self, item):
        index = 0
        current = self.first
        while current is not None:
            if current.value == item:
                return index
            current = current.next
            index += 1
        else:
            return -1

    # contains
    def contains(self, item):
        return self.indexOf(item) != -1

    # length of linked list
    def size(self):
        return self.count

    # helper function

    def isEmpty(self):
        return self.first.value is None


llist = LinkedList()
print(llist.size())
llist.addFirst(10)
print(llist.size())
llist.removeFirst()
print(llist.size())
llist.addFirst(20)
llist.addFirst(30)
llist.addLast(40)
print(llist.size())
llist.removeLast()
print(llist.size())
llist.addLast(50)
llist.removeFirst()
print(llist.size())
print(llist.indexOf(60))
print(llist.contains(50))
