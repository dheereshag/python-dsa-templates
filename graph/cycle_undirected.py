class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph[u] acts as a "bucket" for all edges starting at u
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w=1):
        # Storing (source, destination, weight) using u, v, w
        self.graph[u].append((u, v, w))
        self.graph[v].append((v, u, w))

    def _has_cycle_dfs(self, u, visited, parent):
        # Mark the current node u as visited
        visited[u] = True

        # Check all neighboring nodes of u
        # We unpack using u, v, w (ignoring the redundant source u)
        for _, v, w in self.graph[u]:
            # If the neighbor v is not visited, recurse on it
            if not visited[v]:
                if self._has_cycle_dfs(v, visited, u):
                    return True
            # If an adjacent vertex v is visited and is NOT the parent of u,
            # then there is a cycle in the graph.
            elif v != parent:
                return True

        return False

    def has_cycle(self):
        # Track visited vertices across potential disconnected components
        visited = [False] * self.V

        # Loop through all vertices to handle disconnected graphs
        for i in range(self.V):
            if not visited[i]:
                # Start DFS with parent initialized as -1
                if self._has_cycle_dfs(i, visited, -1):
                    return True
                    
        return False

# --- Example Usage ---

print("Graph with a cycle:")
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 0)  # Completes the cycle 0-1-2-3-0

if g.has_cycle():
    print("Graph contains a cycle!")
else:
    print("Graph does not contain a cycle.")
