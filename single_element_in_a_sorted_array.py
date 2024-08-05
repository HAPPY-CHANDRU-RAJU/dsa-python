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
 
Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105

LINK : https://leetcode.com/problems/single-element-in-a-sorted-array/
"""

# Brute Force
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if num in res:
                res.remove(num)
            else:
                res.append(num)
        return res[-1]


# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]

# Optimal
"""
    Time complexity     : (log n)
    Space complexity    : (1)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[-1]
        
        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]
            
        low, high = 1, n-2
        while low <= high:
            mid = (low+high)//2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1] :
                return nums[mid]
            if ( mid%2 == 1 and nums[mid] == nums[mid-1] ) or ( mid%2 == 0 and  nums[mid] == nums[mid+1]):
                low = mid+1
            else:
                high = mid-1
        return -1
        


