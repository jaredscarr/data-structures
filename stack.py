# -*- coding: utf-8 -*-

from linked_list import LinkedList
from linked_list import Node


class Stack(object):
    """Create Stack class."""

    def __init__(self, iterable=None):
        """Initialize Stack object."""
        self.head = None
        self.container = LinkedList()

    def push(self, val):
        """Push value to head of stack."""
        # self.container = LinkedList()
        self.container.insert(val)

    def pop(self):
        """Remove and return the head of the stack."""
        self.container.pop()
