"""
Maximum XOR of Two Numbers in an Array

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:
1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
"""

#####  Brute Force  #####
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = -9999
        for i in range(n):
            for j in range(i, n):
                max_num = max(max_num, nums[i]^nums[j])
        return max_num


##### Better  #####
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, output = 0, 0
        
        for i in range(32, -1, -1):
            mask = mask | 1 << i
            founds = set([n & mask for n in nums])
            temp = output | 1 << i
            for found in founds:
                if found^temp in founds:
                    output = temp
        return output
        

