"""
Count Distinct Substrings  /  Number Of Distinct Substring

https://www.codingninjas.com/studio/problems/number-of-distinct-substring_1465938?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website

https://www.codingninjas.com/studio/problems/count-distinct-substrings_985292?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0
"""

##### Better  #####

def countDistinctSubstrings(s):
    cnt = 1
    list_ = []
    n = len(s)
    for i in range(n):
        for j in range(i,n):
            chr = s[i:j+1]
            if chr not in list_:
                list_.append(chr)
                cnt += 1
    return cnt

##### Optimal #####
class Trienode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class Trie:
    def __init__(self):
        self.root = Trienode()
        self.nodecnt = 1

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                self.nodecnt += 1
                node.children[char] = Trienode()
            node = node.children[char]
        node.end_word = True

def countDistinctSubstrings(s):
    n = len(s)
    obj = Trie()
    for i in range(n):
        chr = s[i:]
        obj.insert(chr)
        
    return obj.nodecnt