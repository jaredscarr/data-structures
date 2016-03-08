# -*- coding: utf-8 -*-


class Node(object):
    """Construct Node object."""

    def __init__(self, data):
        """Initialize node object."""
        self.data = data
        self.next = None

        def get_data(self):
        """Get data."""
        return self.data

        def get_next(self):
        """Get the reference to the next node."""
        return self.next_node

        def set_next(self, new_next):
        """Set the reference to the next node."""
        self.next_node = new_next


class LinkedList(object):
    """Handle creation of a linked list."""

    def __init__(self):
        """Init linked list object."""
        self.temp_list = []

    def insert(self, val):
        """Insert new node at head of list."""
        new_node = Node(val)
        new_node.next

    def pop(self):
        """Removes node at head and returns the value."""
        pass


    def remove(self, node):
        """Remove specific node."""
        current = self.head
        previous = None
        found = False
        while current.next is not None and not found:
            current = current.data
