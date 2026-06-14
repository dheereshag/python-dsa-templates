from heapq import heappush, heappop

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph[s] acts as a "bucket" for all edges starting at s
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, s, d, w):
        # Storing (source, destination, weight) for structural consistency
        self.graph[s].append((s, d, w))
        self.graph[d].append((d, s, w))

    def dijkstra(self, src, dest):
        # Initialize distances with infinity
        dist = [float("inf")] * self.V
        # Set distance of source node to 0
        dist[src] = 0

        # Create a priority queue
        pq = [(0, src)]
        # Initialize the parent array
        parent = [-1] * self.V

        while pq:
            # Get node with minimum distance from the priority queue
            (min_dist, s) = heappop(pq)

            # If we have reached the destination node, break out of the loop
            if s == dest:
                break

            # Check all neighboring nodes of s
            # We unpack the tuple completely, using '_' to ignore the redundant source
            for _, d, w in self.graph[s]:
                # If the distance to d through s is smaller than the current distance to d
                if dist[s] + w < dist[d]:
                    # Update the distance to d
                    dist[d] = dist[s] + w
                    # Set the parent of d to s
                    parent[d] = s
                    # Add d to the priority queue
                    heappush(pq, (dist[d], d))

        # If dest is unreachable, print an error message
        if parent[dest] == -1:
            print("Path not found!")
            return

        # Print the minimum distance to dest
        print("Minimum distance from", src, "to", dest, "is", dist[dest])

        # Find the path from src to dest
        path = []
        while dest != -1:
            path.append(dest)
            dest = parent[dest]

        # Reverse the path to print it in the correct order
        path.reverse()

        # Print the path
        print("The path is:", " -> ".join(map(str, path)))

# Example usage
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 4, 5)
g.add_edge(1, 2, 1)
g.add_edge(1, 4, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 2, 6)
g.add_edge(3, 0, 7)
g.add_edge(4, 1, 3)
g.add_edge(4, 2, 9)
g.add_edge(4, 3, 2)

g.dijkstra(0, 2)
