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

    def peek(self):
        """Check the next node in the queue."""
        if self.container.tail is None:
            return None
        return self.container.tail.previous.val

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
