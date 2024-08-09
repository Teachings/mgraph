# Graph Visualization Framework

This project is a lightweight and customizable framework built from the ground up to create and visualize stateful graphs in Python. It allows users to define nodes and their transitions, visualize the execution of these graphs in real-time via a web interface, and easily modify the graph’s behavior by altering just two files: `nodes.py` and `setup.py`.

The primary goal of this framework is to enable developers to define complex workflows or state machines as graphs, visualize their execution, and extend functionality for various use cases. Future enhancements will include additional visualization options, support for more complex node logic, and advanced real-time interaction features.

## Technical Architecture

The framework is composed of the following components:

1. **Node Definition (`nodes.py`)**: This file contains the logic for each node in the graph. A node represents a single step in the process and is responsible for updating the state and determining the next node.

2. **Graph Setup (`setup.py`)**: This file is used to define the structure of the graph. It connects nodes together, setting up the sequence of execution and the relationships between nodes.

3. **State Management (`state.py`)**: The `State` class manages the data shared between nodes during graph execution. Each node can read from and write to the state, allowing for dynamic transitions based on state data.

4. **Graph Execution (`graph.py`)**: This component drives the execution of the graph. It manages the progression through nodes, updates the state, and generates visual representations of the graph at each step.

5. **Web Interface**: The web interface, served by FastAPI, provides real-time visualization of the graph's execution. It uses WebSockets to update the graph and state display dynamically, ensuring that users can see the exact state of the graph at each step.

## Future Use Cases

Some of the planned enhancements for this framework include:
- **Complex Node Logic**: Support for conditional branching, looping, and parallel execution within nodes.
- **Enhanced Visualization**: More detailed and customizable graph visualizations, potentially including different layouts and styles.
- **Real-Time Interaction**: Allowing users to interact with the graph during execution, such as manually triggering nodes or altering the state.

## Setup Instructions

Follow these steps to set up the project on your local machine:

### Step 1: Install Graphviz
Graphviz is required for generating visual representations of the graph.

```bash
sudo apt-get install graphviz
```

### Step 2: Set Up the Python Environment
Create a new Conda environment for the project.

```bash
conda create -n mgraph python=3.12 pip
conda activate mgraph
```

### Step 3: Install Python Dependencies
Install the required Python packages using pip.

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
Start the FastAPI server to visualize the graph.

```bash
uvicorn app.main:app --reload
```

## Modifying the Graph

To define your own graph, you need to modify the following two files:

1. **`nodes.py`**: Define the logic for each node in your graph. A node typically updates the state and returns the name of the next node.

2. **`setup.py`**: Set up the structure of your graph. Here, you define the nodes and their relationships (i.e., which node follows which).

### Example
```python
# nodes.py
def node_a(state):
    print("Executing Node A")
    state.update('step', 'A')
    return 'B'

def node_b(state):
    print("Executing Node B")
    state.update('step', 'B')
    return 'C'

def node_c(state):
    print("Executing Node C")
    state.update('step', 'C')
    return 'END'
```

```python
# setup.py
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
```

## Summary

This project offers a powerful and flexible foundation for creating and visualizing stateful graphs. By following the setup instructions and modifying `nodes.py` and `setup.py`, you can quickly create your own custom workflows and visualize their execution in real-time. Keep an eye out for future updates as more features and capabilities are added!