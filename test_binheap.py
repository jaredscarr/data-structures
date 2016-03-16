# -*- coding: utf-8 -*-
def test_iterable_passed():
    """Test if Heap is initialized."""
    from binheap import Heap
    my_heap = Heap([1, 2, 3, 4]) 
    assert my_heap.container[0] == ''


def test_left():
    """Assert if item in list is the left child."""
    from binheap import Heap
    my_heap = Heap([1, 2, 3, 4])
    assert my_heap.left(1) == 2


def test_right():
    """Assert if item in list is the right child."""
    from binheap import Heap
    my_heap = Heap([1, 2, 3, 4])
    assert my_heap.right(1) == 3


def test_parent():
    """Assert if the item in the list is a parent."""
    from binheap import Heap
    my_heap = Heap([1, 2, 3, 4])
    assert my_heap.parent(2) == 1

# def test_parent():

# def test_heapify():
#     """Test weather or not the greater of two values are swapped."""
#     from binheap import Heap
#     my_heap = Heap(['', 1, 10, 6, 8, 3, 9])
#     assert swap(some_list) == [1, 3, 6, 8, 9]