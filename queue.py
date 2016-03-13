# -*- coding: utf-8 -*-
from dll import DoublyLinkedList


class Queue(object):
    """Queue class. Startrek. Nerds."""

    def __init__(self):
        """Init the Queue."""
        self.container = DoublyLinkedList()

    def enqueue(self, val):
        """Insert into front position."""
        self.container.insert(val)

    def dequeue(self, val):
        """Remove item in the list."""
        self.container.remove(val)

    def size(self):
        """Return size of container."""
        current = self.container.head
        counter = 1
        if current is None:
            return 0
        while current.next is not None:
            counter += 1
            current = current.next
        return counter
