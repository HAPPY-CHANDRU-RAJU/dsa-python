"""
Best Time to Buy and Sell Stock
"""

# Optimal
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_ = prices[0]
        for i in range(len(prices)):
            min_ = min(min_, prices[i])
            profit = max( profit , (prices[i] - min_ ))
        return profit
