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

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

LINK : https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

# Brute Force
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)

# Optimal
"""
    Time complexity     : (log n)
    Space complexity    : (1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            Algorithm:
            1. Initialize low to 0 and high to the last index of the array.
            2. While low is less than or equal to high:
                a. Calculate mid as the average of low and high.
                b. If the middle element is the target, return the index mid.
                c. Determine which part of the array is sorted:
                    i. If the left half is sorted:
                        - Check if the target is within this range:
                            - If the target is in the range, adjust high to mid - 1.
                            - Otherwise, adjust low to mid + 1.
                    ii. If the right half is sorted:
                        - Check if the target is within this range:
                            - If the target is in the range, adjust low to mid + 1.
                            - Otherwise, adjust high to mid - 1.
            3. If the target is not found, return -1.
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                # Left hand must be sorted
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                # Right hand must be sorted
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1