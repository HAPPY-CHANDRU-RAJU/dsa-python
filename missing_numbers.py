"""
Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

# Brute Force
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        return -1
   
# Optimal
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # cur_sum = sum(nums)
        # act_sum = (len(nums) * (len(nums) + 1)//2)
        return (len(nums) * (len(nums) + 1)//2) - sum(nums)
