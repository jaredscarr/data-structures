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
        self.container = ['a','b', 'c', 'd']

    def left(self, index):
        """Return left child of parent."""
        return self.container[(index * 2) + 1]

    def right(self, index):
        """Return right child of parent."""
        return self.container[(index * 2) + 2]

    def parent(self, index):
        """Return parent of a child."""
        return self.container[index // 2 - 1]

    def swappy(self, value):
        """Swap parent and child."""
        val_index = self.container.index(value)
        temp_location = self.container[val_index]
        current_parent = self.parent(val_index)
        self.container[current_parent] = value
        self.container[val_index] = temp_location
        return self.container[current_parent]

    def push(self, value):
        """Push a value to the Heap and maintain Heap structure."""
        heap = self.container
        heap.append(value)
        current_parent = self.parent(value)
        while current_parent < value:
            current_parent = self.swappy(value)


#     def bubble_up():
#         swappy_thing(left(index), parent(index))












#     @property
#     # to set length of list
#     def foo(self):
#         return self._foo

# # Use len - 1, not insert ''


#     # def heapify(self):



#     # def push(self):




#     def swap(index):
#         temp = my_list[parent(index)]
#         my_list[parent(index)] = my_list[index]
#         my_list[index] = temp

#     while (index+1) // 2 > 0:


#         parent = (index - 1) >> 1
#         bitshifting





