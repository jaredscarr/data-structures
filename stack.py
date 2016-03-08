# -*- coding: utf-8 -*-


class Node(object):
    """Construct Node object."""

    def __init__(self, data, point_to=None):
        """Initialize node object."""
        self.data = data
        self.point_to = point_to


class Stack(object):
    """Implement a stack."""

    def __init__(self, iterable=[]):
        """Init a stack."""
        self.top = None

    def push(self, val):
        """Add node to top of stack."""
        new_node = Node(val)
        self.top = new_node

