"""
Implement Trie ll

Ninja has to implement a data structure ”TRIE” from scratch. Ninja has to complete some functions.

1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.
2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.
3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.
4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.
5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.

Note:
1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.
2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution. 

Can you help Ninja implement the "TRIE" data structure?

LINK : https://www.naukri.com/code360/problems/implement-trie
"""

# Solution
"""
    Time complexity     : 
            insert(word): O(n)
            countWordsEqualTo(word): O(n)
            countWordsStartingWith(prefix): O(n)
            erase(word): O(n)
    Space complexity    : 
            Trie Structure: O(k * n) in the worst case for k words of average length n.
            Operation Space: O(1) or O(n) for recursion in the erase method.
"""
from os import *
from sys import *
from collections import *
from math import *

class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.is_completed = False         
        self.prefix_count = 0 
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.childrens:
                node.childrens[char] = TrieNode()
            node.childrens[char].prefix_count += 1 
            node = node.childrens[char]  
        node.word_count += 1   
        node.is_completed = True

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            if char not in node.childrens:
                return 0
            node = node.childrens[char]
        return node.word_count

    def countWordsStartingWith(self, word):
        node = self.root
        for char in word:
            if char not in node.childrens:
                return 0
            node = node.childrens[char]
        return node.prefix_count
    
    def erase(self, word):
        n = len(word)
        curr = self.root
        toBeDeleted = None

        for i in range(n):
            index = word[i]

            parent = curr
            curr = curr.childrens[index]
            curr.prefix_count -= 1

            if toBeDeleted:
                toBeDeleted = None

            if curr.prefix_count == 0:
                if not toBeDeleted:
                    parent.childrens[index] = TrieNode()
                toBeDeleted = curr

            curr.word_count -= 1

            if toBeDeleted:
                toBeDeleted = None

        ############## OR ###############

    def erase(self, word):
        if not self._erase(self.root, word, 0):
            return
        
    def _erase(self, node, word, depth):
        if depth == len(word):
            if node.word_count > 0:
                node.word_count -= 1
                if node.word_count == 0:
                    node.is_completed = False
                node.prefix_count -= 1
                return len(node.childrens) == 0 and not node.is_completed

            return False

        char = word[depth]
        if char not in node.childrens:
            return False
        
        child_node = node.childrens[char]
        should_delete_child = self._erase(child_node, word, depth + 1)

        if should_delete_child:
            del node.childrens[char]
        
        node.prefix_count -= 1

        return len(node.childrens) == 0 and not node.is_completed
