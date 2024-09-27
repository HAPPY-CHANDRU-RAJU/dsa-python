"""
Repeated String Match

Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3

Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:
Input: a = "a", b = "aa"
Output: 2
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist of lowercase English letters.

LINK : https://leetcode.com/problems/repeated-string-match/description/
"""

# Optimal
"""
    Time complexity     : (n+m)
    Space complexity    : (n)
"""
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = (len(b) + len(a) - 1) // len(a)        
        repeated_a = a * min_repeats
        
        if b in repeated_a:
            return min_repeats
        
        repeated_a += a
        if b in repeated_a:
            return min_repeats + 1
        
        return -1