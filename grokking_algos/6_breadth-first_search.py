from collections import deque

def bfs_shortest_path(graph, start, end):
    """
    Finds the shortest path in a graph using Breadth-First Search.
    Returns the path as a list of nodes.
    """
    # Queue will store paths, starting with the first node
    queue = deque([[start]])
    visited = {start}

    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        node = path[-1]

        # If we've reached the end, return the path
        if node == end:
            return path

        # Go through all neighbors of the current node
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Create a new path and add it to the queue
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    # If the queue becomes empty and we haven't found the end
    return None

# --- Graph for Exercise 6.1 ---
# S=Start, A=Top-Mid, B=Mid, C=Bottom-Mid, D=Bottom-Right, F=Finish
graph1 = {
    'S': ['A', 'C'],
    'A': ['B', 'F'],
    'B': ['C'],
    'C': ['D'],
    'D': ['F'],
    'F': []
}

# --- Graph for Exercise 6.2 ---
graph2 = {
    'CAB': ['CAR', 'CAT'],
    'CAR': ['CAT', 'BAR'],
    'CAT': ['MAT', 'BAT'],
    'BAR': ['BAT'],
    'MAT': ['BAT'],
    'BAT': []
}

# --- Solve and Print Results ---
print("--- Exercise 6.1 ---")
path1 = bfs_shortest_path(graph1, 'S', 'F')
if path1:
    # The length is the number of edges, which is number of nodes - 1
    print(f"Shortest path found: {' -> '.join(path1)}")
    print(f"Length of the shortest path: {len(path1) - 1}")
else:
    print("No path found.")

print("\n--- Exercise 6.2 ---")
path2 = bfs_shortest_path(graph2, 'CAB', 'BAT')
if path2:
    print(f"Shortest path found: {' -> '.join(path2)}")
    print(f"Length of the shortest path: {len(path2) - 1}")
else:
    print("No path found.")