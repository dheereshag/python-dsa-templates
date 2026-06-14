class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def bellman_ford(self, source, dest):
        dist = [float("Inf")] * self.V
        dist[source] = 0
        parent = [-1] * self.V

        for i in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                    parent[d] = s

        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        path = []
        d = dest
        while d != -1:
            path.append(d)
            d = parent[d]
        path.reverse()

        print(
            f"The shortest path from {source} to {dest} is: {' -> '.join(map(str, path))}")
        print(f"The distance is: {dist[dest]}")


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0, 3)
