"""
Rotate List

Given the head of a linked list, rotate the list to the right by k places.
"""

##### Optimal #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        
        len_ = 1
        curr = head
        
        while curr.next:
            curr = curr.next
            len_ += 1

        curr.next = head
        k = k % len_
        k = len_ - k

        while k > 0:
            curr = curr.next
            k -= 1
        
        head = curr.next
        curr.next = None

        return head


        
