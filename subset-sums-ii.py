"""

"""


##### Better  #####

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subsetSumUtil(arr, n, ind, res):
            if res not in ans:
                ans.append(res)
            if n == ind:
                return
            subsetSumUtil(arr, n, ind+1, res+[arr[ind]])
            subsetSumUtil(arr, n, ind+1, res)
        subsetSumUtil(nums, len(nums), 0, [])
        ans.sort()
        return ans



##### Optimal #####
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        def subsetsWithDupUtil(ind, res):
            ans.append(res)
            for i in range(ind, n):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                subsetsWithDupUtil(i+1, res+[nums[i]])
        subsetsWithDupUtil(0, [])
        return ans
        