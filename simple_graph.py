# -*- coding: utf-8 -*-
class Node(object):
    """Node."""

    def __init__(self, value):
        """Init Node."""
        self.value = value


class Graph(object):
    """The Graph."""

    def __init__(self):
        """Init Graph."""
        self.container = {}

    def add_node(self, value):
        """Add node to Graph."""
        self.container.setdefault(value, [])
