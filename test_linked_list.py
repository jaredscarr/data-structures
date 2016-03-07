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


def test_insert():
    """Test if inserts to head position."""
    from linked_list import Node
    from linked_list import LinkedList
    from linked_list import insert
    new_node = Node('dogs', 'cats')
    next_node = Node('cats')
    assert new_node.next == next_node.data
