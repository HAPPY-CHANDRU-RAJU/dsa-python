"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

LINK : https://leetcode.com/problems/valid-parentheses/
"""

# Optimal
"""
    Time complexity     : 
        push(data): O(1) - Adding an element to the end of the list takes constant time.
        pop(): O(1) - Removing the last element from the list takes constant time.
        empty(): O(1) - Checking if the list is empty takes constant time.

    Space complexity    : O(n)
"""
class Stack:
    def __init__(self):
        self.arr = []
    
    def push(self, data):
        self.arr.append(data)
    
    def pop(self):
        if not self.arr:
            return -1
        return self.arr.pop()

    def empty(self):
        return self.arr == []

class Solution:
    def isValid(self, s: str) -> bool:
        obj = Stack()
        for char in s:
            if char in ["{", "[", "("]:
                obj.push(char)
            elif char in ["}", ")", "]"]:
                top = obj.pop()
                if top == "{" and char == "}":
                    continue
                elif top == "[" and char == "]":
                    continue
                elif top == "(" and char == ")":
                    continue
                else:
                    return False
        return obj.empty()