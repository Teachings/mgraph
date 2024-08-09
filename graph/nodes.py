def node_setup(state):
    print("Executing Node setup")
    state.update('step', 'setup')
    return 'A'

def node_a(state):
    print("Executing Node A")
    state.update('step', 'A')
    return 'B'

def node_b(state):
    print("Executing Node B")
    state.update('step', 'B')
    #conditional edge logic
    if (2>1):
        return 'C'
    else:
        return 'D'

def node_d(state):
    print("Executing Node D")
    state.update('step', 'D')
    return 'END'

def node_c(state):
    print("Executing Node C")
    state.update('step', 'C')
    return 'END'

def end_node(state):
    print("Reached End Node")
    state.update('step', 'END')
    return None
