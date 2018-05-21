''' A linked list consists of nodes that contain vals and pointers.
The pointers point to another node. This means to get all vals in a
linked list, you must traverse them sequentially.

Advantages:
    - memory saving.
'''


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next


# create all nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# link them together
node1.next = node2
node2.next = node3

# print all vals stored in linked list
node1.traverse()
