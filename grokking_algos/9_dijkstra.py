def dijkstra_visualized(graph, start_node, end_node):
    """
    Implements Dijkstra's algorithm and visualizes its steps.
    """
    print("--- Initializing Dijkstra's Algorithm ---")
    
    # 1. Initialize tables
    costs = {node: float('inf') for node in graph}
    costs[start_node] = 0
    
    parents = {node: None for node in graph}
    processed = []

    def find_lowest_cost_node(costs):
        """Finds the node with the lowest cost that hasn't been processed yet."""
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    # --- Main Loop ---
    print(f"Initial Costs: {costs}")
    print("-" * 30)
    
    node = find_lowest_cost_node(costs)
    step = 1
    while node is not None:
        print(f"--- Step {step}: Processing Node '{node}' ---")
        cost = costs[node]
        neighbors = graph[node]
        
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # If we found a cheaper path to the neighbor...
            if costs[n] > new_cost:
                # ...update the cost and parent for this neighbor.
                costs[n] = new_cost
                parents[n] = node
                print(f"  -> Found a cheaper path to '{n}'. New cost: {new_cost}, via '{node}'")
        
        # Mark the node as processed
        processed.append(node)
        print(f"Node '{node}' processed. Current costs: {costs}")
        
        # Find the next node to process
        node = find_lowest_cost_node(costs)
        step += 1
        print("-" * 30)
        
    # --- Reconstruct the final path ---
    print("\n--- Algorithm Finished. Reconstructing Path ---")
    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse() # Reverse to get the path from start to end

    print(f"Final Costs Table: {costs}")
    print(f"Final Parents Table: {parents}")
    print(f"\nShortest path from '{start_node}' to '{end_node}' is: {' -> '.join(path)}")
    print(f"Total Cost: {costs[end_node]}")

# --- Define the graph from our example ---
graph = {
    'Start': {'A': 6, 'B': 2},
    'A': {'Finish': 1},
    'B': {'A': 3, 'Finish': 5},
    'Finish': {}
}

dijkstra_visualized(graph, 'Start', 'Finish')