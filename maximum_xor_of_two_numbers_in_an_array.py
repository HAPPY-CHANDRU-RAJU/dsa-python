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

LINK : https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        n = len(nums)

        for i in range(n-1):
            for j in range(i+1, n):
                max_xor = max( nums[i]^nums[j], max_xor) 
        return max_xor

# Optimal - Bit Manipulation
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, output = 0, 0
        for i in range(32, -1, -1):
            mask = mask | 1 << i
            founds = set([num & mask for num in nums])
            temp = output | 1 << i
            for found in founds:
                if found^temp in founds:
                    output = temp
        return output
        

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class TrieNode:
    def __init__(self):
        self.binaryNode = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.binaryNode:
                node.binaryNode[bit] = TrieNode()
            node = node.binaryNode[bit]
    
    def getmax(self, num):
        node = self.root
        maxnum = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if 1-bit in node.binaryNode:
                maxnum = maxnum | (1 << i)
                node = node.binaryNode[1-bit]
            else:
                node = node.binaryNode[bit]
        return maxnum
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        obj = Trie()
        for num in nums:
            obj.insert(num)
        
        max_ = -float('inf')
        for num in nums:
            max_ = max(obj.getmax(num), max_)
        
        return max_
        