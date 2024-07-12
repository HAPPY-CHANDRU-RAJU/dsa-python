"""
Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

LINK : https://leetcode.com/problems/rotate-list/
"""

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head

        len_ = 1
        curr = head
        while curr.next:
            len_ += 1
            curr = curr.next
        
        curr.next = head

        k = k % len_
        k = len_ - k

        while k > 0:
            k -= 1
            curr = curr.next

        head = curr.next
        curr.next = None

        return head
