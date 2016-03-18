# -*- coding: utf-8 -*-
import pytest
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


def test_delete_edge_in_graph():
    """Test if an edge between two nodes is removed."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_node('egg')
    graph.add_edge('egg', 'chicken')
    graph.delete_edge('egg', 'chicken')
    assert graph.container['egg'] == []


def test_delete_edge_key_error():
    """Test if KeyError exception is raised."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('egg')
    with pytest.raises(KeyError):
        graph.delete_edge('dog', 'egg')


def test_delete_edge_value_error():
    """Test if ValueError exception is raised."""
    from simple_graph import Graph
    with pytest.raises(ValueError):
        graph = Graph()
        graph.add_node('egg')
        graph.delete_edge('egg', 'dog')


def test_neighbors():
    """Return the list of all nodes connect to node."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_node('egg')
    graph.add_edge('egg', 'chicken')
    assert graph.get_neighbors('egg') == ['chicken']


def test_neighbors_KeyError():
    """Test if KeyError raised."""
    from simple_graph import Graph
    with pytest.raises(KeyError):
        graph = Graph()
        graph.get_neighbors('monkey')
