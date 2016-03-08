# -*- coding: utf-8 -*-


def test_node_init():
    """Test if Node object is there."""
    from stack import Node
    node = Node('data')
    assert node.data == 'data'
