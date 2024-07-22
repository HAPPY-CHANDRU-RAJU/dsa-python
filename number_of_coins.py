"""
Number of Coins

Given a value V and array coins[] of size M, the task is to make the change for V cents, given that you have an infinite supply of each of coins{coins1, coins2, ..., coinsm} valued coins. Find the minimum number of coins to make the change. If not possible to make change then return -1.

Example 1:
Input: V = 30, M = 3, coins[] = {25, 10, 5}
Output: 2

Explanation: Use one 25 cent coin and one 5 cent coin

Example 2:
Input: V = 11, M = 4,coins[] = {9, 6, 5, 1} 
Output: 2 

Explanation: Use one 6 cent coin and one 5 cent coin

Your Task:  
You don't need to read input or print anything. Complete the function minCoins() which takes V, M and array coins as input parameters and returns the answer.

Expected Time Complexity: O(V*M)
Expected Auxiliary Space: O(V)

Constraints:
1 ≤ V*M ≤ 106
All array elements are distinct

LINK : https://www.geeksforgeeks.org/problems/number-of-coins
"""

# Brute Force
"""
    Time complexity     : (V^M)         # Exponential
    Space complexity    : (V)
"""
def minCoins(self, coins, m, V):
		if V == 0:
		    return 0
		    
		res = sys.maxsize
		for i in range(m):
		    if coins[i] <= V:
		        sub_res = self.minCoins(coins, m, V-coins[i])
		        
		        if sub_res != sys.maxsize and sub_res+1 < res:
                    res = sub_res + 1		        
		 
		return res

# Optimal
"""
    Time complexity     : (V*M)         # Polynomial
    Space complexity    : (V)
"""
# The dynamic programming approach reduces the time complexity from exponential to polynomial.
def minCoins(self, coins, m, V):
    dp = [float('inf')]*(V+1)
    dp[0] = 0
    
    for i in range(1, V+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
                
    return dp[V]  if dp[V] != float('inf') else -1