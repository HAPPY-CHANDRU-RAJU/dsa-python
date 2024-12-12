"""
Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.


Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  

Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3

Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0

Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

LINK : https://leetcode.com/problems/longest-common-subsequence/description/
"""

# Brute Force
"""
    Time complexity     : (2^min(m,n))
    Space complexity    : (min(m,n))
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            
            if s1[m-1] == s2[n-1]:
                return 1+lcs(s1, s2, m-1, n-1)
            else:
                return max(
                    lcs(s1, s2, m-1, n),
                    lcs(s1, s2, m, n-1)
                )
        
        return lcs(text1, text2, len(text1), len(text2))


# Medium Effort
"""
    Time complexity     : (m*n)
    Space complexity    : (m*n)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[-1 for _ in range(n+1)] for i in range(m+1)]

        def lcs(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            
            if memo[m][n] != -1:
                return memo[m][n]
            
            if s1[m-1] == s2[n-1]:
                memo[m][n] = 1+lcs(s1, s2, m-1, n-1)
                return memo[m][n]
            
            memo[m][n] = max( lcs(s1, s2, m-1, n), lcs(s1, s2, m, n-1 ) )
            return memo[m][n]
        
        return lcs(text1, text2, m, n)


# Optimal
"""
    Time complexity     : (m*n)
    Space complexity    : (m*n)
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo = [[0] * (n+1) for i in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] =  max(memo[i][j-1], memo[i-1][j])
        
        return memo[m][n]