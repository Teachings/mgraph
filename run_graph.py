from graph.setup import setup_graph

graph = setup_graph()

state = graph.state
for step in graph.execute():
    print(state)
