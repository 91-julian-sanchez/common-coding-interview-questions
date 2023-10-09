# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # Conjunto para almacenar caracteres únicos en la ventana
        max_length = 0    # Longitud máxima de la subcadena sin caracteres repetidos
        left = 0          # Índice izquierdo de la ventana

        for right in range(len(s)):
 
            # Mientras el carácter en la posición derecha ya esté en el conjunto,
            # eliminamos el carácter en la posición izquierda de la ventana
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Agregamos el carácter en la posición derecha a la ventana
            char_set.add(s[right])
            # Actualizamos la longitud máxima de la subcadena
            max_length = max(max_length, right - left + 1)

            print(max_length,":",char_set)

        return max_length

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        sol = Solution()
        result = sol.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(result, 3)

    def test_case_2(self):
        sol = Solution()
        result = sol.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(result, 1)

    def test_case_3(self):
        sol = Solution()
        result = sol.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(result, 3)

    def test_case_4(self):
        sol = Solution()
        result = sol.lengthOfLongestSubstring("abcdefg")
        self.assertEqual(result, 7)

    def test_case_5(self):
        sol = Solution()
        result = sol.lengthOfLongestSubstring("aab")
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()