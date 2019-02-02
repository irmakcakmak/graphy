from graph.edge import Edge


class Graph:
    def __init__(self, size):
        self.__adj = [set() for x in range(size)]
        self.size = size

    def add(self, v, w):
        self.__adj[v].add(w)
        self.__adj[w].add(v)

    def adj(self, v):
        return self.__adj[v]


class EdgeWeightedDirectedGraph:
    def __init__(self, size):
        self.__adj = [set() for i in range(size)]
        self.size = size

    def add_edge(self, edge):
        if edge in self.__adj[edge.v]:
            self.__adj[edge.v].remove(edge)
        self.__adj[edge.v].add(edge)

    def adjacency_of(self, vertex):
        return self.__adj[vertex]


if __name__ == '__main__':
    g = EdgeWeightedDirectedGraph(5)
    g.add_edge(Edge(1, 2, 12))
    g.add_edge(Edge(2, 4, 13))
    g.add_edge(Edge(2, 3, 4))
    g.add_edge(Edge(2, 3, 5))
    g.add_edge(Edge(2, 5, 4))
    for i in g.adjacency_of(2):
        print(i)
