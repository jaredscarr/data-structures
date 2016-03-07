# -*- coding: utf-8 -*-

import pytest


def test_node_class():
    """Test Node."""
    from linked_list import Node
    new_node = Node('caterpillar')
    assert new_node.data == 'caterpillar'
