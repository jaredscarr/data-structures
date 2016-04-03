"""Module to detect status of sequence of parens."""
from stack import Stack


def match_parens(string):
    """Return whether the string contains mathing perens or not."""
    char_list = []
    for char in string:
        if char == '(' or char == ')':
            char_list.append(char)
    if char_list[0] == ')':
        return -1
    my_stack = Stack()
    for char in string:
        if char == '(':
            my_stack.push(char)
        elif char == ')':
            my_stack.pop()
    if my_stack.container.head is None:
        return 0
    else:
        return 1

