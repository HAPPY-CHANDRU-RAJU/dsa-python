"""
Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true

Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true

Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.

All the strings of wordDict are unique.

LINK : https://leetcode.com/problems/word-break/
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def solver(self, start, n, s, wordDict, memo):
        if start == n:
            return True
        
        if start in memo:
            return memo[start]

        for end in range(start+1, n+1):
            if s[start:end] in wordDict and self.solver(end, n, s, wordDict, memo):
                memo[start] = True
                return True

        memo[start] = False
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        return self.solver(0, n, s, set(wordDict), {})

# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)

        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        
        return dp[-1]