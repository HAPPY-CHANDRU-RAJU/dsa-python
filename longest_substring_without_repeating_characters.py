"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.
 
Example 1:
Input: s = "abcabcbb"
Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

LINK : https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

# Brute Force
"""
    Time complexity     : (n^3)
    Space complexity    : (1)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def unique(s, i, j):
            return len(set(s[i:j])) == len(s[i:j])

        n = len(s)

        if n <= 1:
            return n

        max_len = -1
        for i in range(n):
            for j in range(i+1, n+1):
                if unique(s, i, j):
                    max_len = max(max_len, j-i)
                
        return max_len

# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n <= 1:
            return n

        max_len = -1
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j-i+1)
                
        return max_len

# Optimal
"""
    Time complexity     : (S), where S is the sum of all characters in all strings.
    Space complexity    : (n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low, high, cnt = 0, 0, 0
        n = len(s)
        char_list = []

        while low < n:
            if s[low] in char_list:
                char_list.remove(s[high])
                high += 1
            else:
                char_list.append(s[low])
                cnt = max(cnt, low - high + 1)
                low += 1

        return cnt