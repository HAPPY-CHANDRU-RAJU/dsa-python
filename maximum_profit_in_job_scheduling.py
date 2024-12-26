"""
Maximum Profit in Job Scheduling

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
If you choose a job that ends at time X you will be able to start another job that starts at time X.


Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120

Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150

Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104

LINK : https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
"""

# Brute Force
"""
    Time complexity     : O(2^n * n log n)
    Space complexity    : O(n)
"""

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = list(zip(startTime, endTime, profit))
        n = len(intervals)
        
        solutions = []

        def greedy_non_overlap(intervals):
            intervals.sort(key=lambda x: x[1])
            last_end_time = -1
            curr_profit = 0
            for start, end, profit in intervals:
                if start >= last_end_time:
                    curr_profit += profit
                    last_end_time = end
            return curr_profit

        max_profit = float('-inf')
        for i in range(1 << n):
            subsets = [ intervals[j] for j in range(n) if i & (1 << j)]
            current_profit = greedy_non_overlap(subsets)
            max_profit = max(current_profit, max_profit)

        return max_profit


# Medium Effort
"""
    Time complexity     : O(n log n)
    Space complexity    : O(n)
"""
from bisect import bisect_right
from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        intervals = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [0] * (n + 1)  

        end_times = [interval[1] for interval in intervals]
        for i in range(1, n + 1):
            start, end, profit = intervals[i - 1] 
            j = bisect_right(end_times[:i-1], start) 
            dp[i] = max(dp[i - 1], dp[j] + profit)

        return dp[n]

# Optimal
"""
    Time complexity     : O(n log n)
    Space complexity    : O(n)
"""

from bisect import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect(dp, [s + 1]) - 1

            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        
        return dp[-1][1]