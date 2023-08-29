"""
Implement Trie ll

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string wordinto the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix)Returns the number of strings in the trie that have the string prefix as a prefix.
void erase(String word) Erases the string wordfrom the trie


Example 1:
Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]

Output
[null, null, null, 2, 2, null, 1, 1, null, 0]

Explanation
Trie trie = new Trie();
trie.insert("apple");               // Inserts "apple".
trie.insert("apple");               // Inserts another "apple".
trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple");                // Erases one "apple".
trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple");                // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0

"""

##### Optimal #####
from os import *
from sys import *
from collections import *
from math import *

class Trienode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word_count = 0        
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trienode()
            node = node.children[char]
            node.prefix_count += 1
        node.word_count += 1
        node.is_end_of_word = True

    def countWordsEqualTo(self, word):
        node = self.root
        for char in word:
            if node is None or char not in node.children:
                return 0
            node = node.children[char]
        return node.word_count

    def countWordsStartingWith(self, word):
        node = self.root
        for char in word:
            if node is None or char not in node.children:
                return 0
            node = node.children[char]
        return node.prefix_count

    def erase(self, word):
        node = self.root
        toBeDeleted = None
        for char in word:
            parent = node
            node = node.children[char]
            node.prefix_count -= 1
            if toBeDeleted:
                toBeDeleted = None
            
            if node.prefix_count == 0:
                if not toBeDeleted:
                    parent.children[char] = None
                toBeDeleted = node
            
            node.word_count -= 1

            if toBeDeleted:
                toBeDeleted = None



