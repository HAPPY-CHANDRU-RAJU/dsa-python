"""
Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

LINK : https://leetcode.com/problems/max-consecutive-ones/description/
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count = 0
                while i < len(nums) and nums[i] == 1:
                    count += 1
                    i += 1
                max_count = max(max_count, count)
        return max_count

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_, count = 0, 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                max_ = max(max_, count)
                count = 0
        max_ = max(max_, count)

        return max_
