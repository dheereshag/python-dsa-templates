from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)

    def bfs(self, start):
        """Traverse the graph in breadth-first order from the given start node."""
        visited = [False] * self.vertices
        traversal = []
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            traversal.append(node)
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return traversal


# Example usage

graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
print(graph.bfs(0))
