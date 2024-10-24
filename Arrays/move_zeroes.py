"""
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.


Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

LINK : https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
"""

"""
    Time complexity     : 
    Space complexity    : 
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_indx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_indx], nums[i] = nums[i], nums[last_indx]
                last_indx += 1
        