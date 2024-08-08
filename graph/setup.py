from .graph import Graph
from .nodes import node_a, node_b, node_c, end_node

def setup_graph():
    graph = Graph()
    graph.add_node('A', node_a)
    graph.add_node('B', node_b)
    graph.add_node('C', node_c)
    graph.add_node('END', end_node)
    graph.set_entry_point('A')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'END')
    return graph
