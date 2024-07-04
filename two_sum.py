"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

LINK : https://leetcode.com/problems/two-sum/description/
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]+nums[j] == target:
                    return [i,j]

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hs = {}
        for i in range(n):
            rem = target - nums[i]
            if rem in hs:
                return [hs[rem], i]
            hs[nums[i]] = i