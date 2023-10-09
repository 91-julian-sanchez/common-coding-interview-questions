# Longest Palindromic Substring
# Given a string s, return the longest palindromic
 
# substring
#  in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 
import unittest

class Solution:
    def expand_around_center(self, s,left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # print(s[left + 1:right])
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        for i in range(len(s)):
            # Caso 1: Palíndroma con centro en el propio carácter
            palindrome1 = self.expand_around_center(s,i, i)
            if len(palindrome1) > len(longest):
                longest = palindrome1
            
            # Caso 2: Palíndroma con centro entre dos caracteres
            palindrome2 = self.expand_around_center(s,i, i + 1)
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        result = sol.longestPalindrome("babad")
        self.assertEqual(result, "bab")
    def test_case_2(self):
        sol = Solution()
        result = sol.longestPalindrome("cbbd")
        self.assertEqual(result, "bb")

if __name__ == '__main__':
    unittest.main()