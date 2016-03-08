# -*- coding: utf-8 -*-


# node1 = Node('data')
# node2 = Node('dog')
# node3 = Node('Mimmy')

# STACK = Stack()


def test_node_init():
    """Test if Node object is there."""
    from stack import Node
    node = Node('data')
    assert node.data == 'data'


def test_stack_init():
    """Test if stack exists."""
    from stack import Stack
    init_stack = Stack()
    assert init_stack.top is None


def test_push():
    """Test if new node is added to the top of the linked list."""
    from stack import Stack, Node
    node1 = Node('this')
    a_stack = Stack()
    a_stack.push(node1)
    assert a_stack.top == node1
