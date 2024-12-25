"""
Palindrome Partitioning II

Given a string s, partition s such that every  substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.
 
Example 1:
Input: s = "aab"
Output: 1

Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.

LINK : https://leetcode.com/problems/palindrome-partitioning-ii/description/
"""

# Brute Force
"""
    Time complexity     : (n * n^2)
    Space complexity    : (n)
"""
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        def isPalindrome(chars) -> bool:
            return chars == chars[::-1]
        
        def backtrack(start):
            if start == n:
                return 0
            
            min_cuts = float('inf')
            for end in range(start, n):
                chars = s[start:end+1]
                if isPalindrome(chars):
                    cuts = 1 + backtrack(end+1)
                    min_cuts = min(cuts, min_cuts)
            
            return min_cuts
        
        return backtrack(0)-1

# Medium Effort
"""
    Time complexity     : (n^2)
    Space complexity    : (n)   # memo and recursion
"""
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        def isPalindrome(chars) -> bool:
            return chars == chars[::-1]
        
        def backtrack(start):
            if start == n:
                return 0
            
            if start in memo:
                return memo[start]

            min_cuts = float('inf')
            for end in range(start, n):
                chars = s[start:end+1]
                if isPalindrome(chars):
                    cuts = 1 + backtrack(end+1)
                    min_cuts = min(cuts, min_cuts)

            memo[start] = min_cuts
            return memo[start]
        
        memo = {}
        return backtrack(0)-1


# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (n^2)   # palindrome table
"""
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        isPalindrome = [[False]*n for _ in range(n)]

        for i in range(n):
            isPalindrome[i][i] = True
        
        for length in range(2, n+1):
            for start in range(n-length+1):
                end = start+length-1
                if s[start] == s[end] and ( length == 2 or isPalindrome[start+1][end-1]):
                    isPalindrome[start][end] = True
                
        dp = [float('inf')]*n
        for i in range(n):
            if isPalindrome[0][i]:
                dp[i] = 0 
            else:
                for j in range(i):
                    if isPalindrome[j+1][i]:
                        dp[i] = min(dp[i], dp[j]+1)
        
        return dp[-1]