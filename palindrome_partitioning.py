"""
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome . 
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

LINK : https://leetcode.com/problems/palindrome-partitioning/description/
"""

# Brute Force
"""
    Time complexity     : (n * 2^n)
    Space complexity    : (n)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, ans = [], []

        def isPalindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def dfs(ind: int, s: str) -> None:
            if ind >= len(s):
                res.append(ans.copy())
                return

            for i in range(ind, len(s)):
                if isPalindrome(s[ind:i + 1]):
                    ans.append(s[ind:i + 1])
                    dfs(i + 1, s)
                    ans.pop()

        dfs(0, s)
        return res


# Optimal
"""
    Time complexity     : (n * 2^n)
    Space complexity    : (n * 2^n)
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, memo = [], {}

        def isPalindrome(sub) -> bool:
            return sub == sub[::-1]

        def dfs(start) -> List:
            if start in memo:                   # Memorisation if start already in memo return the list
                return memo[start]

            if start == len(s):
                return [[]]

            participate = []
            for end in range(start+1, len(s)+1):
                if isPalindrome(s[start:end]):
                    for suffix in dfs(end):
                        participate.append([s[start:end]] + suffix)
            memo[start] = participate
            return participate     
        res = dfs(0)
        return res