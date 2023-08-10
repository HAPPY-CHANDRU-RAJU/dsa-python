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
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

##### Brute Force ######
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recurse(c: int) -> bool:
            if c >= len(s):
                return True

            res = False
            for word in wordDict:
                if word == s[c: c+ len(word)]:
                    res = res or recurse(c+len(word))
            return res
        return recurse(0)

##### Better  #####
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True]
        for i in range(1, n+1):
            dp.append( any( dp[j] and s[j:i] in wordDict for j in range(i)))
        
        return dp[-1]

##### Optimal #####
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        max_len = max(map(len, wordDict))
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            for j in range(i - 1, max(i - 1 - max_len, -1), -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
