# -*- coding: utf-8 -*-
class Heap(object):
    """Create a Heap."""

    def __init__(self, iterable=None):
        """Initialize Heap."""
        if iterable:
            self.container = list(iterable)
        else:
            self.container = []
        # self.parent = self.container[i // 2]
        # self.left = self.container[2*i]
        # self.right = self.container[2*i+1]

    def left(self, index):
        """Return left child of parent."""
        return self.container[index * 2]

    def right(self, index):
        """Return right child of parent."""
        return self.container[index * 2 + 1]

    def parent(self, index):
        """Return parent of a child."""
        return self.container[index // 2]

    # def heapify(self):

    # def pop(self):

    # def push(self):
