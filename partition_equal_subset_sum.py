"""
Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
Input: nums = [1,5,11,5]
Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

LINK : https://leetcode.com/problems/partition-equal-subset-sum/description/
"""

# Brute Force
"""
    Time complexity     : (2^n)
    Space complexity    : (n)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:        
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total//2
        nums.sort(reverse=True)

        def backtrace(current_sum, indx):
            if current_sum == target:
                return True
            
            if current_sum > target or indx >= len(nums):
                return False
            
            if backtrace(current_sum+nums[indx], indx+1):
                return True
            
            return backtrace(current_sum, indx+1)
        
        return backtrace(0, 0)

# Medium Effort - Memorisation
"""
    Time complexity     : (n * target)
    Space complexity    : (n * target)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:        
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total//2
        memo = {}
        def backtrace(current_sum, indx):
            if current_sum == target:
                return True
            
            if current_sum > target or indx >= len(nums):
                return False

            if (indx, current_sum) in memo:
                return memo[(indx, current_sum)]
            
            include =  backtrace(current_sum+nums[indx], indx+1)
            exclude = backtrace(current_sum, indx+1)

            memo[(indx, current_sum )] = include or exclude 
            return memo[(indx, current_sum)]
        
        return backtrace(0, 0)


# Optimal - Tabulation
"""
    Time complexity     : (n * target)
    Space complexity    : (target)
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:        
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total//2

        dp = [False]*(target+1)
        dp[0] = True

        for num in nums:
            for t in range(target, num-1, -1):
                if not dp[t]:
                    dp[t] = dp[t - num]
        
        return dp[target]