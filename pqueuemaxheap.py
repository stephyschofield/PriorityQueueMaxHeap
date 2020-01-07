# Stephanie Schofield - University of Oregon Clark Honors College - 2019
#
# Implementing a Priority Queue using a Max-Heap

class max_heap(object):
    """Binary max-heap

    Supports most standard heap operations (insert, peek, extract_max).
    Can be used for building a priority queue or heapsort. Since Python
    doesn't have built-in arrays, the underlying implementation uses a
    Python list instead. When initialized, max_heap creates a new list of
    fixed size or uses an existing list.
    """

    def __init__(self, size = 20, data = None):
        """Initialize a binary max-heap. """
        if data is not None:
            self.max_size = len(data)
            self.length = len(data)
            self.heap = data
        else:
            self.max_size = size
            self.length = 0
            self.heap = [None] * size
        
    def get_heap(self):
        return self.heap

    def insert(self, data):
        """Insert an element into the heap.
        
        Raises IndexError if the heap is full."""
        self.length = self.length + 1
        self.heap[self.length - 1] = -1

        """ Heap-Increase-Key(self, data) """
        i = self.length - 1
        if data < self.heap[i]:
            print("KeyError")
        self.heap[i] = data

        # can't have parent 
        while i > 0 and (self.heap[self.__get_parent(i)] < self.heap[i]):
            self.__swap(self.__get_parent(i), i)
            i = self.__get_parent(i)
         
    def peek(self):
        """Return the maximum value in the heap. Returns element at front of container."""
        return self.heap[0]

    def extract_max(self):
        """Remove and return the maximum value in the heap.

        Raises KeyError if the heap is empty."""
        
        if self.length < 1:
            raise KeyError
        heapmax = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.length = self.length - 1
        self.__heapify(0)
        return heapmax

    def __heapify(self, curr_index, list_length = None):
        # helper function for moving elements down in the heap
        
        left = self.__get_left(curr_index)
        right = self.__get_right(curr_index)
        if left < self.length and self.heap[left] > self.heap[curr_index]:
            largest = left
        else:
            largest = curr_index

        if right < self.length and self.heap[right] > self.heap[largest]:
            largest = right
   
        if largest != curr_index:
            self.__swap(curr_index, largest)
            self.__heapify(largest)

    def build_heap(self):
        # builds max heap from the list l.

        i = self.length // 2 - 1
        while i > -1:
            self.__heapify(i)
            i = i - 1

    def __get_parent(self, loc):
        # left child has odd location index
        # right child has even location index
        # if loc % 2 == 0:
        #     parent = int((loc - 2) / 2)
        # else:
        parent = int((loc - 1) / 2)
        return parent

    def __get_left(self, loc):
        return 2*loc + 1

    def __get_right(self, loc):
        return 2*loc + 2
        

    def __swap(self, a, b):
        # swap elements located at indexes a and b of the heap
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
    

def heap_sort(l):
    """Sort a list in place using heapsort."""

    templist = []
    resultlist = []
    myheap = max_heap(len(l), l)
    myheap.build_heap()
    for i in range(len(l)):
        mymax = myheap.extract_max()
        templist.append(mymax)

    for i in range(len(templist)):
        resultlist.append(templist.pop())

    return resultlist
