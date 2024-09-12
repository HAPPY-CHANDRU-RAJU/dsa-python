"""
Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.


Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

LINK : https://leetcode.com/problems/sliding-window-maximum/description/
"""

# Brute Force
"""
    Time complexity     : (n*k)
    Space complexity    : (n-k+1)
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        max_res = []
        n = len(nums)
        for i in range(0, n-k+1):
            max_res.append(max(nums[i:i+k]))
        return max_res


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n-k+1) 
"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        The Solution:
            Use a Deque: 
                - The deque will store indices of elements from nums in a way that the values corresponding to these indices are in a non-increasing order. The front of the deque will always have the index of the maximum value for the current window.

            Slide the Window:
                - For each new element in nums, remove indices from the back of the deque if the current element is greater than the elements corresponding to these indices. This ensures that the deque remains useful for finding maximums efficiently.
                - Remove the front element of the deque if it is out of the current window.
                -  Append the current index to the deque.
                - The front of the deque holds the index of the maximum element for the current window, so add it to the result.

        """
        if not nums:
            return []
        
        dq = deque()
        max_res = []

        for i in range(len(nums)):
            if dq and dq[0] < i-k+1:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            if i >= k-1:
                max_res.append(nums[dq[0]])

        return max_res
