"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

LINK : https://leetcode.com/problems/trapping-rain-water/
"""

# Brute Force
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        n = len(height)
        for i in range(1, n-1):
            rain += min(max(height[:i+1]), max(height[i:])) - height[i]
        return rain

# Medium 
"""
    Time complexity     : (n)
    Space complexity    : (2n)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        n = len(height)

        max_ = height[0]
        prefixSum = [max_]
        for i in height[1:]:
            max_ = max(max_, i)
            prefixSum.append(max_)
        
        max_ = height[-1]
        suffixSum = [max_]
        for i in height[-1:0:-1]:
            max_ = max(max_, i)
            suffixSum.append(max_)
        suffixSum.reverse()

        for i in range(n):
            count = min(suffixSum[i], prefixSum[i]) - height[i]
            if count >= 1:
                rain += count
        return rain

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

"""
# Initialization:

rain: Variable to keep track of the total water trapped.
n: Length of the height list.
leftmax, rightmax: Variables to store the maximum height encountered from the left and right, respectively.
l, r: Two pointers, starting at the beginning (l = 0) and the end (r = n-1) of the height list.

# Two-Pointer Approach:
While l is less than r:
    If the height at the left pointer (height[l]) is less than or equal to the height at the right pointer (height[r]):
        If height[l] is greater than leftmax, update leftmax.
        Otherwise, add the difference between leftmax and height[l] to rain (this is the trapped water at index l).
        Move the left pointer one step to the right (l += 1).
    Otherwise:
        If height[r] is greater than rightmax, update rightmax.
        Otherwise, add the difference between rightmax and height[r] to rain (this is the trapped water at index r).
    Move the right pointer one step to the left (r -= 1).
    
Return the Total Trapped Water:

After the loop, the rain variable contains the total amount of trapped water, which is then returned.
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        rain = 0
        n = len(height)

        leftmax, rightmax = 0, 0
        l, r = 0, n-1
        while l < r:
            if height[l] <= height[r]:
                if height[l] > leftmax:
                    leftmax = height[l]
                else:
                    rain += (leftmax - height[l])
                l += 1
            else:
                if height[r] > rightmax:
                    rightmax = height[r]
                else:
                    rain += (rightmax - height[r])
                r -= 1
        return rain