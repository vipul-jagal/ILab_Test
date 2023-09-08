# To construct a max-heap using the bottom-up approach, we'll start with the given set and perform heapify operations to transform it into a max-heap. Here's the step-by-step process:

# Initial set: [50, 30, 70, 20, 60, 45, 55]

# Step 1: Start with the last non-leaf node and heapify it (from right to left).

Initial State: [50, 30, 70, 20, 60, 45, 55]

Heapify at index 2 (70):
Result: [50, 30, 70, 20, 60, 45, 55]


#Step 2: Move to the previous non-leaf node and heapify it.

Heapify at index 1 (30):
Result: [50, 60, 70, 20, 30, 45, 55]

#Step 3: Continue this process for all non-leaf nodes until you reach the root.

Heapify at index 0 (50):
Result: [70, 60, 50, 20, 30, 45, 55]

#The final result is a max-heap representation of the given set:

[70, 60, 50, 20, 30, 45, 55]

# So, the max-heap representation of the initial set [50, 30, 70, 20, 60, 45, 55] is [70, 60, 50, 20, 30, 45, 55].