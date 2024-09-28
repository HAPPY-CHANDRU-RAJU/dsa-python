"""
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0

Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

LINK : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
"""


# Brute force
"""
    Time complexity     : (n+m) or (n*m)
    Space complexity    : (1) 
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) # Using algorithm like Knuth-Morris-Pratt (KMP) 


# Optimal - Rabin-Karp algorithm
"""
    Time complexity     : (n+m) or (n*m)
    Space complexity    : (1) 
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: If needle is empty
        if not needle:
            return 0
        
        # Lengths of haystack and needle
        n, m = len(haystack), len(needle)
        
        # If needle is longer than haystack, return -1
        if m > n:
            return -1
        
        d = 256  # Base number for the rolling hash (number of characters)
        q = 101   # A large prime number for modulo operations
        
        # Hash values for needle (pattern) and haystack's current window (text)
        p_hash = 0
        t_hash = 0

        # Precompute h = d^(m-1) % q
        h = 1
        for i in range(m - 1):
            h = (h * d) % q
        
        # Calculate the hash value for the pattern and the first window of the text
        for i in range(m):
            p_hash = (d * p_hash + ord(needle[i])) % q
            t_hash = (d * t_hash + ord(haystack[i])) % q
        
        # Slide the window over the text
        for i in range(n - m + 1):
            # Check if the hash values match then check character-by-character
            if p_hash == t_hash:
                if haystack[i:i + m] == needle:
                    return i
            
            # Calculate the hash value for the next window (rolling hash)
            if i < n - m:
                t_hash = (d * (t_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
                
                # We might get negative hash, convert it to positive
                if t_hash < 0:
                    t_hash += q
        
        # If no match found, return -1
        return -1
