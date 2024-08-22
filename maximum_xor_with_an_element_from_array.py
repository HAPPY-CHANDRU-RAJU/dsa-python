"""
Maximum XOR With an Element From Array

You are given an array nums consisting of non-negative integers. You are also given a queries array, where queries[i] = [xi, mi].
The answer to the ith query is the maximum bitwise XOR value of xi and any element of nums that does not exceed mi. In other words, the answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger than mi, then the answer is -1.
Return an integer array answer where answer.length == queries.length and answer[i] is the answer to the ith query.

Example 1:
Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
Output: [3,3,7]

Explanation:
1) 0 and 1 are the only two integers not greater than 1. 0 XOR 3 = 3 and 1 XOR 3 = 2. The larger of the two is 3.
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

Example 2:
Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
Output: [15,-1,5]
 

Constraints:

1 <= nums.length, queries.length <= 105
queries[i].length == 2
0 <= nums[j], xi, mi <= 109

LINK : https://leetcode.com/problems/maximum-xor-with-an-element-from-array/description/
"""

# Brute Force
"""
    Time complexity     : (Q*n) # Q is the number of queries, and N is the number of elements in nums.
    Space complexity    : (Q)
"""
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        res = list()
        min_ele = min(nums)
        for i in range(n):
            x, m = queries[i]
            max_ = -1
            
            if min_ele > m:
                res.append(max_)
                continue

            for num in nums:
                if num > m:
                    continue
                max_ = max(max_, num^x)
            res.append(max_)
        return res

# Optimal
"""
    Time complexity     : (n log n+ q log q)
    Space complexity    : (n+q)
"""
class TrieNode:
    def __init__(self):
        self.binary = {}
        self.min_val = float('inf')

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit  = (num >> i) & 1
            if bit not in node.binary:
                node.binary[bit] = TrieNode()
            node = node.binary[bit]
            node.min_val = min(node.min_val, num)
    
    def maxXorWithLimit(self, x, limit):
        node = self.root

        max_num = 0
        for i in range(31, -1, -1):
            bit = (x >> i) & 1
            toggle_bit = 1-bit
            if toggle_bit in node.binary and node.binary[toggle_bit].min_val <= limit:
                max_num = max_num | (1<<i)
                node = node.binary[toggle_bit]
            elif bit in node.binary:
                node = node.binary[bit]
            else:
                return -1
        return max_num

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        
        trie = Trie()
        res = [-1] * len(queries)
        idx = 0
        
        for i, (x, m) in queries:
            while idx < len(nums) and nums[idx] <= m:
                trie.insert(nums[idx])
                idx += 1
            res[i] = trie.maxXorWithLimit(x, m)
        
        return res