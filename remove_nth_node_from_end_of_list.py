"""
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
Follow up: Could you do this in one pass?

LINK : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

"""
    Time complexity     : (L), where L is the length of the linked list. This includes one pass to calculate the length and another pass to reach the node to be removed.
    Space complexity    : (1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lengthNode(head)
        res = curr = head

        if length == n:
            return res.next

        for _ in range(length-n-1):
            curr = curr.next
        
        if self.lengthNode(curr) < 2:
            curr.next = None
            return res
        
        curr.next = curr.next.next
        return res

        return curr
    
    def lengthNode(self, temp):
        i = 0
        while temp:
            temp = temp.next
            i += 1
        return i