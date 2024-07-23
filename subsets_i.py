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

LINK : https://leetcode.com/problems/subsets/description/
"""

# Optimal
"""
    Time complexity     : (2^n)
    Space complexity    : (n ⋅ 2^n)
"""
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    n = len(nums)
    def backtrace(start, sub_res):
        res.append(sub_res)
        for i in range(start, n):
            backtrace(i+1, sub_res+[nums[i]])
    backtrace(0, [])
    return res
