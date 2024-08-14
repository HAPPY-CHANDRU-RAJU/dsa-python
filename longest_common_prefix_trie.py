"""

You are given an array ‘ARR’ consisting of ‘N’ strings. Your task is to find the longest common prefix among all these strings. If there is no common prefix, you have to return an empty string.

A prefix of a string can be defined as a substring obtained after removing some or all characters from the end of the string.

For Example:
Consider ARR = [“coding”, ”codezen”, ”codingninja”, ”coders”]
The longest common prefix among all the given strings is “cod” as it is present as a prefix in all strings. Hence, the answer is “cod”.

Sample Input 1:
2
4
coding codezen codingninja coder
3
night ninja nil 

Sample Output 1:
cod
ni

Explanation of sample input 1:
    For the first test case,  The longest common prefix among all the given strings is “cod” as it is present as a prefix in all strings. Hence, the answer is “cod”.
    For the second test case, The longest common prefix among all the given strings is “ni” as it is present as a prefix in all strings. Hence, the answer is “ni”.

Sample Input 2:
2
3
applejuice applepie apple
4
car cus cart carat

Sample Output 2:
apple
c

Constraints:
1 <= T <= 10
1 <= N <= 3000
1 <= |ARR[i]| <=1000

Each string consists of only lowercase letters.

Time limit: 1 sec

LINK : https://www.naukri.com/code360/problems/longest-common-prefix_
"""

# Medium
"""
    Time complexity     : (n*m)
    Space complexity    : (m)
"""
def longestCommonPrefix(arr, n):
    prefix = arr[0]
    for word in arr[1:]:
        while word[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix 

# Optimal 
"""
    Time complexity     : (2n)
    Space complexity    : (n)
"""
class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.is_completed = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.childrens:
                node.childrens[char] = TrieNode()
            node = node.childrens[char]
        node.is_completed = True
    
    def findCommonPrefix(self):
        node = self.root
        prefix = []
        while node and len(node.childrens) == 1 and not node.is_completed:
            print()
            char, next_node = next(iter(node.childrens.items()))
            prefix.append(char)
            node = next_node
        return "".join(prefix)

def longestCommonPrefix(arr, n):
    trie_obj = Trie()

    for word in arr:
        trie_obj.insert(word)
    
    return trie_obj.findCommonPrefix()
