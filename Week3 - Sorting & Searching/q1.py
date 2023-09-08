# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# ● For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Example 1:
# Input: x = 4 Output: 2
# Explanation: The square root of 4 is 2, so we return 2. Example 2:
# Input: x = 8 Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
# Constraints:
# ● 0<=x<=2^31 -1
# ● Try to solve in most optimized way possible.


def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    result = 0

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle value

        # Check if mid*mid is equal to x, and return mid if it is
        if mid * mid == x:
            return mid

        # If mid*mid is greater than x, move the 'right' pointer to the left
        # Otherwise, move the 'left' pointer to the right
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
            result = mid  # Store the result as the floor value

    return result

# Example usage:
x1 = 4
x2 = 8

result1 = mySqrt(x1)
result2 = mySqrt(x2)

print("Square root of", x1, "rounded down:", result1)
print("Square root of", x2, "rounded down:", result2)
