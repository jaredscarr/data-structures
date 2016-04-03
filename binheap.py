# -*- coding: utf-8 -*-
class Heap(object):
    """Create a Heap."""

    def __init__(self, iterable=None):
        """Initialize Heap."""
        # if iterable:
        #     self.container = list(iterable)
        #     for i in self.container:
        #         self.push(i)
        # else:
        self.container = []
        self.current_size = 0

    # def swap(self, value):
    #     """Swap parent and child."""
    #     val_index = self.container.index(value)
    #     current_parent = self.parent(val_index)
    #     self.container[current_parent] = value
    #     self.container[val_index] = current_parent
    #     return self.container[current_parent]

    def push(self, value):
        """Push a value to the Heap and maintain Heap structure."""
        self.container.append(value)
        child = len(self.container) - 1
        parent = (child - 1) // 2
        while child > 1 and self.container[child - 1] > self.container[parent - 1]:
            small_parent = self.container[parent - 1]
            self.container[parent - 1] = self.container[child - 1]
            self.container[child - 1] = small_parent
            child = parent
            parent = (child - 1) // 2

    def pop(self):
        """Pop the root of the heap."""
        self.container[0] = self.container.pop()
        self.sort_to_leaf(0)

    def sort_to_leaf(self, index):
        """Sort up the heap."""
        # import pdb; pdb.set_trace()
        index += 1
        left = 2 * index
        right = 2 * index + 1
        most_huge = index
        size = len(self.container)
        if left <= size and self.container[left - 1] > self.container[most_huge - 1]:
            most_huge = left
        if right <= left and self.container[right - 1] > self.container[most_huge - 1]:
            most_huge = right
        if most_huge != index:
            value = self.container[index - 1]
            self.container[index - 1] = self.container[most_huge - 1]
            self.container[most_huge - 1] = value
            self.sort_to_leaf(most_huge - 1)
