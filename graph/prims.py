from heapq import heappush, heappop

class PrimGraph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph[s] acts as a bucket for all edges starting at s
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, s, d, w):
        # Storing (source, destination, weight) for consistency
        # MSTs are built on undirected graphs, so we add both directions
        self.graph[s].append((s, d, w))
        self.graph[d].append((d, s, w))

    def prim_mst(self, start_vertex=0):
        # Track if a vertex is already included in the MST
        in_mst = [False] * self.V
        
        # Stores the parent of each node in the MST structure
        parent = [-1] * self.V
        
        # Key values used to pick minimum weight edge in cut
        key = [float('inf')] * self.V
        key[start_vertex] = 0

        # Priority queue stores tuples of (edge_weight, vertex)
        pq = [(0, start_vertex)]
        
        total_cost = 0
        mst_edges = []

        while pq:
            # Pick the vertex with the minimum key value
            weight, u = heappop(pq)

            # If the vertex is already in MST, skip it to avoid cycles
            if in_mst[u]:
                continue

            # Add vertex to MST
            in_mst[u] = True
            total_cost += weight
            
            # Record the edge (except for the starting root node)
            if parent[u] != -1:
                mst_edges.append((parent[u], u, weight))

            # Look at all adjacent vertices of u
            # We unpack the tuple completely, using '_' to ignore the redundant source
            for _, v, w in self.graph[u]:
                # If v is not yet in MST and weight of (u,v) is smaller than current key of v
                if not in_mst[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
                    heappush(pq, (key[v], v))

        # Print the resulting MST
        print("Prim's MST Edges:")
        for s, d, w in mst_edges:
            print(f"{s} -- {d} == Weight: {w}")
        print(f"Total Minimum Cost: {total_cost}\n")


# Example Usage
pg = PrimGraph(5)
pg.add_edge(0, 1, 10)
pg.add_edge(0, 4, 5)
pg.add_edge(1, 2, 1)
pg.add_edge(1, 4, 2)
pg.add_edge(2, 3, 4)
pg.add_edge(4, 2, 9)
pg.add_edge(4, 3, 2)

pg.prim_mst(0)
