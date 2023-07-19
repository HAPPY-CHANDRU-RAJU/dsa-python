"""
Three Sum
"""

# Time : O(n^2)
# Space : O(1)

# Optimal
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            
            l,r = i+1, len(nums)-1
            
            while l < r:
                sum_ = nums[l]+nums[r]+a
                if sum_  ==  0:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum_ > 0:
                    r -= 1
                else:
                    l += 1
        return res

