# -*- coding: utf-8 -*-


class Node(object):
    """Construct Node object."""

    def __init__(self, data):
        """Initialize node object."""
        self.data = data
        self.next = None


class LinkedList(object):
    """Handle creation of a linked list."""

    def __init__(self):
        """Init linked list object."""
        self.temp_list = []

    def insert(self, val):
        """Insert new node at head of list."""
        new_node = Node(val)
        new_node.next
