# -*- coding: utf-8 -*-


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


def test_size():
    """Test if size of list is returned."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('something')
    my_list.insert('something else')
    my_list.insert('Oh what the hell, one more thing.')
    assert my_list.size() == 3


def test_display():
    """Print the list."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert(1)
    my_list.insert(2)
    assert my_list.size() == len(my_list.display())


def test_pop():
    """Assert first value was removed and returned."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('data')
    my_list.insert('more data')
    assert my_list.pop() == 'more data'


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


def test_remove():
    """Remove a specific node."""
    from linked_list import LinkedList
    my_list = LinkedList()
    my_list.insert('Hey, Im a value')
    my_list.insert('b')
    my_list.remove('b')
    assert my_list.head.val == 'b'

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
