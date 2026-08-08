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

    # clear function to clear the list
    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError- Not in list"

    def insert(self, item, pos):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n, pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n + 1

    def __delitem__(self,pos):
        if 0<= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n - 1

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

L = MyList()

L.append('hello')
L.append(2)
L.append(3.5)

print(L)
print(L.find('hello'))
print(L.find('0'))

print(L)
L.insert(1,0)
print(L)
del L[3]
print(L)
