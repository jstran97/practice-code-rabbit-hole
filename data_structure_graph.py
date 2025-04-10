class Graph:

  def __init__(self):
    self.num_of_nodes = 0
    self.adjacency_list = {}  # Hash Table (Dictionary in Python)

  def add_vertex(self, node):
    if node not in self.adjacency_list.keys():
      # = [] is for adding vertices and connecting edges later
      self.adjacency_list[node] = []
      self.num_of_nodes += 1
    else:
      print(f"{node} already exists in the graph.")

  def add_edge(self, node1, node2):
    # Undirected graph - Nodes 1 and 2 point to each other
    self.adjacency_list[node1].append(node2)
    self.adjacency_list[node2].append(node1)

  def show_connections(self):
    for node in self.adjacency_list.keys():
      # List all of the node's adjacent vertices in a string
      node_connections = " ".join(self.adjacency_list[node])
      print(f"{node}-->{node_connections}")


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_vertex('6')  # Attempt to add dupe
graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2')
graph.add_edge('4', '5')
graph.add_edge('1', '2')
graph.add_edge('1', '0')
graph.add_edge('0', '2')
graph.add_edge('6', '5')

graph.show_connections()