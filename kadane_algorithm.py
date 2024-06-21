"""
Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.


Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6

Explanation: The subarray [4,-1,2,1] has the largest sum 6.


Example 2:
Input: nums = [1]
Output: 1

Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

LINK : https://leetcode.com/problems/maximum-subarray/description/
"""

# Brute Force
"""
    Time complexity     :  (n^3)
    Space complexity    : 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        max_ = -sys.maxsize-1

        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                sum_ = sum(nums[i: j+1])
                max_ = max(max_, sum_)
        return max_



# Medium 
"""
    Time complexity     :  (n^2)
    Space complexity    : 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        max_ = -sys.maxsize-1

        n = len(nums)
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                max_ = max(max_, sum_)
        return max_


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : 
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        max_ = -sys.maxsize-1

        n = len(nums)
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            max_ = max(max_, sum_)
            if sum_ <= 0:
                sum_ = 0
        return max_
