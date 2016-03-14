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

    def __init__(self, iterable=None):
        """Init linked list object with optioanl itterable."""
        self.head = None
        self.iterable = iterable
        if iterable is not None:
            try:
                for i in iterable:
                    self.insert(i)
            except TypeError:
                print('value is not an interable')

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
        new_head = current.next
        self.head = new_head
        return current.val

    def remove(self, val):
        """Remove specific val."""
        current = self.head
        if current.val == val:
            self.head = current.next
        else:
            while current.next.val != val:
                try:
                    current = current.next
                except AttributeError:
                    print('That value is not in the list.')
            current.next = current.next.next

    def size(self):
        """Return length of list."""
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def display(self):
        """Print list as tuple."""
        container = []
        current = self.head
        while current is not None:
            container.append(current.val)
            current = current.next
        print(tuple(container))
        return tuple(container)
