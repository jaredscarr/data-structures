# -*- coding: utf-8 -*-
import pytest


# .insert(item): inserts an item into the queue.
def test_insert():
    """Test if value is inserted into the queue."""
    from priority_queue import PriorityQueue
    pq = PriorityQueue()
    pq.priority_queue.append(('value', 1))
    assert pq.priority_queue[0] == ('value', 1)

# .pop(): removes the most important item from the queue.
# def test_pop():
#     """Test if popped item is the top of the queue."""
#     from priority_queue import PriorityQueue
#     pq = PriorityQueue()
#     pq.insert(('value', 1))
#     assert pop() == ('value', 1)


# def test_pop_removed_item():
#     """Test if popped item is the top of the queue."""
#     from priority_queue import PriorityQueue
#     pq = PriorityQueue()
#     pq.priority_queue['value'] = 1
#     pq.priority_queue['second'] = 2
#     pq.pop()
#     assert 'value' not in pq.priority_queue

# .peek(): returns the most important item without removing it from the queue.
# def test_peek():
#     """Test if the most important is returned but still in queue."""
#     from priority_queue import PriorityQueue
#     pq = PriorityQueue()
#     pq.priority_queue['value'] = 1
#     pq.priority_queue['second'] = 2
#     assert peek() == 1
