# -*- coding: utf-8 -*-
import pytest


# .insert(item): inserts an item into the queue.
def test_insert():
    """Test if value is inserted into the queue."""
    from priority_queue import PriorityQueue
    pq = PriorityQueue()
    item = (1, 'value')
    pq.insert(item)
    assert pq.container[0] == (1, 'value')


def test_pop():
    """Test if removes highest priority."""
    from priority_queue import PriorityQueue
    pq = PriorityQueue()
    pq.container = [(2, 'fish'), (3, 'sticks'), (4, 'chix'), (10, 'ticks')]
    pq.pop()
    assert pq.container == [(10, 'ticks'), (3, 'sticks'), (4, 'chix')]


def test_peek():
    """Test if highest priority in queue is returned."""
    from priority_queue import PriorityQueue
    pq = PriorityQueue()
    pq.container = [(2, 'fish'), (3, 'sticks'), (4, 'chix'), (10, 'ticks')]
    assert pq.peek() == (2, 'fish')
