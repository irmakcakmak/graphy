class Graph():
    def __init__(self, size):
        self.__adj = [set() for x in range(size)]
        self.size = size

    def add(self, v, w):
        self.__adj[v].add(w)
        self.__adj[w].add(v)

    def adj(self, v):
        return self.__adj[v]

if __name__ == '__main__':
    g = Graph(5)
    g.add(1, 2)
    g.add(2, 4)
    g.add(2, 3)
    print(g.adj(2))
