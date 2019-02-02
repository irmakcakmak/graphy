from graph.edge import Edge
from graph import EdgeWeightedDirectedGraph
import math
from heapq import heappop, heappush


class Dijkstra(object):
    def __init__(self, edge_weighted_graph: EdgeWeightedDirectedGraph, source: int):
        self.__edge_to = [None] * edge_weighted_graph.size
        # vertex indexed array for distances to source
        self.__dist_to = [math.inf] * edge_weighted_graph.size
        self.__dist_to[source] = 0.0
        # put vertices and their distances to the source
        self.__pq = []
        s = [0.0, source]
        heappush(self.__pq, s)
        # keep references to the edges on the queue in this dict
        self.__pq_indices = {source: s}
        while self.__pq:
            elem = heappop(self.__pq)
            if not elem[0] == math.inf:
                self.__relax(edge_weighted_graph, elem)

    def __relax(self, g, _from):
        fro = _from[-1]
        for edge in g.adjacency_of(fro):
            to = edge.w
            dist = self.__dist_to[fro] + edge.weight
            if self.__dist_to[to] > dist:
                self.__dist_to[to] = dist
                self.__edge_to[to] = edge
                if to in self.__pq_indices:
                    dist_source = self.__pq_indices.pop(to)
                    dist_source[0] = math.inf
                    _to = [dist, dist_source[1]]
                    heappush(self.__pq, _to)
                    self.__pq_indices[dist_source[1]] = _to
                else:
                    dist_source = [dist, to]
                    self.__pq_indices[to] = dist_source
                    heappush(self.__pq, dist_source)

    def dist_to(self, vertex):
        return self.__dist_to[vertex]


if __name__ == '__main__':
    size = 8
    source = 0
    g = EdgeWeightedDirectedGraph(size)
    vertices = {i for i in range(size) if not i == source}
    g.add_edge(Edge(0, 1, 5))
    g.add_edge(Edge(0, 4, 9))
    g.add_edge(Edge(0, 7, 8))
    g.add_edge(Edge(1, 3, 15))
    g.add_edge(Edge(1, 2, 12))
    g.add_edge(Edge(1, 7, 4))
    g.add_edge(Edge(2, 3, 3))
    g.add_edge(Edge(2, 6, 11))
    g.add_edge(Edge(3, 6, 9))
    g.add_edge(Edge(4, 5, 4))
    g.add_edge(Edge(4, 6, 20))
    g.add_edge(Edge(4, 7, 5))
    g.add_edge(Edge(5, 2, 1))
    g.add_edge(Edge(5, 6, 13))
    g.add_edge(Edge(7, 2, 7))
    g.add_edge(Edge(7, 5, 6))
    dijsktra = Dijkstra(g, source)
    for vertex in vertices:
        print('distance of source vertex {} to vertex {} = {}'.format(source, vertex, dijsktra.dist_to(vertex)))

