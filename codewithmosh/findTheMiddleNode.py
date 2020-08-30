# Find a middle node in a given linked list assume that you don't know the size ahead of the time
# if the length of the list is odd return one middle node [10 -> 20 -> 30]  = [20]
# if the length of the list is even return two middle node
# [10 -> 20] = [10,20]
# [10 -> 20 -> 30 -> 40] = [20,30]

class NodeList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self, node):
        while node is not None:
            print(node.val)
            node = node.next


def findtheMiddleNode(head):
    # [ 10 -> 20 -> 30 -> 40 -> 50]
    # use two pointers
    # listsize          Middle value
    #   1                   1
    #   3                   2
    #   5                   3
    #   7                   4
    # see the pattern the size of the list size increase by 2 where the middle value only increase by 1
    # use slow fast pointers slow jumps to next node and fast jumps 2 node

    count = 1
    slow = fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        count += 1

    if count % 2 == 0:
        return [slow.val, slow.next.val]
    return [slow.val]
    #print(f"{slow.val} {count} ")


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

print(findtheMiddleNode(head))
