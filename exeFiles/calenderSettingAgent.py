from langgraph.graph import Graph, START, END


def function_1(input_1):
    return input_1 + " I am "

def function_2(input_2):
    return input_2 + "happy"



# Define a graph
workflow = Graph()

# define nodes
workflow.add_node("node_1", function_1)
workflow.add_node("node_2", function_2)

# define edges
workflow.add_edge(START, 'node_1')
workflow.add_edge('node_1', 'node_2')
workflow.add_edge('node_2', END)

graph = workflow.compile()


print(graph.invoke("hello there"))

from IPython.display import Image

# View
display(Image(graph.get_graph().draw_mermaid_png()))