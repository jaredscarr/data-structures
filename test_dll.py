# -*- coding: utf-8 -*-
import pytest


def test_node():
    """Assert node class is created with specified val."""
    from dll import Node
    new_node = Node(4)
    assert new_node.val == 4


def test_double_linked_list():
    """Assert a doubly linked list is created."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    assert my_list.head is None


def test_insert_on_empty_list():
    """Assert insert works."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(4)
    assert my_list.head.val == 4


def test_insert_on_non_emtpy_list():
    """Assert insert on non-empty list works."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(4)
    my_list.insert('Diana')
    assert my_list.head.val == 'Diana'


# TODO figure out how to test prvious node
def test_assert_previous():
    """Assert second node points to its previous."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert('Daniel')
    my_list.insert('Diana')
    assert my_list.head.val == 'Diana'


def test_tail():
    """Assert the last node is the tail."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(4)
    my_list.insert(5)
    my_list.insert(6)
    assert my_list.tail.val == 4


def test_append_non_empty():
    """Assert node gets appended to the end of the lsit."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(4)
    my_list.append(8)
    assert my_list.tail.val == 8


def test_append_empty():
    """Assert node gets appended to empty list."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.append(4)
    assert my_list.tail.val == 4


def test_pop_non_empty():
    """Assert first node gets removed and returned."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(4)
    my_list.insert(5)
    assert my_list.pop() == 5


def test_pop_single_item_list():
    """Test pop on single item list."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(4)
    my_list.pop()
    assert my_list.head is None


def test_pop_empty():
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    with pytest.raises(IndexError):
        my_list.pop()


def test_shift():
    """Assert shift works on non empty list."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(3)
    assert my_list.shift() == 1


def test_shift_single_item_list():
    """Test pop on single item list."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert(4)
    my_list.shift()
    assert my_list.head is None


def test_shift_empty():
    """Assert shift works on empty list."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    with pytest.raises(IndexError):
        my_list.shift()


def test_remove():
    """Test if selected Node is removed from list."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert('last')
    my_list.insert('second')
    my_list.insert('head')
    my_list.remove('second')
    assert my_list.head.next.val == 'last'


def test_remove_empty():
    """Assert remove works on empty list."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    with pytest.raises(AttributeError):
        my_list.remove('chicken')
