class Queue(object):
    ''' Like a list except only the first element can be removed.

    FIFO; First In First Out
    '''

    def __init__(self, l):
        self._l = l

    def enqueue(self, x):
        self._l.append(x)

    def dequeue(self):
        self._l = self._l[1:]
