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

    def pop_left(self):
        """Remove head of deque and return that value."""
        self.container.pop()

    def peek(self):
        """Check the next node in the deque."""
        if self.container.tail is None:
            return None
        return self.container.tail.val

    def peek_left(self):
        """Return the tail of the deque."""
        if self.container.head is None:
            return None
        return self.container.head.val

    def size(self):
        """Return the size of the deque."""
        current = self.container.head
        counter = 1
        if current is None:
            return 0
        while current.next is not None:
            counter += 1
            current = current.next
        return counter
