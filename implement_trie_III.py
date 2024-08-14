"""
Implement Trie lll - Delete Operation

You are given a Trie data structure which stores words or strings and a string 'WORD'. Your task is to perform the delete operation on the Trie to delete an input string 'WORD' from it.
You have to complete the function deleteWord() which takes the root of input Trie 'ROOT' and a string 'WORD' as parameters and returns a TrieNode pointer. If the string 'WORD' exists in the trie, it must be deleted, and the root of new Trie should be returned. If the correct word is deleted, the output will be “TRUE” else it will be “FALSE”.
If the string “word” doesn’t exist in the Trie, then no delete operation will take place, and the output will be “TRUE”. If for any query, the output is “FALSE”, then the answer is wrong.
Trie is a data structure which is like a tree data structure in its organization. It consists of nodes that store letters or alphabets of words, which can be added, retrieved, and deleted from the trie in a very efficient way. In other words, Trie is an information retrieval data structure, which can beat naive data structures like Hashmaps, Trees etc. in time complexities of its operations.

Above figure is the representation of a Trie. New words that are added are inserted as the children of the root node. Alphabets are added in the top to bottom fashion in parent to children hierarchy. Alphabets that are highlighted with blue circles are the end nodes which mark the ending of a word in the Trie.
To define this problem, we perform operations with the following two types of queries.
To insert a string WORD in the Trie, we use ‘’Type 1’’ query.

Example: 1 WORD 
We will put the integer 1 before the input string WORD to insert it into the Trie.
To delete the string  WORD from the Trie, we use the “Type 2” query.

Example: 2 WORD
We will put integer 2 before the input string WORD to delete the string WORD from the Trie.
Example:-
    Query A - 1 coding
    This query will add the string “coding” in the trie.

    Query B - 2 coding
    This query will delete the string “coding” from the Trie. After deleting the string, it will produce “TRUE” as it’s output.

Note:
If anywhere in the output, the word “FALSE” is printed, it means that the given string is not deleted successfully from the Trie, and hence it will lead to a Wrong Answer.

LINK : https://www.naukri.com/code360/problems/trie-delete-operation
"""

# Solution
"""
    Time complexity     :  (n)
    Space complexity    :  (k * n) in the worst case for k words of average length n.
"""
from os import *
from sys import *
from collections import *
from math import *

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26

def isEmpty(root):
    for i in range(26):
        if root.children[i]:
            return False
    return True

def deleteWordHelper(root, word, depth=0):
    if root is None:
        return None

    if depth == len(word):
        if root.isEnd:
            root.isEnd = False
        
        if isEmpty(root):
            return None
        return root

    index = ord(word[depth]) - ord('a')
    root.children[index] = deleteWordHelper(root.children[index], word, depth + 1)

    if isEmpty(root) and not root.isEnd:
        return None

    return root

def deleteWord(root, word):
    return deleteWordHelper(root, word)