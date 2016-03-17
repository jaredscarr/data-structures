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
