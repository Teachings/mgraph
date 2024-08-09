from .graph import Graph
from .nodes import node_setup, node_a, node_b, node_c, node_d, end_node

def setup_graph():
    #define graph
    graph = Graph()

    #Step 1: creates nodes
    graph.add_node('setup', node_setup)
    graph.add_node('A', node_a)
    graph.add_node('B', node_b)
    graph.add_node('C', node_c)
    graph.add_node('D', node_d)
    graph.add_node('END', end_node)

    #Step 2: create entrypoints
    graph.set_entry_point('setup')

    #Step 3: create edges
    graph.add_edge('setup', 'A')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'END')
    graph.add_edge('D', 'END')

    return graph
