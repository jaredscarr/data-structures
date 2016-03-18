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


def test_add_edge():
    """Test if there is an edge between two nodes."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_node('egg')
    graph.add_edge('egg', 'chicken')
    assert 'chicken' in graph.container['egg']


def test_delete_node():
    """Delete selected node."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_node('egg')
    graph.delete_node('chicken')
    assert 'chicken' not in graph.container
