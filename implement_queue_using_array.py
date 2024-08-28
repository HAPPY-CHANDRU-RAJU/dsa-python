"""
Implement Queue using array

Implement a Queue using an Array. Queries in the Queue are of the following type:
    (i) 1 x   (a query of this type means  pushing 'x' into the queue)
    (ii) 2    (a query of this type means to pop an element from the queue and print the popped element)

Examples:

Input: Q = 5, Queries = 1 2 1 3 2 1 4 2
Output: 2 3

Explanation:
In the first test case for query 
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the queue will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3 


Input: Q = 4, Queries = 1 3 2 2 1 4   
Output: 3 -1

Explanation:
In the second testcase for query 
1 3 the queue will be {3}
2   poped element will be 3 the queue will be empty
2   there is no element in the queue and hence -1
1 4 the queue will be {4}. 


Expected Time Complexity: O(1) for both push() and pop().
Expected Auxiliary Space: O(1) for both push() and pop().

Constraints:
1 ≤ Q ≤ 105
0 ≤ x ≤ 105

LINK : https://www.geeksforgeeks.org/problems/implement-queue-using-array/1
"""

# Optimal
"""
    Time complexity     : (1)
    Space complexity    : (1)
"""
from collections import deque 

class MyQueue:
    def __init__(self):
        self.queue = deque()
        self.length = 0
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.queue.append(x)
        self.length += 1
    
    #Function to pop an element from queue and return that element.
    def pop(self): 
        try:
            if self.length == 0:
                return -1
            self.length -= 1
            return self.queue.popleft()
        except Exception as e:
            return -1