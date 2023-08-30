"""
Longest Word With All Prefixes | Complete String

https://www.codingninjas.com/studio/problems/complete-string_2687860

"""

#####  Brute Force  #####
class Trienode:
    def __init__(self):
        self.children = {}
        self.end_word = False

class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trienode()
            node = node.children[char]
        node.end_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_word
    
    def searchPrefix(self, word):
        for pos in range(len(word)-1):
            if self.search(word[:pos+1]) == False:
                return False
        return True 

def completeString(n: int, a: List[str])-> str:
    trieObj = Trie()
    for word in a:
        trieObj.insert(word)
    sorted_list = sorted(a, key=lambda x: (-len(x), x[0]))
    for word in sorted_list:
        if trieObj.searchPrefix(word) == True:
            return word
    return "None"


##### Optimal #####
def completeString(n: int, a: List[str])-> str:
    ans = "" 
    mp = {}
    for word in a:
        mp[word] = True

    for word in a:
        pre = ""
        flag = True
        for char in word:
            pre += char
            if pre not in mp:
                flag = False
                break
        if flag:
            if len(ans) < len(word):
                ans = word
            elif len(ans) == len(word) and ans > word:
                ans = word

    if len(ans) == 0:
        ans = "None"
    return ans             