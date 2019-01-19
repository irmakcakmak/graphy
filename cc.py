""" Connected component """

from graph import Graph

class CC():
    def __init__(self, graph):
        self.__graph = graph
        self.__marked = [None] * graph.size
        self.__edge_to = [None] * graph.size
        self.__current_vertex = 0
        for index in range(self.__graph.size):
            self.__current_vertex = index
            if not self.__marked[index]:
                self.__dfs(index)
                self.__edge_to[index] = index
        print(self.__edge_to)

    def __dfs(self, source):
        self.__marked[source] = True
        for v in self.__graph.adj(source):
            if not self.__marked[v]:
                self.__dfs(v)
                self.__edge_to[v] = self.__current_vertex

    def is_connected(self, v, w):
        return self.__edge_to[v] == self.__edge_to[w]

if __name__ == '__main__':
    g = Graph(10)
    g.add(1, 2)
    g.add(2, 3)
    g.add(3, 5)
    g.add(3, 4)
    g.add(5, 6)
    g.add(8, 9)
    g.add(7, 9)
    cc = CC(g)
    print(cc.is_connected(1, 6))
    print(cc.is_connected(0, 5))
    print(cc.is_connected(7, 9))
    print(cc.is_connected(6, 9))
