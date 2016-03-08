# -*- coding: utf-8 -*-
import pytest


# def test_node_class():
#     """Test Node."""
#     from linked_list import Node
#     new_node = Node('caterpillar')
#     assert new_node.get_data() == 'caterpillar'


def test_search():
    """Search for node in list and return node."""
    from linked_list import LinkedList
    fake_list = LinkedList()
    fake_list.insert('that')
    assert fake_list.search('that') == 'that'


# def test_size():
#     """Test if size of list is returned."""
#     from linked_list import LinkedList
#     from linked_list import size
#     fake_list = ('20', 'bob', 'chicken-monkey', 'lizards')
#     assert fake_list.size() == 4


# def test_display():
#     """Print the list."""
#     from linked_list import Node
#     from linked_list import LinkedList
#     from linked_list import test_display
#     new_node = Node('dogs', 'cats')
#     next_node = Node('cats')
#     fake_list = [new_node, next_node]
#     assert fake_list.display() == ('dogs', 'cats')


# def test_pop():
#     """Remove the first value at the head of the list. Return value."""
#     from linked_list import Node
#     from linked_list import LinkedList
#     from linked_list import test_pop
#     new_node = Node('cats', 'dogs')
#     assert some_list.pop() == 'cats'


# def test_head_is_true():
#     """Test if the node is the head."""
#     from linked_list import Node
#     from linked_list import LinkedList
#     from linked_list import head_is_true
#     new_node = Node('cats', 'dogs')
#     assert new_node.head is True


def test_insert_empty():
    """Test if inserts to head position."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('this')
    assert my_list.head is not None


# def test_remove():
#     """Remove a specific node."""
#     from linked_list import Node
#     from linked_list import LinkedList
#     from linked_list import remove
#     node1 = Node('1', 'dogs')
#     node2 = Node('dogs', 'cats')
#     node3 = Node('cats')
#     LinkedList.remove(node2)
#     assert LinkedList.search(node2) == -1


# def test_not_in_list():
#     """Test if node is in list."""
#     from linked_list import Node
#     from linked_list import LinkedList
#     from linked_list import search
#     from linked_list import test_not_in_list
#     node1 = Node('1', 'dogs')
#     node2 = Node('2', 'cats')
#     node3 = Node('3', 'people')
#     assert fake_list.search('not here') == -1
