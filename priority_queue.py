# -*- coding: utf-8 -*-


class PriorityQueue(object):
    """A priority Queue."""

    def __init__(self):
        """Initialize PriorityQueue object."""
        self.container = []

    def insert(self, item):
        """Insert item into the queue."""
        self.container.append(item)
        child = len(self.container) - 1
        parent = (child - 1) // 2
        while child > 1 and self.container[child - 1][0] > self.container[parent - 1][0]:
            small_parent = self.container[parent - 1]
            self.container[parent - 1][0] = self.container[child - 1][0]
            self.container[child - 1][0] = small_parent
            child = parent
            parent = (child - 1) // 2

    def pop(self):
        """Pop the highest priority in the queue."""
        self.container[0] = self.container.pop()
        self.sort_to_leaf(0)

    def sort_to_leaf(self, index):
        """Sort up the heap."""
        index += 1
        left = 2 * index
        right = 2 * index + 1
        most_huge = self.container[index][0]
        size = len(self.container)
        if left <= size and self.container[left - 1][0] > self.container[most_huge - 1][0]:
            most_huge = left
        if right <= left and self.container[right - 1][0] > self.container[most_huge - 1][0]:
            most_huge = right
        if most_huge != self.container[index][0]:
            value = self.container[index - 1]
            self.container[index - 1] = self.container[most_huge - 1]
            self.container[most_huge - 1] = value
            self.sort_to_leaf(most_huge - 1)

    def peek(self):
        """Returns the highest priority item in the queue."""
        return self.container[0]
