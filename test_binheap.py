# -*- coding: utf-8 -*-
def test_iterable_passed():
    """Test if Heap is initialized."""
    from binheap import Heap
    my_heap = Heap([1, 2, 3, 4])
    assert my_heap.container[0] == 'a'


def test_left():
    """Assert if item in list is the left child."""
    from binheap import Heap
    my_heap = Heap(['a', 'b', 'c', 'd'])
    assert my_heap.left(0) == 'b'


def test_right():
    """Assert if item in list is the right child."""
    from binheap import Heap
    my_heap = Heap([1, 2, 3, 4])
    assert my_heap.right(0) == 'c'


def test_parent():
    """Assert if the item in the list is a parent."""
    from binheap import Heap
    my_heap = Heap([1, 2, 3, 4])
    assert my_heap.parent(3) == 'a'


def test_push():
    """Test if value to the heap."""
    from binheap import Heap
    my_heap = Heap()
    my_heap.push(98)
    my_heap.push(24)
    assert my_heap[0] == 98
