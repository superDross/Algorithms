''' The heapq module is more practical.'''


class Heap(object):
    ''' A priority list with the smallest value taking priority.'''
    def __init__(self, l):
        self._l = l
        self._sort()

    def __str__(self):
        return str(self._l)

    def _sort(self):
        self._l = sorted(self._l)

    def push(self, x):
        self._l.append(x)
        self._sort()

    def pop(self):
        self._l = self._l[1:]

    def place(self, x):
        self.pop()
        self.push(x)


# heap sortd elements when intialised
l = [9, 0, 1, 2, 3, 4]
heap = Heap(l)
print(heap)

# add new element to heap
heap.push(7)
print(heap)

# remove first element
heap.pop()
print(heap)

# remove first element and replace with new value
heap.place(12)
print(heap)
