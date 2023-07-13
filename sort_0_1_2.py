"""
Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

 
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

# Better
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        cnt0 = 0
        cnt1 = 0
        cnt2 = 0

        for i in range(n):
            if nums[i] == 0:
                cnt0 += 1
            elif nums[i] == 1:
                cnt1 += 1
            elif nums[i] == 2:
                cnt2 += 1
        
        for i in range(cnt0):
            nums[i] = 0
        
        for i in range(cnt0, cnt0+cnt1):
            nums[i] = 1
        
        for i in range(cnt0+cnt1, n):
            nums[i] = 2

# Optimal
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[mid] , nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] =  nums[mid], nums[high]
                high -= 1
