"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

# Optimal
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        m = []
        intervals.sort(key=lambda x: x[0])
        m.append(intervals[0])
        for i in intervals[1:]:
            if i[0] <= m[-1][1]:
                if i[1] >= m[-1][1]:
                    m[-1][1] = i[1]
            else:
                m.append(i)
        return m
                