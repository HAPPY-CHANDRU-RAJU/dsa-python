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

#################### OR ####################

"""
    Time complexity     : (n*m)
    Space complexity    : (1) 
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1
        
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1

        for i in range(n):
            indx = i
            j = 0
            while j < m and indx < n:
                if needle[j] == haystack[indx]:
                    j += 1
                    indx += 1
                else:
                    break
            
            if j == m:
                return i
        return -1


# Optimal - Rabin-Karp algorithm
"""
    Time complexity     : (n*m)
    Space complexity    : (1)  or (m)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: If needle is empty, return 0 (as per the problem definition)
        if not needle:
            return 0
        
        # Lengths of haystack and needle
        n, m = len(haystack), len(needle)
        
        # If the needle is longer than the haystack, no match is possible, return -1
        if m > n:
            return -1
        
        # d is the number of characters in the input alphabet (ASCII base for rolling hash)
        d = 256  
        # q is a large prime number used for modulus in the rolling hash to reduce collisions
        q = 101   
        
        # Hash values for the needle (pattern) and the first window of the haystack (text)
        p_hash = 0  # Hash value for the needle (pattern)
        t_hash = 0  # Hash value for the current window in the haystack (text)

        # h = d^(m-1) % q, used to remove the leading digit in the rolling hash
        h = 1
        for i in range(m - 1):
            h = (h * d) % q
        
        # Calculate the initial hash value for the needle and the first window of the haystack
        for i in range(m):
            p_hash = (d * p_hash + ord(needle[i])) % q
            t_hash = (d * t_hash + ord(haystack[i])) % q
        
        # Slide the window over the haystack one character at a time
        for i in range(n - m + 1):
            # If the hash values of the current window and the needle match
            if p_hash == t_hash:
                # Check character by character to ensure it's a real match (not a hash collision)
                if haystack[i:i + m] == needle:
                    return i  # Return the index where the match is found
            
            # Compute the hash value for the next window (rolling hash)
            if i < n - m:
                t_hash = (d * (t_hash - ord(haystack[i]) * h) + ord(haystack[i + m])) % q
                
                # We might get a negative hash value, convert it to positive
                if t_hash < 0:
                    t_hash += q
        
        # If no match is found, return -1
        return -1


# Optimal - Z Algorithm algorithm
"""
    Time complexity     : (n+m)
    Space complexity    : (n+m) 
"""
class Solution:
    def getZarr(self, string, z):
        """
        This function generates the Z-array for the input string.
        The Z-array for a string str is an array of length n where Z[i] is the length 
        of the longest substring starting from str[i] which is also a prefix of str.

        string: The concatenated string (needle + '$' + haystack)
        z: Z-array to store the lengths of the longest prefix match
        """
        n = len(string)  # Length of the input string
        r, l = 0, 0      # Right and left boundary of the Z-box
        
        for i in range(1, n):
            if i > r:  # If i is outside the current Z-box
                l, r = i, i  # Set new left and right boundary
                # Expand the box as long as characters match the prefix
                while r < n and string[r - l] == string[r]:
                    r += 1
                z[i] = r - l  # Store the length of the matching prefix
                r -= 1  # Adjust right boundary
            else:
                k = i - l  # Index within the Z-box
                # If the value at z[k] is within the bounds of the Z-box, reuse it
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    # Otherwise, start checking for a new match from outside the Z-box
                    l = i
                    while r < n and string[r - l] == string[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Function to find the first occurrence of needle in haystack using the Z-algorithm.
        If the needle is not found, return -1. If the needle is empty, return 0.

        haystack: The text in which we want to search for the needle
        needle: The substring to find
        return: The starting index of the first occurrence of needle in haystack, or -1 if not found
        """
        if not needle:
            return 0  # If needle is empty, return 0 as per the problem's requirement

        if len(needle) > len(haystack):
            return -1  # If needle is longer than haystack, it can't be found

        # Concatenate needle + '$' + haystack to create the combined string
        new_string = needle + '$' + haystack
        l = len(new_string)  # Length of the combined string
        z = [0] * l  # Initialize the Z-array with 0s

        # Get the Z-array for the combined string
        self.getZarr(new_string, z)
        pat_len = len(needle)  # Length of the needle (pattern)

        # Iterate over the Z-array starting from the index after the needle + '$'
        for i in range(pat_len + 1, l):
            if z[i] == pat_len:
                # If the value in Z-array equals the length of the needle, 
                # it means we found the needle in the haystack
                return i - pat_len - 1  # Return the index where the needle starts in haystack

        return -1  # If needle is not found, return -1
