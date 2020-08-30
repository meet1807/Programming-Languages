# reverse the given linked list
# [10 -> 20 -> 30 -> 40 -> 50 -> Null] = [ 50 -> 40 -> 30 -> 20 -> 10 -> Null]

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self, node):
        while node is not None:
            print(node.val)
            node = node.next


def reverseLinkedList(head):
    prev, current, ref = None, head, head

    while ref is not None:
        ref = ref.next
        current.next = prev
        prev = current
        current = ref

    return prev


head = NodeList(10)
second = NodeList(20)
third = NodeList(30)
fourth = NodeList(40)
fifth = NodeList(50)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
#fifth.next = None

reversedList = reverseLinkedList(head)
NodeList().printList(reversedList)
