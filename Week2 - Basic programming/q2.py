# Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.
# Note: There are no duplicates in the list.
# Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
# Output: 5
# Explanation: The missing number between 1 to 8 is 5

def find_missing_number(arr, N):
    # Calculate the expected sum of the first N natural numbers
    expected_sum = (N * (N + 1)) // 2
    
    # Calculate the actual sum of the elements in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected sum and the actual sum
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Example usage:
arr = [1, 2, 4, 6, 3, 7, 8]
N = 8
missing_number = find_missing_number(arr, N)
print("Missing number:", missing_number)
