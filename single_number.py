"""
Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 
Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

LINK : https://leetcode.com/problems/single-number/description/
"""

# Brute Force
"""
    Time complexity     : (n log n)
    Space complexity    : ( 1 )
"""
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        nums.sort()
        print(nums)
        i = 0
        while i < n-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2

        return nums[-1]


# Medium Effort
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num, freq in Counter(nums).items():
            if freq == 1:
                return num

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result