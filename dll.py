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
        if iterable:
            try:
                for i in iterable:
                    self.insert(i)
            except TypeError:
                print('value is not an interable')

    def insert(self, val):
        """Insert new node at head of list."""
        new_node = Node(val)
        if new_node.next is None:
            new_node.next = self.head
            self.head = new_node
        else:
            next_node = new_node.next
            next_node.previous = new_node
            self.head = new_node






    # def search(self, val):
    #     """Search for value and return node."""
    #     current = self.head
    #     found = False
    #     while current and not found:
    #         if current.val == val:
    #             found = True
    #             return current.val
    #         current = current.next
    #     return None

    # def pop(self):
    #     """Remove node at head and returns the value."""
    #     current = self.head
    #     new_head = current.next
    #     new_head = self.head
    #     return current.val

    # def remove(self, val):
    #     """Remove specific val."""
    #     current = self.head
    #     previous = None
    #     found = False
    #     while current is not None and not found:
    #         if current.val == val:
    #             previous = current
    #             current = current.next
    #             found = True
    #         else:
    #             current = current.next
    #             previous = current.val
    #         if current is None:
    #             raise ValueError('Node not in list!')
    #         if previous is None:
    #             self.head = current.next
    #         else:
    #             previous.next = current.next

    # def size(self):
    #     """Return length of list."""
    #     current = self.head
    #     counter = 0
    #     while current is not None:
    #         counter += 1
    #         current = current.next
    #     return counter

    def display(self):
        """Print list as tuple."""
        container = []
        current = self.head
        while current is not None:
            container.append(current.val)
            current = current.next
        print(tuple(container))
        return tuple(container)









