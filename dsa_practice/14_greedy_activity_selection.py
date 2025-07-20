
# This file demonstrates a Greedy Algorithm with the Activity Selection Problem.

def activity_selection(start, finish):
    """
    Selects the maximum number of non-overlapping activities.
    The greedy choice is to always pick the activity that finishes earliest.
    :param start: A list of start times for the activities.
    :param finish: A list of finish times for the activities.
    :return: A list of the indices of the selected activities.
    Time Complexity: O(n log n) due to sorting.
    Space Complexity: O(n) to store the activities.
    """
    n = len(finish)
    # Combine start and finish times into a list of activities [start, finish, original_index]
    activities = sorted([[start[i], finish[i], i] for i in range(n)], key=lambda x: x[1])

    # The first activity always gets selected
    selected_activities_indices = []
    if n > 0:
        selected_activities_indices.append(activities[0][2])
        # The finish time of the most recently selected activity
        last_finish_time = activities[0][1]

        # Iterate through the rest of the activities
        for i in range(1, n):
            # If this activity has a start time that is greater than or equal to the
            # finish time of the previously selected activity, then select it
            if activities[i][0] >= last_finish_time:
                selected_activities_indices.append(activities[i][2])
                last_finish_time = activities[i][1]

    return selected_activities_indices

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Greedy Algorithm: Activity Selection Demonstration ---")

    start_times = [1, 3, 0, 5, 8, 5]
    finish_times = [2, 4, 6, 7, 9, 9]
    
    print(f"\nStart Times:  {start_times}")
    print(f"Finish Times: {finish_times}")

    selected_indices = activity_selection(start_times, finish_times)

    print(f"\nIndices of selected activities: {selected_indices}")
    print("Selected activities (start, finish):")
    for index in selected_indices:
        print(f"  Activity {index}: ({start_times[index]}, {finish_times[index]})")
