"""
Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:
Input: s = "zzazz"
Output: 0

Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2

Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5

Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

LINK : https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
"""

# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (n^2)
"""
class Solution:
    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)

        dp = [[-1 for i in range(m+1)] for j in range(n+1)]

        for i in range(m+1):
            dp[i][0] = 0

        for i in range(n+1):
            dp[0][i] = 0

        for indx1 in range(1, n+1):
            for indx2 in range(1, m+1):
                if s1[indx1-1] == s2[indx2-1]:
                    dp[indx1][indx2] = 1 + dp[indx1-1][indx2-1]
                else:
                    dp[indx1][indx2] = max(dp[indx1-1][indx2], dp[indx1][indx2-1])
        
        return dp[n][m]
    
    def longestPalindromeSubsequence(self, s):
        t = s
        s = s[::-1]
        return self.lcs(t, s)

    def minInsertions(self, s: str) -> int:
        n = len(s)
        k =  self.longestPalindromeSubsequence(s)
        return n - k 
