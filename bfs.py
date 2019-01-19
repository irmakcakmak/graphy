from graph import Graph
from collections import deque

class BFS():
    def __init__(self, graph, source):
        self.__marked = [None] * graph.size
        self.__edge_to = [None] * graph.size
        self.__graph = graph
        self.__source = source
        self._bfs()

    def _bfs(self):
        queue = deque([])
        queue.append(self.__source)
        while(queue):
            root = queue.popleft()
            self.__marked[root] = True
            for v in self.__graph.adj(root):
                if not self.__marked[v]:
                    queue.append(v)
                    self.__edge_to[v] = root

    @property
    def edge_to(self):
        return self.__edge_to

if __name__ == '__main__':
    g = Graph(7)
    g.add(1, 2)
    g.add(2, 3)
    g.add(3, 5)
    g.add(3, 4)
    g.add(5, 6)
    b = BFS(g, 1)
    print(b.edge_to)


