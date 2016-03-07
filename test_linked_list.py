# -*- coding: utf-8 -*-
import pytest


def test_node_class():
    """Test Node."""
    from linked_list import Node
    new_node = Node('caterpillar')
    assert new_node.data == 'caterpillar'


def test_search():
    """Search for node in list and return node."""
    from linked_list import Node
    from linked_list import LinkedList
    from linked_list import search
    fake_list = ('20', 'bob', 'chicken-monkey', 'lizards')
    new_node = Node('chicken-monkey', 'lizards')
    assert fake_list.search('chicken-monkey') == new_node


def test_size():
    """Test if size of list is returned."""
    from linked_list import LinkedList
    from linked_list import size
    fake_list = ('20', 'bob', 'chicken-monkey', 'lizards')
    assert fake_list.size() == 4


def test_display():
    """Print the list."""
    from linked_list import Node
    from linked_list import LinkedList
    from linked_list import test_display
    new_node = Node('dogs', 'cats')
    next_node = Node('cats')
    fake_list = [new_node, next_node]
    assert fake_list.display() == ('dogs', 'cats')


def test_insert(val):
    """Test if inserts to head position."""
    from linked_list import Node
    from linked_list import LinkedList
    from linked_list import insert
    new_node = Node('dogs', 'cats')
    next_node = Node('cats')
    assert new_node.next == next_node.data
