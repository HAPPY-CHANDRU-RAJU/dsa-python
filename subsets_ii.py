"""
Subsets II
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

LINK : https://leetcode.com/problems/subsets-ii/description/
"""

# Brute Force
"""
    Time complexity     : (n ⋅ 4^n)
    Space complexity    : (n ⋅ 2^n)
"""
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = list()
    n = len(nums)
    def backtrace(start, sub_res):
        sub_res.sort()
        if sub_res not in res:  
            res.append(sub_res)
        for i in range(start, n):
            backtrace(i+1, sub_res+[nums[i]])
    
    backtrace(0, [])
    return res
    

# Optimal
"""
    Time complexity     : (2^n)
    Space complexity    : (n ⋅ 2^n)
"""
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = list()
    n = len(nums)
    nums.sort()
    def backtrace(start, sub_res):
        res.append(sub_res)
        for i in range(start, n):
            if i > start and nums[i-1] == nums[i]:
                continue
            backtrace(i+1, sub_res+[nums[i]])
    
    backtrace(0, [])
    return res