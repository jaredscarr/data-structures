# -*- coding: utf-8 -*-


def test_pop():
    """Test if entry sorts to the correct position."""
    from binheap import Heap
    heap = Heap()
    heap.container = [2, 3, 4, 10]
    heap.pop()
    assert heap.container == [10, 3, 4]


def test_push():
    """Test when a value is appended to the heap the structure is maintained."""
    from binheap import Heap
    heap = Heap()
    heap.container = [4, 7, 38, 96]
    heap.push(5)
    assert heap.container == [96, 7, 38, 4, 5]

