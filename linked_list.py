# -*- coding: utf-8 -*-


class Node(object):
    """Construct Node object."""

    def __init__(self, data):
        """Initialize node object."""
        self.data = data
        self.next = None
