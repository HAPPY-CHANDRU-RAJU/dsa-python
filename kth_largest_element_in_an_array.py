"""
Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104


LINK : https://leetcodekth-largest-element-in-an-array.com/problems/kth-largest-element-in-an-array/description/
"""


# Brute Force
"""
    Time complexity     : (n log n)
    Space complexity    : (1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        nums.sort(reverse=True)
        return nums[k-1]

# Medium Effort
"""
    Time complexity     : (n log k)
    Space complexity    : (k)
"""
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in  nums[k:]:
            if num > min_heap[0]:
                heapq.heappop(min_heap)  
                heapq.heappush(min_heap, num) 

        return min_heap[0]  

# Optimal
"""
    Time complexity     : (n) 
    Space complexity    : (1)
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        def partition(left, right, pivot_index):
            pivot_value = nums[pivot_index]
            
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left

            for i in range(left, right):
                if nums[i] < pivot_value: 
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1

            nums[store_index], nums[right] = nums[right], nums[store_index]
            return store_index

        def quickselect(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            pivot_index = left + (right - left) // 2
            pivot_index = partition(left, right, pivot_index)

            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return quickselect(left, pivot_index - 1, k_smallest)
            else:
                return quickselect(pivot_index + 1, right, k_smallest)

        return quickselect(0, len(nums) - 1, len(nums) - k)
