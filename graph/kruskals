class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []  # Stores edges as [source, destination, weight]

    def add_edge(self, s, d, w):
        # Kruskal's treats the graph as a list of edges
        self.graph.append([s, d, w])

    # Helper functions for Union-Find data structure
    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])  # Path compression
        return parent[i]

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        mst = []  # Stores the resulting MST edges
        
        # Step 1: Sort all edges in non-decreasing order of their weight
        self.graph.sort(key=lambda item: item[2])

        parent = list(range(self.V))
        rank = [0] * self.V

        edge_count = 0
        index = 0  # Index used to pick next edge

        # An MST always has exactly (V - 1) edges
        while edge_count < self.V - 1 and index < len(self.graph):
            s, d, w = self.graph[index]
            index += 1
            
            root_s = self.find(parent, s)
            root_d = self.find(parent, d)

            # Step 2: If including this edge doesn't cause a cycle, include it
            if root_s != root_d:
                edge_count += 1
                mst.append([s, d, w])
                self.union(parent, rank, root_s, root_d)
            # Else, discard the edge

        # Print the resulting MST
        print("Kruskal's MST Edges:")
        total_cost = 0
        for s, d, w in mst:
            print(f"{s} -- {d} == Weight: {w}")
            total_cost += w
        print(f"Total Minimum Cost: {total_cost}\n")


# Example Usage (matching your graph size)
kg = KruskalGraph(5)
kg.add_edge(0, 1, 10)
kg.add_edge(0, 4, 5)
kg.add_edge(1, 2, 1)
kg.add_edge(1, 4, 2)
kg.add_edge(2, 3, 4)
kg.add_edge(4, 2, 9)
kg.add_edge(4, 3, 2)

kg.kruskal_mst()
