class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

a = Node(1)
print(a.data)
print(a.next)
b = Node(2)
c = Node(3)

class LinkedList:

    def __init__(self):

        # create an empty linked list
        self.head = None
        self.n = 0 # no of nodes in the linked list

        