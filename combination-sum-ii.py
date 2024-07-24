"""
Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

LINK : https://leetcode.com/problems/combination-sum-ii/description/
"""

# Optimal
"""
    Time complexity     : ( 2^n )
    Space complexity    : ( n * 2^n )
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        n = len(candidates)
        def backtrack(start, curr_sum, curr_combination):
            if curr_sum == target:
                res.append(curr_combination.copy())
                return

            if curr_sum > target:
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr_combination.append(candidates[i])
                backtrack(i+1, curr_sum+candidates[i], curr_combination )
                curr_combination.pop()
                
        backtrack(0, 0, [])
        return res
