# -*- coding: utf-8 -*-


def test_stack_init():
    """Test if stack exists."""
    from stack import Stack
    init_stack = Stack()
    assert init_stack.head is None


def test_push():
    """Test if new node is added to the top of the linked list."""
    from stack import Stack
    a_stack = Stack()
    a_stack.push('this')
    a_stack.push('that')
    assert a_stack.container.head.val == 'that'


def test_pop():
    """Test if node at head gets removed and returned."""
    from stack import Stack
    the_stack = Stack()
    the_stack.push('this')
    the_stack.push('that')
    assert the_stack.container.pop() == 'that'
