# -*- coding: utf-8 -*-


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


def test_assert_previous():
    """Assert second node points to its previous."""
    from dll import DoublyLinkedList
    my_list = DoublyLinkedList()
    my_list.insert('Daniel')
    my_list.insert('Diana')
    assert my_list.head.next == 'Daniel'






