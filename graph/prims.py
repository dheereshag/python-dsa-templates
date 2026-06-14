from heapq import heappush, heappop

class PrimGraph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph[u] acts as a "bucket" for all edges starting at u
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        # Storing (u, v, w) for structural consistency
        # MSTs are built on undirected graphs, so we add both directions
        self.graph[u].append((u, v, w))
        self.graph[v].append((v, u, w))

    def prim_mst(self, src):
        # Track if a vertex is already included in the MST
        in_mst = [False] * self.V
        
        # Initialize the parent array
        parent = [-1] * self.V
        
        # Key values used to pick minimum weight edge
        key = [float('inf')] * self.V
        key[src] = 0

        # Create a priority queue (stores weight, node)
        pq = [(0, src)]
        
        total_cost = 0
        mst_edges = []

        while pq:
            # Get node with minimum key value from the priority queue
            weight, u = heappop(pq)

            # If the vertex is already in MST, skip it to avoid cycles
            if in_mst[u]:
                continue

            # Add vertex to MST
            in_mst[u] = True
            total_cost += weight
            
            # Record the edge (except for the initial source node)
            if parent[u] != -1:
                mst_edges.append((parent[u], u, weight))

            # Check all neighboring nodes of u
            # We unpack the tuple completely, using '_' to ignore the redundant entry
            for _, v, w in self.graph[u]:
                # If v is not yet in MST and edge weight is smaller than current key of v
                if not in_mst[v] and w < key[v]:
                    # Update key and parent
                    key[v] = w
                    parent[v] = u
                    heappush(pq, (key[v], v))

        # Print the resulting MST
        print("Prim's MST Edges:")
        for u, v, w in mst_edges:
            print(f"{u} -- {v} == Weight: {w}")
        print(f"Total Minimum Cost: {total_cost}\n")


# Example Usage
pg = PrimGraph(5)
pg.add_edge(0, 1, 10)
pg.add_edge(0, 4, 5)
pg.add_edge(1, 2, 1)
pg.add_edge(1, 4, 2)
pg.add_edge(2, 3, 4)
pg.add_edge(3, 2, 6)
pg.add_edge(3, 0, 7)
pg.add_edge(4, 1, 3)
pg.add_edge(4, 2, 9)
pg.add_edge(4, 3, 2)

pg.prim_mst(0)
