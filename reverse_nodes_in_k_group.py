"""
Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

Follow-up: Can you solve the problem in O(1) extra memory space?

LINK : https://leetcode.com/problems/reverse-nodes-in-k-group/description/
"""


# Medium
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kthNode =  self.kthNode(groupPrev, k)
            if not kthNode:
                break
            
            groupNext = kthNode.next

            prev, curr = kthNode.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = temp

        return dummy.next
    
    def kthNode(self, curr, k):
        while curr and k > 0:
            k -= 1
            curr = curr.next
        return curr


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy
        tail = dummy

        while True:
            count = 0
            while tail and count < k:
                count += 1
                tail = tail.next
            if not tail:
                break

            head = prev.next
            while prev.next != tail:
                curr = prev.next
                prev.next = curr.next
                curr.next = tail.next
                tail.next = curr
            
            tail = head
            prev = head

        return dummy.next
