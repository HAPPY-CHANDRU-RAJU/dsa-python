"""
Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]] 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.


LINK : https://leetcode.com/problems/subsets/
"""

# Optimal - Bit Manipulation
"""
    Time complexity     : (n * 2^n)
    Space complexity    : (n * 2^n)
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        power_set = 2**n
        for i in range(power_set):
            sub_res = []
            for j in range(n):
                if (i& (1<<j)) > 0:
                    sub_res.append(nums[j])

            if sub_res:
                res.append(sub_res)
        return res