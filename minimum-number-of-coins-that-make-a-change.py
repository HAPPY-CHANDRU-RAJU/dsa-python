"""
Find minimum number of coins that make a given value

Given a value V, if we want to make a change for V cents, and we have an infinite supply of each of C = { C1, C2, .., Cm} valued coins, what is the minimum number of coins to make the change? If it’s not possible to make a change, print -1.

Examples:  

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents
"""

##### Better  #####

import sys
def minCoins(coins, m, V):
    res = sys.maxsize
    
    if V == 0:
        return 0
        
    for i in range(m):
        if coins[i] <= V:
            sub_res = minCoins(coins, m, V-coins[i])
            
            if sub_res != sys.maxsize and sub_res+1  < res:
                res = sub_res+1

    return res

coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is",minCoins(coins, m, V))



##### Optimal #####
import sys
def minCoinsFunc(coins, m, V, dp):
    res = sys.maxsize
    
    if V == 0:
        return 0
        
    if dp[V] != -1:
        return dp[V]
    
    for i in range(m):
        if coins[i] <= V:
            sub_res = minCoinsFunc(coins, m, V-coins[i], dp)
            
            if sub_res != sys.maxsize and sub_res+1  < res:
                res = sub_res+1

    dp[V] = res
    return res


def minCoins(coins, m, V):
    dp = [-1]*(V+1)
    
    return minCoinsFunc(coins, m, V, dp )

coins = [9, 6, 5, 1]
m = len(coins)
V = 11
print("Minimum coins required is",minCoins(coins, m, V))

