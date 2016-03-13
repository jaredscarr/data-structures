# -*- coding: utf-8 -*-
"""Implementation of stack."""

from linked_list import LinkedList


class Stack(object):
    """Create Stack class."""

    def __init__(self):
        """Initialize Stack object."""
        self.container = LinkedList()

    def push(self, val):
        """Push value to head of stack."""
        self.container.insert(val)

    def pop(self):
        """Remove and return the head of the stack."""
        return self.container.pop()
