"""
Middle of the Linked List


Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

"""

##### Optimal #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        if fast.next is not None:
            slow = slow.next

        return slow
