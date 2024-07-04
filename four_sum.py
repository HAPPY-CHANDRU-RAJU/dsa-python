"""
4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] 
such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.

nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
 
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 
Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

LINK : https://leetcode.com/problems/4sum/description/
"""

# Brute Force
"""
    Time complexity     : (n^4)
    Space complexity    : (n)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i]+nums[j]+nums[k]+nums[l] == target:
                            res.add((nums[i], nums[j], nums[k], nums[l]))
        return res


# Optimal
"""
    Time complexity     : (n^3)
    Space complexity    : (m), where m is the number of quadruplets found. Excluding the output list, it is O(1).
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res, quad = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i-1] == nums[i] : 
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            
            l, r = start, len(nums)-1
            while l < r:
                sum_ = nums[l]+nums[r]
                if sum_ == target:
                    res.append(quad+[nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                elif sum_ > target:
                    r -= 1
                else:
                    l += 1

        kSum(4, 0, target)
        return res
