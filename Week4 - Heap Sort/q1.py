# You are given an array. Now you have to convert it into a min heap and max heap. write the logic behind the given functions.
# 1. CreateMinHeap( array ) -> returns MinHeap
# 2. CreateMaxHeap( array ) -> returns MaxHeap
# 3. AddElementInMinHeap( MinHeap ) -> returns modified MinHeap
# 4. PopSamllestElementFromMinHeap( MinHeap ) -> returns element, MinHeap
# 5. PopLargestElementFromMaxHeap( MaxHeap ) -> returns element, MaxHeap


import heapq

# Function to create a Min Heap from an array
def createMinHeap(array):
    heapq.heapify(array)
    return array

# Function to create a Max Heap from an array
def createMaxHeap(array):
    maxHeap = [-x for x in array]
    heapq.heapify(maxHeap)
    return maxHeap

# Function to add an element to a Min Heap
def addElementInMinHeap(minHeap, element):
    heapq.heappush(minHeap, element)
    return minHeap

# Function to pop the smallest element from a Min Heap
def popSmallestElementFromMinHeap(minHeap):
    smallest = heapq.heappop(minHeap)
    return smallest, minHeap

# Function to pop the largest element from a Max Heap
def popLargestElementFromMaxHeap(maxHeap):
    largest = -heapq.heappop(maxHeap)
    return largest, maxHeap

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

minHeap = createMinHeap(arr.copy())
maxHeap = createMaxHeap(arr.copy())

print("Min Heap:", minHeap)
print("Max Heap:", maxHeap)

minHeap = addElementInMinHeap(minHeap, 0)
print("Min Heap after adding 0:", minHeap)

smallest, minHeap = popSmallestElementFromMinHeap(minHeap)
print("Smallest Element from Min Heap:", smallest)
print("Min Heap after popping smallest element:", minHeap)

largest, maxHeap = popLargestElementFromMaxHeap(maxHeap)
print("Largest Element from Max Heap:", largest)
print("Max Heap after popping largest element:", maxHeap)
