"""
Largest Rectangle in Histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10

Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 
Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

LINK : https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            > Use a stack to keep track of bar indices.
            > Traverse through the histogram:
                - Push the index of the bar onto the stack if it's higher than the bar at the top of the stack.
                - If the current bar is lower than the stack's top, pop indices from the stack and calculate the area of rectangles with the popped bars as the smallest height.
            > Continue this until all bars are processed, and then calculate areas for the remaining bars in the stack.
        """
        stack = []
        max_area = 0
        index = 0

        while index < len(heights):
            if not stack or heights[index] >= heights[stack[-1]]:
                stack.append(index)
                index += 1
            else:
                top_of_stack = stack.pop()
                area = (
                    heights[top_of_stack] *
                    ((index-stack[-1]-1) if stack else index)
                )
                max_area = max(max_area, area)
            
        while stack:
            top_of_stack = stack.pop()
            area = (
                heights[top_of_stack] *
                ((index-stack[-1]-1) if stack else index)
            )
            max_area = max(max_area, area)
        
        return max_area
            