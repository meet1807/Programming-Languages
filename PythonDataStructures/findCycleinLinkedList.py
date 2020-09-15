# find if the linked list has a loop
# in the below example node(50).next points to 30 creating a loop
#  10 -> 20 -> 30 -> 40 -> 50
#               ^           ^
#               |-----------|
# Hint : use floyd's cycle finding algorithm

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findCycleinLinkedList(head: NodeList) -> bool:
    # declare two pointers slow : jumps one node at a time & fast  : jumps 2 node at a time
    # according to floyd's algorithm for finding cycle both pointers will meet at some point

    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False


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
fifth.next = head

print(findCycleinLinkedList(head))
