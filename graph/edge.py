class Edge(object):
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def __eq__(self, other):
        return self.v == other.v and self.w == other.w

    def __str__(self):
        return '{} ---({})--> {}'.format(self.v, self.weight, self.w)

    def __repr__(self):
        return '({}--{}->{})'.format(self.v, self.weight, self.w)

    def __hash__(self):
        return hash((self.v, self.w))


if __name__ == '__main__':
    a = Edge(1, 2, 29.99999999999998)
    b = Edge(4, 5, 29.99999999999999)
    import heapq
    pq = []
    heapq.heappush(pq, a)
    heapq.heappush(pq, b)
    print(heapq.heappop(pq))
    print(heapq.heappop(pq))
