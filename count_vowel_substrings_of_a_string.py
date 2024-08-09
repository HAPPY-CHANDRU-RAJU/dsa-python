"""
Count Vowel Substrings of a String

A substring is a contiguous (non-empty) sequence of characters within a string.
A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
Given a string word, return the number of vowel substrings in word.

Example 1:
Input: word = "aeiouu"
Output: 2

Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Example 2:
Input: word = "unicornarihan"
Output: 0

Explanation: Not all 5 vowels are present, so there are no vowel substrings.

Example 3:
Input: word = "cuaieuouac"
Output: 7

Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
 

Constraints:

1 <= word.length <= 100
word consists of lowercase English letters only.

LINK : https://leetcode.com/problems/count-vowel-substrings-of-a-string/
"""

# Brute Force
"""
    Time complexity     :  (n^3)
    Space complexity    :  (1)
"""
class Solution:
    def check_vowels(self, substring):
        vowels_set = set(substring)
        return vowels_set.issubset(set("aeiou")) and len(vowels_set) == 5
            
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        count_vowels = 0
        for i in range(n):
            for j in range(i+5, n+1):
                if self.check_vowels(word[i:j]):
                    count_vowels += 1
        return count_vowels

# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        count_vowels = 0

        vowels = set("aeiou")
        for i in range(n):
            if word[i] in vowels:
                seen = set()
                for j in range(i, n):
                    if word[j] in vowels:
                        seen.add(word[j])
                        if len(seen) == 5:
                            count_vowels += 1
                    else:
                        break
        return count_vowels