"""
3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that :
    The solution set must not contain duplicate triplets. 
    The order of the output and the order of the triplets does not matter.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:
Input: nums = [0,1,1]
Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105

LINK : https://leetcode.com/problems/3sum/description/
"""

# Brute Force
"""
    Time complexity     : (n^3)
    Space complexity    : (n)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        tmp = tuple(sorted((nums[i], nums[j], nums[k])))
                        res.add( tmp )
        return res


# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() # sort the nums
        
        res = set()
        for i in range(n):
            target = -nums[i]
            seen = set()
            for j in range(i+1, n):
                compliment = target - nums[j]
                if compliment in seen:
                    res.add((nums[i], nums[j], compliment))
                seen.add(nums[j])
        return res

# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (k), where k is the number of unique triplets in the result list. Excluding the result list, the space complexity is O(1).
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            l, r = i+1, n-1

            while l < r:
                sum_ = a+nums[l]+nums[r]
                if sum_ == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
                elif sum_ > 0:
                    r -= 1
                else:
                    l += 1
        return res