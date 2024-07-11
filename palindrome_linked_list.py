"""
Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 
Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?

LINK : https://leetcode.com/problems/palindrome-linked-list/
"""

# Brute Force
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values == values[::-1]


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

"""
Approach:

Use two pointers to find the middle of the linked list.
Reverse the second half of the list in place.
Compare the first half and the reversed second half of the list.
Restore the list to its original state in a single pass.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        first_half = self.find_middle(head)
        second_half  = self.reverse_list(first_half.next)
        
        p1 = head
        p2 = second_half
        result = True
        while result and p2:
            if p1.val != p2.val:
                result = False
            p1 = p1.next
            p2 = p2.next
        
        first_half.next = self.reverse_list(second_half)
        return result
    
    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        return prev

    def find_middle(self, curr):
        slow = curr
        fast = curr
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow