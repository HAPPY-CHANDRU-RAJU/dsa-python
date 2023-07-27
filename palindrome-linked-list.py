"""
palindrome-linked-list

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

##### Better #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        list_ = ""
        while curr:
            list_ += str(curr.val)
            curr = curr.next

        return list_ == list_[::-1]



##### Optimal #####

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left, right = self.findLeftandRight(head)
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    def findLeftandRight(self, head):
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next    # Logic
        
        if fast:
            slow = slow.next

        return prev, slow

