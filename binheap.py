# -*- coding: utf-8 -*-
class Heap(object):
    """Create a Heap."""

    def __init__(self, iterable=None):
        """Initialize Heap."""
        if iterable:
            self.container = list(iterable)
            self.container.insert(0, '')
        else:
            self.container = ['']

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
