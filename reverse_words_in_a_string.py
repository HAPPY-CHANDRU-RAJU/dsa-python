"""
Reverse Words in a String

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"

Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?

LINK : https://leetcode.com/problems/reverse-words-in-a-string/description/
"""

# Brute Force 
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        queue = []
        for word in s.strip().split():
            queue.append(word.strip())
        
        return ' '.join(reversed(queue))

# Medium
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def remove_extra_space(self, s):
        low = 0
        n = len(s)
        for indx in range(n):
            if indx > 0 and s[indx] == ' ' and s[indx-1] == ' ':
                continue
            s[low] = s[indx]
            low += 1
        return s[:low]
    
    def reverse(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        
    def reverseWords(self, s: str) -> str:
        # Step 1: Convert the string into a list of characters (since Python strings are immutable)
        s = list(s.strip()) 

        # Step 2: Remove extra spaces between words
        s = self.remove_extra_space(s)

        # Step 3: Reverse the entire string
        self.reverse(s, 0, len(s)-1)
        
        # Step 4: Reverse each word in the reversed string
        slow = 0
        n = len(s)
        for indx in range(n+1):
            if indx == n or s[indx] == ' ':
                self.reverse(s, slow, indx-1)
                slow = indx+1
        
        # Step 5: Convert list back to string and return  
        return ''.join(s)