# -*- coding: utf-8 -*-
"""Implementation of the deque class."""

from dll import DoublyLinkedList


class Deque(object):
    """Deque class."""

    def __init__(self):
        """Initilizer of deque class."""
        self.container = DoublyLinkedList()

    def append_left(self, val):
        """Append val to the head of the list."""
        self.container.insert(val)

    def append(self, val):
        """Append val to the tail of the list."""
        self.container.append(val)

    def pop(self):
        """Return and remove head from the list."""
        self.container.shift()

)


