# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def linked_list():
    """Test fixture for linked list tests."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.insert('a')
    ll.insert('b')
    ll.insert('c')
    return ll


def test_node_class():
    """Test Node."""
    from linked_list import Node
    new_node = Node('caterpillar')
    assert new_node.val == 'caterpillar'


def test_search():
    """Search for node in list and return node."""
    from linked_list import LinkedList
    fake_list = LinkedList()
    fake_list.insert('that')
    assert fake_list.search('that') == fake_list.head


def test_size():
    """Test if size of list is returned."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('something')
    my_list.insert('something else')
    my_list.insert('Oh what the hell, one more thing.')
    assert my_list.size() == 3


def test_pop():
    """Assert first value was removed and returned."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('data')
    my_list.insert('more data')
    assert my_list.pop() == 'more data'


def test_head_is_true():
    """Test if the node is the head."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('this')
    assert my_list.head.val == 'this'


def test_insert_empty():
    """Test if inserts to head position."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('this')
    assert my_list.head is not None


def test_insert():
    """Test insert works."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    assert my_list.head.val == 'c'


def test_remove():
    """Test if node is in the middle it removes that val."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('a')
    my_list.insert('b')
    my_list.insert('c')
    my_list.remove('b')
    assert my_list.head.next.val == 'a'


def test_remove_last_node(linked_list):
    """Test can remove last node."""
    linked_list.remove('a')
    assert linked_list.head.next.next is None


def test_remove_one_node():
    """Test to remove one node."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('a')
    my_list.remove('a')
    assert my_list.head is None


def test_remove_error():
    """Test if error raised if the node does not exist."""
    from linked_list import LinkedList
    with pytest.raises(AttributeError):
        my_list = LinkedList()
        my_list.remove('test')


def test_iterable():
    """Assert iterable upacks and inserts to list."""
    from linked_list import LinkedList
    x = [1, 2, 3]
    my_list = LinkedList(x)
    assert my_list.display() == (3, 2, 1)
