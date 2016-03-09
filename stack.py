# -*- coding: utf-8 -*-

from linked_list import LinkedList

from linked_list import Node


class Stack(LinkedList):
    """Create Stack class."""

    def __init__(self, itr=None):
        """Initialize Stack object."""
        self.head = None

    def push(self, val):
        """Push value to head of stack."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            self.head.next = new_node
            self.head = new_node
