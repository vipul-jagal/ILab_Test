# An Introduction to the Longest Increasing Subsequence Problem

# The task is to find the length of the longest subsequence in a given array of integers such that all elements of the subsequence are sorted in strictly ascending order. This is called the Longest Increasing Subsequence (LIS) problem.
# For example, the length of the LIS for is since the longest increasing subsequence is [15,27,14,38,26,55,46,65,85] .
 
# Given a sequence of integers, find the length of its longest strictly increasing subsequence.
# Function Description
# Complete the longestIncreasingSubsequence function in the editor below. It should return an integer that denotes the array's LIS.
# longestIncreasingSubsequence has the following parameter(s): arr: an unordered array of integers

# Input Format
# The first line contains a single integer , the number of elements in . Each of the next lines contains an integer, arr[i]
# Constraints
# 1 <= n <= 10^6
# 1 <= arr[i] <= 10^5

# Output Format
# Print a single line containing a single integer denoting the length of the longest increasing subsequence.
# Sample Input 0
# 5 
# 2 
# 7
# 4
# 3
# 8
# Sample Output 0
# 3
# Explanation 0
# In the array arr = [2,7,4,3,8] the longest increasing subsequence is [2,7,8]. It has a length of 3.
# Sample Input 1
#  6
#  2 
# 4 
# 3 
# 7 
# 4 
# 5
# Sample Output 1
# 4
# Explanation 1
# The LIS of arr = [2,4,3,7,4,5] is [2,3,4,5]


def longestIncreasingSubsequence(arr):
    n = len(arr)
    lis = [1] * n  # Initialize an array to store the length of LIS for each element

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)  # Return the maximum length of LIS

# Read input
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# Find and print the length of the longest increasing subsequence
result = longestIncreasingSubsequence(arr)
print(result)
