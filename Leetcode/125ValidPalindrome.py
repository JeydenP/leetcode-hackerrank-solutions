# Problem 125: Valid Palindrome
# Difficulty: Easy
# This code checks if a given string is a valid palindrome, ignoring punctuation, spaces, and case.
# Problem Statement: https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        punc = """`!()-[]{};:'"\,<>./?@#$%^&*_~"""
        for char in s:
            if char in punc:
                s = s.replace(char,"")
        s = s.replace(" ","")
        return s.lower() == s[::-1].lower()


# Example usage:
solution = Solution()
test_string = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(test_string))
# Output: True, since the string is a valid palindrome ignoring punctuation and spaces.
test_string = "race a car"
print(solution.isPalindrome(test_string))
# Output: False, since the string is not a valid palindrome.