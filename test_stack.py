# -*- coding: utf-8 -*-


def test_stack_init():
    """Test if stack exists."""
    from stack import Stack
    init_stack = Stack()
    assert init_stack.top is None


def test_push():
    """Test if new node is added to the top of the linked list."""
    from stack import Stack
    a_stack = Stack()
    a_stack.push('this')
    a_stack.push('that')
    assert a_stack.head == 'that'
