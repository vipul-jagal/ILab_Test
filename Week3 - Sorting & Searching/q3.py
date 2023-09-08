# Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. You are given two arrays that represent the arrival and departure times of trains that stop.
# ( Instruction : optimise the algorithm )
# Input:
# arr[ ] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00},
# dep[ ] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
# Output: 3
# Explanation: There are at-most three trains at a time (time between 9:40 to 12:00)
# Input:
# arr[ ] = {9:00, 9:40},
# dep[ ] = {9:10, 12:00}
# Output: 1
# Explanation: Only one platform is needed.


def minPlatforms(arr, dep):
    # Sort the arrival and departure times in ascending order
    arr.sort()
    dep.sort()

    n = len(arr)
    platforms_needed = 1  # Initialize with one platform for the first train
    result = 1

    i = 1  # Pointer for arrival times
    j = 0  # Pointer for departure times

    while i < n and j < n:
        if arr[i] <= dep[j]:
            platforms_needed += 1
            i += 1
            if platforms_needed > result:
                result = platforms_needed
        else:
            platforms_needed -= 1
            j += 1

    return result

# Example usage:
arrival_times = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departure_times = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]

# Convert time strings to integers for easier comparison
arrival_times = [int(time.replace(":", "")) for time in arrival_times]
departure_times = [int(time.replace(":", "")) for time in departure_times]

platforms = minPlatforms(arrival_times, departure_times)
print("Minimum platforms required:", platforms)
