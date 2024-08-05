"""
Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104

LINK : https://leetcode.com/problems/reverse-string-ii/description/
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)

        for start in range(0, n, 2*k):
            end = min(start+k, n)
            s[start:end] = reversed(s[start:end])
        return ''.join(s)