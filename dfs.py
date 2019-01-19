from graph import Graph

class DFS():
    def __init__(self, graph, source):
        self.__marked = [None] * graph.size
        self.__edge_to = [None] * graph.size
        self.__graph = graph
        self.__source = source
        self._dfs(source)

    def _dfs(self, source):
        self.__marked[source] = True
        for x in self.__graph.adj(source):
            if not self.__marked[x]:
                self._dfs(x)
                self.__edge_to[x] = source

    def has_path_to(self, target):
        return self.__marked[target] is not None

    def path_to(self, target):
        x = target
        path = []
        while self.__edge_to[x] and x != self.__source:
            path.append(x)
            x = self.__edge_to[x]
        path.append(self.__source)
        path.reverse()
        return path



if __name__ == '__main__':
    g = Graph(7)
    g.add(1, 2)
    g.add(2, 3)
    g.add(3, 5)
    g.add(3, 4)
    g.add(5, 6)
    d = DFS(g, 1)
    print(' -> '.join([str(v) for v in d.path_to(6)]))
