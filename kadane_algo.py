"""
Kadane's Algorithm : Maximum Subarray Sum in an Array
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.
"""

# Brute Force
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


# Better
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
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = -999999

        n = len(nums)
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            max_ = max(max_, sum_)
            if sum_ <= 0 :
                sum_ = 0
        return max_
