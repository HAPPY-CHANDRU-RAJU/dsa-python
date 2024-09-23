"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"

Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

LINK : https://leetcode.com/problems/longest-palindromic-substring/description/
"""

# Brute Force
"""
    Time complexity     : (n^3)
    Space complexity    : (1)
"""
class Solution:
    def is_palindrome(self, word):
        return word == word[::-1]

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        max_length = 0
        max_palindrome = ""

        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if len(s[i:j+1]) > max_length and self.is_palindrome(s[i:j+1]):
                    max_length = len(s[i:j+1])
                    max_palindrome = s[i:j+1]
        return max_palindrome


# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def expand_around_center(self, left, right, word):
        while left >= 0 and right < len(word) and word[left] == word[right]:
            left -= 1
            right += 1
        return word[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        """
        The "Expand Around Center" approach works:

        Algorithm:
            1. Iterate through the string and treat each character (or pair of adjacent characters) as the center of a potential palindrome.
            2. Expand outward as long as the substring remains a palindrome.
            3. Keep track of the longest palindrome found during the expansion.
        """
        if not s:
            return ""
        
        longest_palindrome = ""

        for i in range(len(s)):
            palindrom_odd = self.expand_around_center(i, i, s)
            palindrom_even = self.expand_around_center(i, i+1, s)

            if len(longest_palindrome) < len(palindrom_odd):
                longest_palindrome = palindrom_odd
            
            if len(longest_palindrome) < len(palindrom_even):
                longest_palindrome = palindrom_even

        return longest_palindrome