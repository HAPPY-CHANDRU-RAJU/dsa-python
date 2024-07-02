"""
Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109
 
Follow up: Could you solve the problem in linear time and in O(1) space?

LINK : https://leetcode.com/problems/majority-element-ii/description/
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = set()
        for num in nums:
            if nums.count(num) > (n//3):
                result.add(num)
        return result

# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = set()
        counter_dict = dict(Counter(nums))
        for num in counter_dict.items():
            if num[1] > (len(nums)//3):
                result.add(num[0])
        return result

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

""" Boyer-Moore Voting Algorithm """
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1, ele2 = None, None
        cnt1 = cnt2 = 0

        for num in nums:
            if cnt1 == 0 and num != ele2:
                cnt1 = 1
                ele1 = num
            elif cnt2 == 0 and num != ele1:
                cnt2 = 1
                ele2 = num
            elif num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == ele1:
                cnt1 += 1
            if num == ele2:
                cnt2 += 1
        
        mini = int(len(nums)/3)+1
        
        result = []
        if cnt1 >= mini:
            result.append(ele1)
        if cnt2 >= mini:
            result.append(ele2)

        return result