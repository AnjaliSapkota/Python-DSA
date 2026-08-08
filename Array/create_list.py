# Creating a custom list class using ctypes

import ctypes

class MyList:

    # creating array
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        # [1,2,3]
        result = ""
        for i in range(self.n):
            result = result + str(self.A[i]) + ','

        return '[' + result[:-1] + ']'

    # indexing function to get the item at the index
    def __getitem__(self, index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return "Index out of range"

    #append function to add item to the end of the list
    def append(self, item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)

        #append
        self.A[self.n] = item
        self.n += 1

    # pop function to remove the last item from the list
    def pop(self):
          if self.n == 0:
                return "List is empty"
          else:
              print(self.A[self.n-1])
              self.n = self.n - 1


    def clear(self):
        self.n = 0
        self.size = 1
    
    # resize function to resize the array when it is full by making a new array and copying the content of the old array to the new array and reassigning the new array to the old array
    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign A
        self.A = B

    # make_array function to create aarray with size capacity
    def __make_array(self, capacity):
        # create a c type array (static, referential) with size capacity
        return (capacity * ctypes.py_object)()

L = MyList()


L.append('hello')
L.append(2)
L.append(3.5)

print(L)
print(L[0])
print(L[3])
L.pop()
print(L)
L.pop()
print(L)
L.pop()
print(L)
L.pop()
print(L)

L = [10,2,3,45]
print(L)
L.clear()
print(L)