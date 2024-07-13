"""
Flatten A Linked List

You are given a linked list containing 'n' 'head' nodes, where every node in the linked list contains two pointers:

(1) ‘next’ which points to the next node in the list
(2) ‘child’ pointer to a linked list where the current node is the head.

Each of these child linked lists is in sorted order and connected by 'child' pointer.
Your task is to flatten this linked such that all nodes appear in a single layer or level in a 'sorted order'.

Example:
Input: Given linked list is:
Output:
1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 12 → 20 → null.

Explanation:
The returned linked list should be in a sorted order. All the elements in this returned linked list are connected by 'child' pointers and 'next' pointers point to null.

LINK : https://www.naukri.com/code360/problems/flatten-a-linked-list
"""

# Optimal
"""
    Time complexity     : 
    Space complexity    : 
"""
class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child

def merge(l1, l2):
    dummyNode = Node(-1)
    res = dummyNode

    while l1 and l2:
        if l1.data < l2.data:
            res.child = l1
            res = l1
            l1 = l1.child
        else:
            res.child = l2
            res = l2
            l2 = l2.child
        res.next = None
    
    if l1:
        res.child = l1
    else:
        res.child = l2
    
    if dummyNode.child:
        dummyNode.child.next = None
    
    return dummyNode.child


def flattenLinkedList(head: Node) -> Node:
    if not head or not head.next:
        return head
    
    Mergedhead = flattenLinkedList(head.next)
    head = merge(head, Mergedhead)
    return head


