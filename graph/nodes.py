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

def end_node(state):
    print("Reached End Node")
    state.update('step', 'END')
    return None
