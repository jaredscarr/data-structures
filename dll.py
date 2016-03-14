# -*- coding: utf-8 -*-


class Node(object):
    """Construct Node object."""

    def __init__(self, val):
        """Initialize node object."""
        self.val = val
        self.next = None
        self.previous = None


class DoublyLinkedList(object):
    """Handle creation of a linked list."""

    def __init__(self, iterable=None):
        """Init linked list object with optioanl itterable."""
        self.head = None
        self.iterable = iterable
        self.tail = None
        if iterable:
            try:
                for i in iterable:
                    self.insert(i)
            except TypeError:
                print('value is not an interable')

    def insert(self, val):
        """Insert new node at head of list."""
        new_node = Node(val)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        else:
            next_node = self.head
            next_node.previous = new_node
            new_node.next = next_node
            self.head = new_node

    def append(self, val):
        """Add node to end of list."""
        new_node = Node(val)
        last = self.tail
        if last is None:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node
        else:
            last.next = new_node
            new_node.previous = last
            self.tail = new_node

    def pop(self):
        """Remove node at head and returns the value."""
        if self.head is None:
            raise AttributeError
            print('err')
        current = self.head
        new_head = self.head.next
        new_head.previous = None
        self.head = new_head
        current.next = None
        return current.val

    def shift(self):
        """Remove node at the tail and return the value."""
        if self.tail is None:
            raise AttributeError
            print('You can shift an empty list!')
        last_node = self.tail
        new_tail = self.tail.previous
        new_tail.next = None
        self.tail = new_tail
        last_node.previous = None
        return last_node.val

    def remove(self, val):
        """Remove selected Node from the list."""
        current = self.head
        if current.val == val:
            self.head = current.next
            self.head.previous = None
            current.next = None
        elif self.tail.val == val:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            while current.next.val != val:
                try:
                    current = current.next
                except AttributeError:
                    print('That value is not here.')
            current.next = current.next.next
            current.next.previous = current
