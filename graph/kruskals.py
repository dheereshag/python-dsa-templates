class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices
        # Flat edge list to align with how Kruskal's evaluates globally
        self.graph = []  

    def add_edge(self, s, d, w):
        # Consistent with your pattern of tracking complete (s, d, w) tuples
        self.graph.append([s, d, w])

    # Helper functions for Union-Find (Disjoint Set)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        mst_edges = []
        
        # Sort edges by weight (w is item[2])
        self.graph.sort(key=lambda item: item[2])

        parent = list(range(self.V))
        rank = [0] * self.V

        edge_count = 0
        index = 0  

        # An MST always has exactly V - 1 edges
        while edge_count < self.V - 1 and index < len(self.graph):
            # Consistently unpacking using s, d, w
            s, d, w = self.graph[index]
            index += 1
            
            root_s = self.find(parent, s)
            root_d = self.find(parent, d)

            # If adding this edge doesn't form a cycle
            if root_s != root_d:
                edge_count += 1
                mst_edges.append([s, d, w])
                self.union(parent, rank, root_s, root_d)

        # Print the resulting MST
        print("Kruskal's MST Edges:")
        total_cost = 0
        for s, d, w in mst_edges:
            print(f"{s} -- {d} == Weight: {w}")
            total_cost += w
        print(f"Total Minimum Cost: {total_cost}\n")


# Example Usage (matching your exact inputs)
kg = KruskalGraph(5)
kg.add_edge(0, 1, 10)
kg.add_edge(0, 4, 5)
kg.add_edge(1, 2, 1)
kg.add_edge(1, 4, 2)
kg.add_edge(2, 3, 4)
kg.add_edge(3, 2, 6)
kg.add_edge(3, 0, 7)
kg.add_edge(4, 1, 3)
kg.add_edge(4, 2, 9)
kg.add_edge(4, 3, 2)

kg.kruskal_mst()
