"""
Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?

LINK : https://leetcode.com/problems/majority-element/
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            if nums.count(num) > (n//2):
                return num

# Brute Force 
"""
    Time complexity     : (n log n)
    Space complexity    : (1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > len(nums) // 2:
                return num

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

""" Boyer-Moore Voting Algorithm """
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        ele = None

        for num in nums:
            if cnt == 0:
                ele = num
            cnt += (1 if num == ele else -1)
        
        cnt  = 0
        for num in nums:
            if num == ele:
                cnt += 1
        
        if cnt > (len(nums)//2) :
            return ele
        return -1