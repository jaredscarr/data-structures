"""Module to detect status of sequence of parens."""
from stack import Stack


def match_parens(string):
    """Return whether the string contains mathing perens or not."""
    if string[0] == ')':
        return -1
    my_stack = Stack()
    for char in string:
        if char == '(':
            my_stack.push(char)
        elif char == ')' and my_stack.container.head is not None:
            my_stack.pop()
    if my_stack.container.head is None:
        return 0
    else:
        return 1

