"""
Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example :

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.

These are the only two combinations.
"""

##### Better  #####

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curr):
            if sum(curr) == target:
                if curr not in res:
                    res.append(curr.copy())
                return 
            
            if i >= len(candidates) or sum(curr) > target:
                return 

            dfs(i+1, curr+[candidates[i]])
            dfs(i+1, curr)
        
        dfs(0, [])
        return res

##### Optimal #####
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(ind, curr):
            if sum(curr) == target:
                res.append(curr.copy())
                return 
            for i in range(ind, len(candidates)):
                if sum(curr) + candidates[i] > target:
                    return
                
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                else:
                    dfs(i+1, curr+[candidates[i]])
        
        dfs(0, [])
        return res