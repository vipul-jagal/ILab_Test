# Ques 1--- Palindrome String Checker 10 Point A palindrome string has some properties which are mentioned below:
# ● A palindrome string has a symmetric structure which means that the character in the first half of the string are the same as in the rear half but in reverse order. Any string of length 1 is always a palindrome.
# Write a function to check the Palindrome Print Yes or No, write the space and time complexity.
# Input : abbcbba output: Yes Input: apple output: No




def is_palindrome(s):
    # Remove spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Example usage:
input_str1 = "abbcbba"
input_str2 = "apple"

if is_palindrome(input_str1):
    print("Yes")
else:
    print("No")

if is_palindrome(input_str2):
    print("Yes")
else:
    print("No")
