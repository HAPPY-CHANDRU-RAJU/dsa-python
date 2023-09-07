"""
Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 
Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

#####  Brute Force  #####
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels  = ['a','e','i','o','u']
        word = [char for char in s]
        def changeVowels(word, start):
            org, rep = None , None
            ind = start
            for char in word[start:]:
                if org is None and char.lower() in vowels:
                    org = ind

                elif rep is None and char.lower() in vowels:
                    rep = ind
                    break
                ind += 1
            if org is not None and rep is not None:
                word[org], word[rep] = word[rep], word[org]
                changeVowels(word, org+1)
        changeVowels(word, 0)
        return "".join(word)

##### Optimal #####
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels  = ['a','e','i','o','u']
        word = [char for char in s]
        i , j = 0, len(s)-1
        while i < j :
            if word[i].lower() not in vowels:
                i+= 1
                continue

            if word[j].lower() not in vowels:
                j -= 1
                continue

            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1

        return "".join(word)
            
