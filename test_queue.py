# -*- coding: utf-8 -*-
import pytest


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


def test_dequeue_empty():
    """Test dequeue on empty."""
    from queue import Queue
    my_queue = Queue()
    with pytest.raises(AttributeError):
        my_queue.container.remove('puppy')


def test_dequeue_nonempty():
    """Test dequeue on empty."""
    from queue import Queue
    my_queue = Queue()
    my_queue.enqueue('monkey')
    my_queue.enqueue('chicken')
    my_queue.dequeue('monkey')
    assert my_queue.container.tail.val == 'chicken'


def test_peek():
    """Return the next value in the queue."""
    from queue import Queue
    my_queue = Queue()
    my_queue.enqueue('monkey')
    my_queue.enqueue('chicken')
    my_queue.enqueue('baby')
    assert my_queue.peek() == 'chicken'


def test_size():
    """Test if the size method works."""
    from queue import Queue
    my_queue = Queue()
    my_queue.enqueue('monkey')
    my_queue.enqueue('chicken')
    my_queue.enqueue('baby')
    assert my_queue.size() == 3
