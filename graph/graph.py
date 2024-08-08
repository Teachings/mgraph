import time
import graphviz
from .state import State

class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.entry_point = None
        self.active_node = None
        self.state = State()
        self.graph_generator = None

    def add_node(self, name, func):
        self.nodes[name] = func

    def add_edge(self, from_node, to_node):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append(to_node)

    def set_entry_point(self, name):
        self.entry_point = name

    def execute(self):
        current_node = self.entry_point
        while current_node:
            self.active_node = current_node
            yield self.visualize(current_node)
            print(f"Executing {current_node}")
            time.sleep(1)  # Add delay to visualize the transition
            next_node = self.nodes[current_node](self.state)
            current_node = next_node

    def visualize(self, active_node=None):
        dot = graphviz.Digraph(comment='State Management Graph')
        for node in self.nodes:
            if node == active_node:
                dot.node(node, style='filled', color='lightblue')
            else:
                dot.node(node)
        for from_node, to_nodes in self.edges.items():
            for to_node in to_nodes:
                dot.edge(from_node, to_node)
        return dot.pipe(format='svg').decode('utf-8')
