"""
Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""

##### Optimal #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ 
            1. store groupprev and groupnext by k nodes 
            2. Reverse group
            3. link groupPrev with kth 
        """
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
    
    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr