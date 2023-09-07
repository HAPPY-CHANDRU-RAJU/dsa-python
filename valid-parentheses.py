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
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

##### Better  #####
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False
        stack = []
        for i in s:
            try:
                if i == "{" or i == "[" or i == "(":
                    stack.append(i)
                elif i == '}' and stack.pop(-1) == "{":
                    continue
                elif i == ']' and stack.pop(-1) == "[":
                    continue
                elif i == ')' and stack.pop(-1) == "(":
                    continue
                else:
                    return False
            except:
                return False
        if len(stack) == 0:
            return True
        return False
        

##### Optimal #####
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
        if obj.empty():
            return True
        return False
