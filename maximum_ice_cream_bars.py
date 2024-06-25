"""
Maximum Ice Cream Bars

It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

Note: The boy can buy the ice cream bars in any order.

Return the maximum number of ice cream bars the boy can buy with coins coins.
You must solve the problem by counting sort.

 
Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4

Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.

Example 2:
Input: costs = [10,6,8,7,7,8], coins = 5
Output: 0

Explanation: The boy cannot afford any of the ice cream bars.

Example 3:
Input: costs = [1,6,3,1,2,5], coins = 20
Output: 6

Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.

LINK : https://leetcode.com/problems/maximum-ice-cream-bars/
"""

# Medium 
"""
    Time complexity     : (n log n)
    Space complexity    : (1)
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        max_icecream = 0
        remaining_cost = coins
        for cost in costs:
            if (remaining_cost - cost) >= 0:
                remaining_cost -= cost
                max_icecream += 1
        return max_icecream


# Optimal
"""
    Time complexity     : (n+k)
    Space complexity    : (k)
"""
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_cost = max(costs)
        count  = [0]*(max_cost+1)

        for cost in costs:
            count[cost] += 1

        ice_creams = 0
        for cost in range(1, max_cost+1):
            if count[cost] == 0:
                continue
            if coins >= cost:
                nums_ice_cream = min(count[cost], coins//cost ) # ( coins // cost ) is minimum afforable ice creams
                ice_creams += nums_ice_cream
                coins -= nums_ice_cream * cost
            else:
                break
        
        return ice_creams