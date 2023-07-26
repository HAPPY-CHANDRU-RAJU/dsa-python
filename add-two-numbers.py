"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

##### Optimal #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head, prev, carry = None, None, 0
        while l1 or l2:
            total = 0
            if l1:
                total += l1.val
            
            if l2:
                total += l2.val

            total += carry
            carry = total // 10
            total = total % 10

            node = ListNode(total, None)

            if head is None:
                prev = node
                head = node
            else:
                prev.next = node
                prev = node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry != 0:
            prev.next = ListNode(carry)
            prev = node
        
        return head
