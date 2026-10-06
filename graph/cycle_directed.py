from collections import deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph[u] acts as a "bucket" for all directed edges starting at u
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Directed edge from u to v: store destination v
        self.graph[u].append(v)

    # --- Method 1: DFS with Path Tracking (Back-edge detection) ---
    def _dfs_directed_path_cycle(self, u, visited, path):
        # Mark current node as visited and append it to the active path
        visited[u] = True
        path.add(u)

        # Check all outgoing edges (u -> v)
        for v in self.graph[u]:
            # If neighbor v is already in the current path,
            # this edge (u -> v) is a back-edge, confirming a cycle.
            if v in path:
                return True
            # If neighbor v is not visited, recurse on it
            if not visited[v]:
                if self._dfs_directed_path_cycle(v, visited, path):
                    return True

        # Backtrack: remove current node from the active path
        path.remove(u)
        return False

    def has_cycle(self):
        """
        Detects cycles using DFS and tracking the current traversal path.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        visited = [False] * self.V
        path = set()

        # Loop through all vertices to handle disconnected components
        for i in range(self.V):
            if not visited[i]:
                if self._dfs_directed_path_cycle(i, visited, path):
                    return True

        return False

    # --- Method 2: BFS using Kahn's Algorithm (Topological Sort) ---
    def has_cycle_bfs(self):
        """
        Detects cycles using Kahn's Algorithm (in-degree count & BFS).
        If topological sort cannot include all V vertices, a cycle exists.
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        # Calculate in-degrees of all vertices
        in_degree = [0] * self.V
        for u in range(self.V):
            for v in self.graph[u]:
                in_degree[v] += 1

        # Push all vertices with 0 in-degree to the queue
        queue = deque([u for u in range(self.V) if in_degree[u] == 0])
        visited_count = 0

        while queue:
            u = queue.popleft()
            visited_count += 1

            # Decrement in-degree of outgoing neighbors
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        # If visited vertices count is not equal to total vertices,
        # there is at least one cycle.
        return visited_count != self.V

    # --- Method 3: DFS using 3-Coloring Algorithm ---
    def _dfs_directed_color_cycle(self, u, color):
        # Constants for clarity:
        # WHITE = 0 (unvisited)
        # GRAY  = 1 (currently visiting / in active DFS recursion path)
        # BLACK = 2 (completely visited / all descendants explored)

        # Mark current node as GRAY
        color[u] = 1

        for v in self.graph[u]:
            # If neighbor is GRAY, we found a back-edge to an ancestor (cycle detected)
            if color[v] == 1:
                return True
            # If neighbor is WHITE, recurse on it
            if color[v] == 0:
                if self._dfs_directed_color_cycle(v, color):
                    return True

        # Mark current node as BLACK (completely processed)
        color[u] = 2
        return False

    def has_cycle_colors(self):
        """
        Detects cycles using the 3-Coloring algorithm:
          0 (WHITE): unvisited
          1 (GRAY):  visiting (in active path)
          2 (BLACK): fully visited
        Time Complexity: O(V + E)
        Space Complexity: O(V)
        """
        # All vertices start as WHITE (0)
        color = [0] * self.V

        # Loop through all vertices to handle disconnected components
        for i in range(self.V):
            if color[i] == 0:
                if self._dfs_directed_color_cycle(i, color):
                    return True

        return False


# --- Example Usage ---

if __name__ == "__main__":
    print("=== Example 1: Directed Graph with a Cycle ===")
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 1)  # Cycle: 1 -> 2 -> 3 -> 1

    print("DFS has_cycle:       ", g1.has_cycle())         # True
    print("BFS has_cycle:       ", g1.has_cycle_bfs())     # True
    print("3-Color has_cycle:   ", g1.has_cycle_colors())  # True

    print("\n=== Example 2: Directed Acyclic Graph (DAG) ===")
    # Diamond structure: 0 -> 1 -> 3 and 0 -> 2 -> 3
    # Vertex 3 is reached by two different paths, but no cycle exists.
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)

    print("DFS has_cycle:       ", g2.has_cycle())         # False
    print("BFS has_cycle:       ", g2.has_cycle_bfs())     # False
    print("3-Color has_cycle:   ", g2.has_cycle_colors())  # False
