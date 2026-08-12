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

    def __len__(self):
        return self.n

    def insert_head(self,value):

        # new node
        new_node = Node(value)

        # create connection
        new_node.next = self.head

        #reassign head
        self.head = new_node

        self.n = self.n + 1 

    def __str__(self):
        curr = self.head

        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head == new_node
            self.n = self.n + 1
            return
        
        curr = self.head

        while curr.next != None:
            curr = curr.next

        # you are at the last node
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):
        new_node = Node(value)

        curr = self.head

        while curr != None:
            if curr.data == after:
                break
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            return "Empty list"
        self.head = self.head.next
        self.n = self.n - 1

    def delete_tail(self):
        # empty list 
        if self.head == None: 
            return "Empty list"

        # only one node 
        if self.head.next == None: 
            return self.delete_head()

        curr = self.head

        # move to second-last node 
        while curr.next.next != None: 
            curr = curr.next

        # remove last node
        curr.next = None
        self.n = self.n - 1


    # delete by value

    def remove(self, value):

        curr = self.head

        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            #item not found
            return 'Not found'
        else:
            curr.next = curr.next.next

# Testing 

L = LinkedList() 

# insert at head

L.insert_head(1)
print(len(L))
L.insert_head(2)
print(len(L))
L.insert_head(3)
print(len(L))
L.insert_head(4)
print(len(L))

print(L)

L.append(5)
print(L)

L.clear()
# print(L)
# L.delete_head()
# print(L)

L.append(10)
L.append(20)
L.append(30)
print(L)
L.delete_tail()
print(L)