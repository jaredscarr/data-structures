# -*- coding: utf-8 -*-
"""Test methods of the deque class."""
import pytest


def test_append_left_on_empty():
    """Assert append_left adds node to the head."""
    from deq import Deque
    my_list = Deque()
    my_list.append_left(7)
    assert my_list.container.head.val == 7


def test_append_left_non_empty():
    """Assert append left adds node to the head."""
    from deq import Deque
    my_list = Deque()
    my_list.append_left(7)
    my_list.append_left('thiat')
    assert my_list.container.head.val == 'thiat'


def test_append_empty():
    """Assert append adds node to the tail."""
    from deq import Deque
    my_list = Deque()
    my_list.append('thiat')
    assert my_list.container.tail.val == 'thiat'


def test_append_non_empty():
    """Assert append adds node to the tail."""
    from deq import Deque
    my_list = Deque()
    my_list.append('thies')


def test_pop_empty():
    """Assert raises error."""
    from deq import Deque
    with pytest.raises(AttributeError):
        my_list = Deque()
        my_list.Deque.pop()


def test_pop():
    """Assert pops val from the tails."""
    from deq import Deque
    my_list = Deque()
    my_list.append_left('thies')
    my_list.append_left('thiat')
    my_list.append_left('strongbad')
    my_list.pop()
    assert my_list.container.head.val == 'strongbad'




