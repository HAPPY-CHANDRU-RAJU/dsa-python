"""
Sort a Stack

You’re given a stack consisting of 'N' integers. Your task is to sort this stack in descending order using recursion.

We can only use the following functions on this stack S.
    is_empty(S) : Tests whether stack is empty or not.
    push(S) : Adds a new element to the stack.
    pop(S) : Removes top element from the stack.
    top(S) : Returns value of the top element. Note that this function does not remove elements from the stack.

Note :
1) Use of any loop constructs like while, for..etc is not allowed. 
2) The stack may contain duplicate integers.
3) The stack may contain any integer i.e it may either be negative, positive or zero.

Constraints:
1 <= 'T' <= 100
1 <=  'N' <= 100
1 <= |'V'| <= 10^9

LINK : https://www.naukri.com/code360/problems/sort-a-stack_985275
"""

# Optimal
"""
    Time complexity     : O(n^2)
    Space complexity    : O(n)
"""

def sortInsert(stack, ele):
    if not stack or ele > stack[-1]:
        stack.append(ele)
        return
    else:
        temp = stack.pop()
        sortInsert(stack, ele)
        stack.append(temp)

def sortStack(stack):
    if stack:
        s = stack.pop()
        sortStack(stack)
        sortInsert(stack, s)


