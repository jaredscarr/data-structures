# -*- coding: utf-8 -*-


class Node(object):
    """Construct Node object."""

    def __init__(self, val):
        """Initialize node object."""
        self.val = val
        self.next = None

    def get_val(self):
        """Get data."""
        return self.val


class LinkedList(object):
    """Handle creation of a linked list."""

    def __init__(self):
        """Init linked list object."""
        # self.temp_list = []
        self.head = None

    def insert(self, val):
        """Insert new node at head of list."""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def search(self, val):
        """Search for value and return node."""
        current = self.head
        found = False
        while current and not found:
            if current.val == val:
                found = True
                return current.val
            current = current.next
        return None

    def pop(self):
        """Remove node at head and returns the value."""
        current = self.head
        new_head = current.get_next()
        new_head = self.head


    # def remove(self, node):
    #     """Remove specific node."""
    #     current = self.head
    #     previous = None
    #     found = False
    #     while current is not None and not found: 
    #         if current.get_val == node:
    #             previous = current
    #             current = current.get_next()
    #             found = True
    #         current = current.get_next()
    #         previous = current.get_data()
    #     if 
