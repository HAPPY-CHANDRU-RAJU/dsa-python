"""
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    MinStack() initializes the stack object.
        - void push(int val) pushes the element val onto the stack.
        - void pop() removes the element on the top of the stack.
        - int top() gets the top element of the stack.
        - int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

 
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

LINK : https://leetcode.com/problems/min-stack/description/
"""

# Optimal
"""
    Time complexity     : (1)
    Space complexity    : (n)
"""
class MinStack:
    """
    Approach:
        Two Stacks Approach:

        Use two stacks:
            - Main Stack (stack): This stack stores all the elements.
            - Min Stack (minStack): This stack keeps track of the minimum values at each level of the main stack.
        
        Operations:
            - Push (push(val)):
                Push the value val onto the stack.
                Push val onto the minStack if minStack is empty or if val is less than or equal to the current minimum (top of minStack).
            
            - Pop (pop()):
                Pop the top element from the stack.
                Also, pop the top element from the minStack if the popped value from the stack is equal to the top of minStack. This ensures the minimum value is always accurate.
                
            - Top (top()):
                Return the top element of the stack, which is the last pushed element.
            
            - Get Minimum (getMin()):
                Return the top element of the minStack, which is the current minimum value of the stack.
    """
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or self.minstack[-1] >= val:
            self.minstack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.minstack[-1]:
                self.minstack.pop()    


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self) -> int:
        if self.minstack:
            return self.minstack[-1]
        return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()