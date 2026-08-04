class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)

    def dfs(self, start):
        """Traverse the graph in depth-first order from the given start node."""
        visited = [False] * self.vertices
        traversal = []

        def visit(node):
            visited[node] = True
            traversal.append(node)
            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visit(neighbor)

        visit(start)
        return traversal


# Example usage

graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
print(graph.dfs(0))
