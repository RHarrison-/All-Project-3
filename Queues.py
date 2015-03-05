import collections

'''
This is a simple wrapper built around the Collections module in python.
A Collection is much faster and useful for the search algorithm
incorporated into the program.
'''
#=========== Collection Wrapper: Queue ====================
class Queue: # A wrapper made around the collections library
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0
    
    def put(self,x):#appends to the array
        self.elements.append(x)

    def get(self): #removes and returns a element from the left sode of the array.
        if len(self.elements) != 0:
            return self.elements.popleft()

    def reverse(self): #reverses the array
        return self.elements.reverse()

    def clear(self):
        self.elements.clear()

    def length(self):
        return self.elements.count()
        
