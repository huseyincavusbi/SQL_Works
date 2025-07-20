def greedy_set_cover(states_to_cover, available_stations):
    """
    Finds an approximate solution to the set cover problem using a greedy algorithm.
    
    :param states_to_cover: A set of all items that need to be covered.
    :param available_stations: A dictionary where keys are station names and 
                               values are sets of items they cover.
    :return: A set of the names of the stations selected.
    """
    print("--- Starting Greedy Set Cover Algorithm ---")
    
    final_stations = set()
    states_needed = states_to_cover.copy() # Work with a copy
    
    step = 1
    # Loop as long as there are states we still need to cover
    while states_needed:
        print(f"\n--- Step {step} ---")
        print(f"States still needed: {states_needed}")
        
        best_station = None
        states_covered_by_best_station = set()
        
        # Iterate through all available stations to find the best one for this step
        for station, states_for_station in available_stations.items():
            # Find the intersection: which of the needed states are covered by THIS station?
            covered = states_needed.intersection(states_for_station)
            
            # If this station covers more states than our current best, update our best
            if len(covered) > len(states_covered_by_best_station):
                best_station = station
                states_covered_by_best_station = covered
        
        # If we found a station that covers at least one needed state
        if best_station:
            print(f"Greedy Choice: Chose '{best_station}' because it covers the most new states: {states_covered_by_best_station}")
            # Add the best station to our final list
            final_stations.add(best_station)
            # Remove the newly covered states from our list of needed states
            states_needed -= states_covered_by_best_station
        else:
            # This would happen if no station covers any of the remaining needed states
            print("Could not cover all states. Aborting.")
            break
            
        step += 1
        
    return final_stations

# The universe of items we need to cover
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# The collection of available subsets (stations)
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

# --- Run the algorithm ---
selected_stations = greedy_set_cover(states_needed, stations)

print("\n\n--- Algorithm Finished ---")
print(f"The selected stations are: {selected_stations}")

