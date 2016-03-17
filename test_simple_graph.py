# -*- coding: utf-8 -*-

# def test_display():
#     """Test that the graph displays."""
#     from simple_graph import 

def test_add_node():
    """Test if node added to graph."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    assert 'chicken' in graph.container


def test_not_in_graph():
    """Test if the Node is in the Graph."""
    from simple_graph import Graph
    graph = Graph()
    assert graph.has_node('chicken') is False


def test_in_graph():
    """Test if Node exists in Graph."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('monkey')
    assert graph.has_node('monkey') is True
