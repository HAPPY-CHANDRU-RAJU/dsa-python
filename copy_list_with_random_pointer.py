"""
Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.
Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
    val: an integer representing Node.val
    random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.

LINK : https://leetcode.com/problems/copy-list-with-random-pointer/
"""

# Brute Force
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        old_to_new = {}                                          # empty dictionary
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            old  = old_to_new[current]
            if current.next:                                     # check the next is not None
                old.next = old_to_new[current.next]
            if current.random:                                   # check the random is not None
                old.random = old_to_new[current.random]
            current = current.next
        
        return old_to_new[head]

# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        old_to_new = {None:  None}                # Added None so even next or random pointed its None only not keyword error
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        
        current = head
        while current:
            old  = old_to_new[current]
            old.next = old_to_new[current.next]
            old.random = old_to_new[current.random]
            current = current.next
        
        return old_to_new[head]

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

"""
1. Interleave the original and copied nodes in the same list.
2. Set the random pointers of the copied nodes by leveraging the interleaved structure.
3. Separate the copied nodes from the original nodes to form the final deep copy list.
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        # Add duplicate Nodes
        current = head
        while current:
            temp = current.next
            new = Node(current.val)
            current.next = new
            new.next = temp
            current = temp
        
        # Assign Random to duplicate nodes
        current = head
        while current:
            if current.random :
                current.next.random = current.random.next
            current = current.next.next

        # Remove the duplicate nodes 
        current = head
        new_head = current.next
        while current:
            new_node = current.next
            current.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            current = current.next
        
        return new_head
