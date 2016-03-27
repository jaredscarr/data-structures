# -*- coding: utf-8 -*-
import pytest


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


def test_add_edge_destination_node_not_exist():
    """Test if a node is added if it is the destination and does not exist."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_edge('chicken', 'egg')
    assert 'egg' in graph.container
    assert 'egg' in graph.container['chicken']



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
    assert graph.container['egg'] == {}


def test_delete_edge_key_error():
    """Test if KeyError exception is raised."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('egg')
    with pytest.raises(KeyError):
        graph.delete_edge('dog', 'egg')


def test_neighbors():
    """Return the list of all nodes connect to node."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_node('egg')
    graph.add_edge('egg', 'chicken')
    assert graph.get_neighbors('egg') == {'chicken': 0}


def test_neighbors_KeyError():
    """Test if KeyError raised."""
    from simple_graph import Graph
    with pytest.raises(KeyError):
        graph = Graph()
        graph.get_neighbors('monkey')


def test_adjacent_true():
    """Test if node returns true."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_node('egg')
    graph.add_edge('egg', 'chicken')
    assert graph.adjacent('egg', 'chicken') is True


def test_adjacent_false():
    """Test if returns false."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('chicken')
    graph.add_node('egg')
    assert graph.adjacent('egg', 'chicken') is False


def test_df_non_cycle():
    """Test if graph is traversed."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    assert graph.depth_first('a') == ['a']


def test_df_two_nodes():
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('a', 'b')
    assert graph.depth_first('a') == ['a', 'b']


def test_df_three_nodes():
    """Test if depth first with four nodes."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('d')
    graph.add_edge('a', 'b')
    graph.add_node('c')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'd')
    assert graph.depth_first('a') == ['a', 'b', 'c', 'd']


def test_df_three_nodes_complex():
    """Test depth first with even more nodes."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_edge('a', 'c')
    graph.add_edge('a', 'd')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'a')
    graph.add_edge('d', 'b')
    assert graph.depth_first('a') == ['a', 'c', 'd', 'b']


def test_bf_one_node():
    """Test breadth first traversal with one node."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    assert graph.breadth_first('a') == ['a']


def test_bf_two_nodes():
    """Test breadth first with two nodes."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_edge('a', 'b')
    assert graph.breadth_first('a') == ['a', 'b']


def test_bf_three_nodes():
    """Test breadth first with three nodes."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_edge('a', 'b')
    graph.add_edge('a', 'c')
    print(graph.container)
    assert graph.breadth_first('a') == ['a', 'b', 'c']


def test_bf_five_nodes():
    """Test breadth first with 5 nodes."""
    from simple_graph import Graph
    graph = Graph()
    graph.add_node('a')
    graph.add_node('b')
    graph.add_node('c')
    graph.add_node('d')
    graph.add_node('e')
    graph.add_edge('a', 'b')
    graph.add_edge('a', 'c')
    graph.add_edge('a', 'd')
    graph.add_edge('b', 'e')
    assert graph.breadth_first('a') == ['a', 'b', 'c', 'd', 'e']
