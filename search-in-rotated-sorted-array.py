"""
Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""

#####  Brute Force  #####
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(nums, low, high):
            if high < low:
                return -1
            if high == low:
                return low
            
            mid = (high+low)//2

            if mid < high and nums[mid] > nums[mid+1]:
                return mid
            if mid > low and nums[mid] < nums[mid-1]:
                return mid-1
            if nums[low] >= nums[mid]:
                return findPivot(nums, low, mid-1)
            return findPivot(nums, mid+1, high)

        def binarySearch(nums, low, high, key):
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == key:
                    return mid
                
                if key > nums[mid] :
                    low = (mid+1)
                else:
                    high = (mid-1)

            return -1
            
        n = len(nums)
        pivot =  findPivot(nums, 0, n-1)
        if pivot == -1:
            return binarySearch(nums, 0, n-1, target)
        
        if nums[pivot] == target:
            return pivot
        if nums[0] <= target:
            return binarySearch(nums, 0, pivot-1, target)
        return binarySearch(nums, pivot+1, n-1, target)

        
##### Better  #####
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
        