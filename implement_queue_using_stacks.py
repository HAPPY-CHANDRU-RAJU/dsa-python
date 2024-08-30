"""
Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]

Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 

Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 

Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

LINK : https://leetcode.com/problems/implement-queue-using-stacks/description/
"""

# Brute Force
"""
    Time Complexity:
        push(x): O(1) — Appending to the end of the list is an O(1) operation.
        pop(): O(n) — Removing the first element requires shifting all subsequent elements to the left, making it O(n).
        peek(): O(1) — Accessing the first element is O(1).
        empty(): O(1) — Checking if the list is empty is O(1).

    Space Complexity:
        Space Complexity: O(n) — The list stores all the elements pushed onto the queue.
"""
class MyQueue:
    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack

# Optimal
"""
    Time Complexity:
        push(x): O(1) — Each push operation is done in constant time by simply appending to stack1.
        pop(): Amortized O(1) — While transferring elements from stack1 to stack2 takes O(n) time in the worst case, this transfer only happens when stack2 is empty. Across a sequence of operations, each element is moved between the stacks at most once, resulting in an amortized O(1) time for each pop.
        peek(): Amortized O(1) — Similar to pop(), the peek operation also benefits from the amortized O(1) time because it only involves peeking at the top of stack2.
        empty(): O(1) — This operation checks whether both stacks are empty, which is a constant-time operation.
    
    Space Complexity:
        Space Complexity: O(n) — The space used by the queue is proportional to the number of elements it holds, distributed across stack1 and stack2.
"""
class MyQueue:
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()