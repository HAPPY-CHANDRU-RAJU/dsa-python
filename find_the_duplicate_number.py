"""
Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

 
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
 

Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n

All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:
> How can we prove that at least one duplicate number must exist in nums?
> Can you solve the problem in linear runtime complexity?

LINK : https://leetcode.com/problems/find-the-duplicate-number/description/

"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return nums[i]

# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 1
            else:
                return i


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point of the two runners
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Finding the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare