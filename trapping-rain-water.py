"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

##### Better  #####
class Solution:
    def trap(self, height: List[int]) -> int:
        pre = [height[0]]
        suf = [height[-1]]
        res = 0
        for i in height[1:]:
            pre.append(max(i,pre[-1]))
            
        for i in height[-2::-1]:
            suf.append(max(i,suf[-1]))
            
        suf.reverse()
        for i in range(len(height)):
            temp =(min(pre[i],suf[i])-height[i])
            res += temp
            
        return res

##### Optimal #####
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        left, right = 0,0
        l, r = 0 , n-1
        while l < r:
            if height[l] <= height[r]:
                if height[l] >= left:
                    left = height[l]
                else:
                    res += (left - height[l])
                l += 1
            else:
                if height[r] >= right:
                    right = height[r]
                else:
                    res += (right - height[r])
                r -= 1
        
        return res



