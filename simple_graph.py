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

    def has_node(self, value):
        """Check if node is in the graph."""
        return value in self.container

    def add_edge(self, pointer_node, destination_node):
        """Add edge between two nodes. If not in graph add nodes and edge."""
        self.container.setdefault(pointer_node, []).append(destination_node)

    def nodes(self):
        """Display a list of Nodes in the graph."""
        return self.container.keys()

    def edges(self):
        """Display a list of edges in the graph."""
        vals = list(self.container.values())
        new_list = []
        for items in vals:
            
