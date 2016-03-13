# -*- coding: utf-8 -*-


def test_enqueue_empty():
    """Test enqueue on empty list."""
    from queue import Queue
    my_queue = Queue()
    my_queue.enqueue('chicken-monkey')
    assert my_queue.container.head.val == 'chicken-monkey'


def test_enqueue_nonempty():
    """Test enqueue on non-empty list."""
    from queue import Queue
    my_queue = Queue()
    my_queue.enqueue('chicken')
    my_queue.enqueue('monkey')
    assert my_queue.container.head.val == 'monkey'

# def test_dequeue

# def test_peek

# def test_size
