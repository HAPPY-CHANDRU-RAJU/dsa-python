"""
Longest Substring Without Repeating Characters

"""

# Brute Force

# Optimal
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r, l, cnt = 0,0,0
        hs = set()
        while r <= len(s)-1:
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            cnt = max(cnt, r-l+1)
            r += 1
        return cnt
