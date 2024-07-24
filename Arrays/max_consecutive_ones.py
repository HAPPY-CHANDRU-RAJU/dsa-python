"""
Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

LINK : https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
"""

# Solution
"""
    Time complexity     : (n), where n is the length of the arr
    Space complexity    : (1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = 0, 0
        indx = 0
        n = len(nums)
        while indx < n:
            if nums[indx] == 1:
                count += 1
                indx += 1
                while indx < n and nums[indx] == 1:
                    count += 1
                    indx += 1
            else:
                max_count = max(max_count, count)
                count = 0
                indx += 1
        max_count = max(max_count, count)
        
        return max_count