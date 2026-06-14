from heapq import heappush, heappop

class PrimGraph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph[s] acts as a "bucket" for all edges starting at s
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, s, d, w):
        # Storing (source, destination, weight) for structural consistency
        self.graph[s].append((s, d, w))
        self.graph[d].append((d, s, w))

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
            weight, s = heappop(pq)

            # If the vertex is already in MST, skip it to avoid cycles
            if in_mst[s]:
                continue

            # Add vertex to MST
            in_mst[s] = True
            total_cost += weight
            
            # Record the edge (except for the initial source node)
            if parent[s] != -1:
                mst_edges.append((parent[s], s, weight))

            # Check all neighboring nodes of s
            for _, d, w in self.graph[s]:
                # If d is not yet in MST and edge weight is smaller than current key of d
                if not in_mst[d] and w < key[d]:
                    # Update key and parent
                    key[d] = w
                    parent[d] = s
                    heappush(pq, (key[d], d))

        # Print the resulting MST
        print("Prim's MST Edges:")
        for s, d, w in mst_edges:
            print(f"{s} -- {d} == Weight: {w}")
        print(f"Total Minimum Cost: {total_cost}\n")


# Example Usage (matching your exact inputs)
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
