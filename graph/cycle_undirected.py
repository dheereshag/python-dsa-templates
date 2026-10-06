from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph[u] acts as a "bucket" for all edges starting at u
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add undirected edge between u and v
        self.graph[u].append(v)
        self.graph[v].append(u)

    # --- Method 1: DFS with Parent Tracking ---
    def _has_cycle_dfs(self, u, visited, parent):
        # Mark the current node u as visited
        visited[u] = True

        # Check all neighboring nodes of u
        for v in self.graph[u]:
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
        """
        Detects cycles using DFS with parent tracking.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        # Track visited vertices across potential disconnected components
        visited = [False] * self.V

        # Loop through all vertices to handle disconnected graphs
        for i in range(self.V):
            if not visited[i]:
                # Start DFS with parent initialized as -1
                if self._has_cycle_dfs(i, visited, -1):
                    return True
                    
        return False

    # --- Method 2: BFS with Parent Tracking ---
    def _has_cycle_bfs(self, start, visited):
        # Queue stores pairs of (current_node, parent)
        queue = deque([(start, -1)])
        visited[start] = True

        while queue:
            u, parent = queue.popleft()

            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append((v, u))
                elif v != parent:
                    # Adjacent node is visited and is NOT the parent
                    return True

        return False

    def has_cycle_bfs(self):
        """
        Detects cycles using BFS with parent tracking.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = [False] * self.V

        # Loop through all vertices to handle disconnected graphs
        for i in range(self.V):
            if not visited[i]:
                if self._has_cycle_bfs(i, visited):
                    return True

        return False

# --- Example Usage ---

if __name__ == "__main__":
    print("Graph with a cycle:")
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)  # Completes the cycle 0-1-2-3-0

    print("DFS has_cycle:", g.has_cycle())         # True
    print("BFS has_cycle:", g.has_cycle_bfs())     # True
