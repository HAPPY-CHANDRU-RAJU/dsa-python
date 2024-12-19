"""
Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.


Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3

Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

LINK : https://leetcode.com/problems/coin-change/description/
"""

# Brute Force - Recursion
"""
    Time complexity     : O(S^N)  - S is the amount, N is the number of coins
    Space complexity    : O(S)    - Maximum depth of recursion
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coin_combination(current_sum):
            if current_sum < 0 :
                return float('inf')

            if current_sum == 0:
                return 0
            
            min_coins  = float('inf')
            for coin in coins:
                result = coin_combination(current_sum-coin)
                min_coins = min(result+1, min_coins)
            
            return min_coins
        
        result = coin_combination(amount)
        return result if result != float('inf') else -1

# Medium Effort - Memorization
"""
    Time complexity     : O(N * S) - S is the amount, N is the number of coins
    Space complexity    : O(S)     - Memo storage and recursion depth
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def coin_combination(current_sum):
            if current_sum < 0 :
                return float('inf')

            if current_sum == 0:
                return 0
            
            if current_sum in memo:
                return memo[current_sum]
            
            min_coins  = float('inf')
            for coin in coins:
                result = coin_combination(current_sum-coin)
                min_coins = min(result+1, min_coins)
            
            memo[current_sum] = min_coins
            return min_coins
        
        result = coin_combination(amount)
        return result if result != float('inf') else -1

# Optimal - Tabulation
"""
    Time complexity     : O(N * S) - S is the amount, N is the number of coins
    Space complexity    : O(S)     - Array dp of size amount+1
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        
        if amount == 0:
            return 0
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for current_amount in range(1, amount+1):
            for coin in coins:
                if current_amount >= coin:
                    dp[current_amount]= min(
                        dp[current_amount],
                        dp[current_amount-coin]+1
                    )
        
        return -1 if dp[amount] == amount+1 else dp[amount]


# Optimal - Tabulation using BFS
"""
    Time complexity     : O(N * S) - S is the amount, N is the number of coins
    Space complexity    : O(S)     - Due to the queue and visited set
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        queue = deque([(amount, 0)])  # (remaining_amount, steps)
        visited = set([amount])

        while queue:
            current_amount, steps = queue.popleft()
            
            for coin in coins:
                next_amount = current_amount - coin

                if next_amount == 0:
                    return steps + 1
                
                if next_amount > 0 and next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, steps + 1))
        
        return -1