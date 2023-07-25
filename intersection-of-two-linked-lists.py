"""
Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""


##### Optimal #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hs = set()
        while headA:
            hs.add(headA)
            headA = headA.next

        while headB:
            if headB in hs:
                return headB
            headB = headB.next
        
        return None
