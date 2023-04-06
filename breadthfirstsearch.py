# vertex definition
class Vertex:
    def __init__(self, label):
        self.label = label
        self.neighbors = []

    def __str__(self):
        return self.label

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
        self.neighbors.sort()


# graph definition
class Graph:
    def __init__(self):
        self.vertices = []

    # adds a vertex object
    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    # gets index of a vertex with corresponding label
    # returns -1 if not found
    def get_vertex_index(self, label):
        index = 0
        for vertex in self.vertices:
            if label == str(vertex):
                return index
            index += 1
        return -1

    # finds a vertex with corresponding label and return as Vertex object
    def find_vertex(self, label):
        for vertex in self.vertices:
            if label == str(vertex):
                return vertex
        return None

    # adds an edge from a vertex with from_label to a vertex with to_label
    # vertices must already exist in the graph
    def add_edge(self, from_label, to_label):
        source_vertex = self.find_vertex(from_label)
        dest_vertex = self.find_vertex(to_label)
        if source_vertex is not None and dest_vertex is not None:
            source_vertex.add_neighbor(to_label)

def breadthFirst(g, start_label):
    visited = []  # tracks visited nodes
    queue = []  # queue initialization
    vertex_start = g.find_vertex(start_label)
    # appends lists from above
    queue.append(vertex_start)
    visited.append(vertex_start)

    while len(queue) > 0:
        c = queue.pop(0)
        for neighbor in c.neighbors:
            neighbor = g.find_vertex(neighbor)
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)

    label = [str(vertex) for vertex in visited]
    return label

if __name__ == "__main__":
    # test
    my_graph = Graph()
    vertices = ["0", "1", "2", "3", "4", "5"]
    edges = [["0", "1"], ["0", "2"], ["1", "3"], ["1", "4"], ["2", "5"]]

    for vertex in vertices:
        my_graph.add_vertex(Vertex(vertex))

    for edge in edges:
        my_graph.add_edge(edge[0], edge[1])

    for vertex in my_graph.vertices:  # prints adjacency list
        print("Vertex ", vertex, ":", vertex.neighbors)

    print(breadthFirst(my_graph, "0"))  # expected: ["0","1","2","3","4","5"]
