
# This file implements a Graph using an adjacency list, and includes BFS and DFS traversals.
from collections import deque

class Graph:
    def __init__(self):
        """Initializes a graph using an adjacency list (a dictionary)."""
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Adds a vertex to the graph if it's not already there."""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        """Adds an edge between two vertices (undirected graph)."""
        # Ensure both vertices exist in the graph
        if v1 not in self.adj_list:
            self.add_vertex(v1)
        if v2 not in self.adj_list:
            self.add_vertex(v2)
        # Add the edge
        self.adj_list[v1].append(v2)
        self.adj_list[v2].append(v1) # For an undirected graph

    def display(self):
        """Displays the adjacency list representation of the graph."""
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

    # --- Traversal Algorithms ---

    def bfs(self, start_vertex):
        """Performs a Breadth-First Search starting from a given vertex. Time complexity: O(V + E)"""
        if start_vertex not in self.adj_list:
            print(f"Vertex {start_vertex} not in graph.")
            return
        
        visited = set()
        queue = deque([start_vertex])
        traversal_order = []

        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                visited.add(current_vertex)
                traversal_order.append(current_vertex)
                # Add unvisited neighbors to the queue
                for neighbor in self.adj_list[current_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        print(f"BFS starting from {start_vertex}: {' -> '.join(traversal_order)}")

    def dfs(self, start_vertex):
        """Performs a Depth-First Search starting from a given vertex. Time complexity: O(V + E)"""
        if start_vertex not in self.adj_list:
            print(f"Vertex {start_vertex} not in graph.")
            return

        visited = set()
        stack = [start_vertex]
        traversal_order = []

        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                traversal_order.append(current_vertex)
                # Add unvisited neighbors to the stack (in reverse to maintain order)
                for neighbor in reversed(self.adj_list[current_vertex]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        print(f"DFS starting from {start_vertex}: {' -> '.join(traversal_order)}")

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Graph Demonstration ---")
    g = Graph()

    print("\nAdding edges to the graph:")
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('E', 'F')

    print("\nGraph Adjacency List:")
    g.display()

    print("\n--- Traversals ---")
    g.bfs('A')
    g.dfs('A')
