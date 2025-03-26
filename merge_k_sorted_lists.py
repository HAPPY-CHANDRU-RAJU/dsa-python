"""
Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]

merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.

LINK : https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Optimal
"""
    Time Complexity     :   O(N log k)
    Space Complexity    :   O(1) (ignoring output) or O(k) (including auxiliary storage)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, ll1, ll2):
        curr = dummy = ListNode()
        
        while ll1 and ll2:
            if ll1.val < ll2.val:
                curr.next, ll1 = ll1, ll1.next
            else:
                curr.next, ll2 = ll2, ll2.next
            curr = curr.next

        curr.next = ll1 or ll2
        return dummy.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                ll1 = lists[i]
                ll2 = lists[i+1] if i+1 < len(lists) else None
                merged_lists.append(self.merge(ll1, ll2))
            lists = merged_lists

        return lists[0] if lists else None
