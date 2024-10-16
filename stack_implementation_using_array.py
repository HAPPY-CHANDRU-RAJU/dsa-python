"""
Stack Implementation Using Array

Stack is a data structure that follows the LIFO (Last in First out) principle. Design and implement a stack to implement the following functions:
1. Push(num): Push the given number in the stack if the stack is not full.
2. Pop: Remove and print the top element from the stack if present, else print -1.
3. Top: Print the top element of the stack if present, else print -1.
4. isEmpty: Print 1 if the stack is empty, else print 0.
5. isFull: Print 1 if the stack is full, else print 0.

You have been given ‘m’ operations which you need to perform in the stack. Your task is to implement all the functions of the stack.

Example:
We perform the following operations on an empty stack which has capacity 2:
When operation 1 1 is performed, we insert 1 in the stack.
When operation 1 2  is performed, we insert 2 in the stack. 
When operation 2 is performed, we remove the top element from the stack and print 2.
When operation 3 is performed, we print the top element of the stack, i.e., 3.
When operation 4 is performed, we print 0 because the stack is not empty.
When operation 5 is performed, we print 0 because the stack is size 1, which is not equal to its capacity.

Sample Input 1 :
2 6
1 1
1 2
2
3
4
5

Sample Output 1 :
2 
1
0
0

Explanation For Sample Output 1 :
We perform the following operations on an empty stack which has capacity 2:
When operation 1 1 is performed, we insert 1 in the stack.
When operation 1 2  is performed, we insert 2 in the stack. 
When operation 2 is performed, we remove the top element from the stack and print 2.
When operation 3 is performed, we print the top element of the stack, i.e., 1.
When operation 4 is performed, we print 0 because the stack is not empty.
When operation 5 is performed, we print 0 because the stack is size 1, which is not equal to its capacity.

Sample Input 2 :
5 5
1 2
2
2 
1 1
3

Sample Output 2 :
2 
-1
1

Explanation For Sample Output 2 :
We perform the following operations on an empty stack which has a capacity of 5:

When operation 1 2 is performed, we insert 2 in the stack.
When operation 2 is performed, we remove the top element from the stack and print 2.
When operation 2 is performed, as the stack is empty, we print -1.
When operation 1 1 is performed, we insert 1 in the stack.
When operation 3 is performed, we print the top element of the stack, i.e., 1.

Constraints :
1 <= 'n', 'm' <= 10^3

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/stack-implementation-using-array
"""

# Solution
"""
    Time complexity     :  (1) # Each operation (push, pop, top, isEmpty, isFull) executes in constant time.
    Space complexity    :  (n)
"""
from sys import *
from collections import *
from math import *
from typing import List

class Stack:
    def __init__(self, n: int):
        self.length = n
        self.curr = -1
        self.stack = []

    def push(self, num: int):
        if self.isFull():
            return
        
        self.curr += 1
        self.stack.append(num)

    def pop(self) -> int:
        if not self.isEmpty():
            self.curr -= 1
            return self.stack.pop()
        return -1

    def top(self) -> int:
        if not self.isEmpty():
            return self.stack[-1]
        return -1

    def isEmpty(self) -> int:
        return 1 if(self.curr < 0) else 0

    def isFull(self) -> int:
        return 1 if(self.curr > self.length-1) else 0

