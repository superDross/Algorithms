class Stack(object):
    ''' Like a list but only remove the last appended element.

    LIFO; Last In First Out'''

    def __init__(self, l):
        self._l = l

    def append(self, x):
        self._l.append(x)

    def pop(self):
        self._l.pop()
