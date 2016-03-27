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
        if value in self.container:
            pass
        else:
            self.container[value] = {}
        # self.container.setdefault(value, [])

    def has_node(self, value):
        """Check if node is in the graph."""
        return value in self.container

    def add_edge(self, pointer_node, destination_node, weight=0):
        """Add edge between two nodes. If not in graph add nodes and edge."""
        # if destination_node not in self.container:
        #     self.add_node(destination_node)
        # self.container.setdefault(pointer_node, []).append(destination_node)
        if pointer_node not in self.container:
            self.add_node(pointer_node)
        if destination_node not in self.container:
            self.add_node(destination_node)
        if destination_node in self.container[pointer_node]:
            pass
        else:
            self.container[pointer_node][destination_node] = weight

    def nodes(self):
        """Display a list of Nodes in the graph."""
        return self.container.keys()

    def edges(self):
        """Display a list of edges in the graph."""
        edges = [(key, value) for key in self.container for value in self.container[key]]
        return edges

    def delete_node(self, node):
        """Delete a node from the graph or return not in graph."""
        if self.has_node(node) is False:
            print('That node does not exist in the graph.')
        else:
            del self.container[node]

    def delete_edge(self, node1, node2):
        """Delete an edge from the graph or return not in graph."""
        try:
            self.container[node1].remove(node2)
        except KeyError:
            raise KeyError('The key you chose does not exist.')
        except ValueError:
            raise ValueError('The second node is not in the list of values')

    def get_neighbors(self, node):
        """Return a list of neighbors."""
        try:
            return self.container[node]
        except KeyError:
            raise KeyError('That node is not in the graph.')

    def adjacent(self, node1, node2):
        """Return weather or not two nodes are adjacent."""
        if self.has_node(node1) and self.has_node(node2):
            return node2 in self.container[node1]

    def depth_first(self, start, visited=[]):
        """Return list of visited nodes using depth first."""
        visited = visited + [start]
        for edge in self.container[start]:
            if edge not in visited:
                visited = self.depth_first(edge, visited)
        return visited

    def breadth_first(self, start):
        """Return a list of visited nodes using breadth first."""
        from collections import deque
        visited, queue = [], deque([start])
        try:
            while len(queue) > 0:
                node = queue.pop()
                if node not in visited:
                    visited.append(node)
                    for edge in self.container[node]:
                        queue.appendleft(edge)
            return visited
        except (TypeError, KeyError):
            return visited
