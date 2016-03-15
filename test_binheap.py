# -*- coding: utf-8 -*-

def test_init():
    """Test if Heap is initialized."""
    from binheap import Heap
    my_heap = Heap()
    some_list = [1, 2, 3, 4]
    my_heap

# def test_heapify():
#     """Test weather or not the greater of two values are swapped."""
#     from binheap import Heap
#     some_list = [1, 2, 3, 4]
#     assert swap(some_list) == [4, 3, 2, 1]
