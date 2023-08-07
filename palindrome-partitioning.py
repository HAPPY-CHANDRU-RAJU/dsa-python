"""
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.


Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

"""

##### Optimal #####

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, ans = [],  []
        def isPalindrom(s):
            return s == s[::-1]

        def dfs(ind, s):
            if ind >= len(s):
                res.append(ans.copy())
                return 
            
            for i in range(ind, len(s)):
                if isPalindrom(s[ind: i+1]):
                    ans.append(s[ind : i+1])
                    dfs(i+1, s)
                    ans.pop(-1)
        dfs(0, s)
        return res