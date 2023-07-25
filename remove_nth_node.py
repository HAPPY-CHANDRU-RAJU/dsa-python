"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

##### Optimal #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_ = self.nodeLength(head)
        if len_ == n:
            return head.next
        res = head
        for _ in range(len_-n-1):
            head = head.next
        
        if self.nodeLength(head) < 2:
            head.next = None
            return res
        
        temp = head.next.next
        head.next = temp
        return res
    
    def nodeLength(self,temp):
        i = 0
        while temp:
            temp = temp.next
            i += 1
        return i
