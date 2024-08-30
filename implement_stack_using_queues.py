"""
Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 
Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.
 

Follow-up: Can you implement the stack using only one queue?

LINK : https://leetcode.com/problems/implement-stack-using-queues/
"""

# Optimal
"""
    Time complexity     : 
        - push: O(n), where n is the current number of elements in the stack.
            Each push operation moves all elements from queue1 to queue2, which takes O(n) time.
        - pop: O(1), because it directly removes the element from queue1.
        - top: O(1), because it directly accesses the front element of queue1.
        - empty: O(1), because it just checks the length of the stack.

    Space complexity    : O(n), where n is the number of elements in the stack.
        - Two queues are used, each capable of holding up to n elements, but the extra space used is proportional to the number of elements stored.
"""
class MyStack:
    def __init__(self):
        self.queue = []
        self.length = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            return 
        self.length -= 1
        return self.queue.pop(-1)

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return self.length == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# Optimal
"""
    Time complexity     : 
        - push: O(n), where n is the current number of elements in the stack.
            Each push operation moves all elements from queue1 to queue2, which takes O(n) time.
        - pop: O(1), because it directly removes the element from queue1.
        - top: O(1), because it directly accesses the front element of queue1.
        - empty: O(1), because it just checks the length of the stack.

    Space complexity    : O(n), where n is the number of elements in the stack.
        - Two queues are used, each capable of holding up to n elements, but the extra space used is proportional to the number of elements stored.
"""
from collections import deque

class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.length = 0 

    def push(self, x: int) -> None:
        self.queue2.append(x)

        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.length += 1

    def pop(self) -> int:
        if self.empty():
            return 
        self.length -= 1
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return self.length == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()