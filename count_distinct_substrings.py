"""
Count Distinct Substrings

Given a string 'S', you are supposed to return the number of distinct substrings(including empty substring) of the given string. You should implement the program using a trie.

Note :
A string ‘B’ is a substring of a string ‘A’ if ‘B’ that can be obtained by deletion of, several characters(possibly none) from the start of ‘A’ and several characters(possibly none) from the end of ‘A’. 
Two strings ‘X’ and ‘Y’ are considered different if there is at least one index ‘i’  such that the character of ‘X’ at index ‘i’ is different from the character of ‘Y’ at index ‘i’(X[i]!=Y[i]).

Sample Input 1 :
2
sds
abc

Sample Output 1 :
6
7

Explanation of Sample Input 1 :
In the first test case, the 6 distinct substrings are { ‘s’,’ d’, ”sd”, ”ds”, ”sds”, “” }
In the second test case, the 7 distinct substrings are {‘a’, ‘b’, ‘c’, “ab”, “bc”, “abc”, “” }.

Sample Input 2 :
2
aa
abab

Sample Output 2 :
3
8

Explanation of Sample Input 2 :
In the first test case, the two distinct substrings are {‘a’, “aa”, “” }.
In the second test case, the seven distinct substrings are {‘a’, ‘b’, “ab”, “ba”, “aba”, “bab”, “abab”, “” }


Hints:
1. Can you think about a data structure that can be used to store the distinct substrings?
2. Can you think about using the fact that every substring of ‘S’ is a prefix of some suffix string of ‘S’?
3. Try to insert every suffix of the string in Trie.

Constraints :
1 <= T <= 5
1 <= |S| <= 10^3

‘S’ contains only lowercase English letters.

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/count-distinct-substrings
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (n^2)
"""
def countDistinctSubstrings(s):
    substrings = set()
    n = len(s)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(s[i:j])
    
    return len(substrings)

# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (n^2)
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node_cnt = 1
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
                self.node_cnt += 1
            node = node.children[char]
        node.is_end = True

def countDistinctSubstrings(s):
    obj = Trie()
    n = len(s)
    for i in range(n):
        obj.insert(s[i:])
    return obj.node_cnt 
