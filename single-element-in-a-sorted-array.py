"""
Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space.

Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

"""

#####  Brute Force  #####
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

##### Better  #####
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)//2
            if mid%2 == 1:
                mid -= 1
            if nums[mid] != nums[mid+1]:
                right = mid
            else:
                left = mid+2
        return nums[left] 

##### Optimal #####
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)
            
