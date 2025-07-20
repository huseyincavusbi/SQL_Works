from collections import deque

def topological_sort(graph):
    # Dictionary to store the in-degree of each node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
            
    # Queue for all nodes with an in-degree of 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    
    sorted_list = []
    
    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        
        # Decrement the in-degree of each neighbor
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add it to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
                
    if len(sorted_list) == len(graph):
        return sorted_list
    else:
        return "Graph has a cycle, topological sort not possible."

# Represent the graph using a dictionary (adjacency list)
# A -> B is represented as 'A': ['B']
morning_routine_graph = {
    'Wake Up': ['Exercise', 'Brush Teeth', 'Pack Lunch'],
    'Get Dressed': ['Shower'],
    'Eat Breakfast': ['Brush Teeth'],
    'Shower': ['Exercise'],
    'Pack Lunch': [],
    'Brush Teeth': [],
    'Exercise': []
}

# Get a valid list
valid_list = topological_sort(morning_routine_graph)
print("A valid list for the graph is:")
print(" -> ".join(valid_list))