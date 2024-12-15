"""
0 1 Knapsack

A thief is robbing a store and can carry a maximal weight of W into his knapsack. There are N items and the ith item weighs wi and is of value vi. Considering the constraints of the maximum weight that a knapsack can carry, you have to find and return the maximum value that a thief can generate by stealing items.

Sample Input:
1 
4
1 2 4 5
5 4 8 6
5

Sample Output:
13

Constraints:
1 <= T <= 10
1 <= N <= 10^2
1<= wi <= 50
1 <= vi <= 10^2
1 <= W <= 10^3

Time Limit: 1 second

LINK : https://www.naukri.com/code360/problems/0-1-knapsack_920542?leftPanelTabValue=PROBLEM
"""

# Brute Force
"""
    Time complexity     : (2^n)
    Space complexity    : (n)
"""
def knapsack(n, wi, vi, W):
    if n == 0 or W == 0 :
        return 0
    
    if wi[n-1] <= W:
        include = vi[n-1] + knapsack(n-1, wi, vi, W-wi[n-1])
        exclude = knapsack(n-1, wi, vi, W)
        return max(include, exclude)
    else:
        return knapsack(n-1, wi, vi, W)
    

# Medium Effort
"""
    Time complexity     : (n*W) # W means Capacity
    Space complexity    : (n*W) # W means Capacity
"""
def knapsack(n, wi, vi, W):
    dp = [[0 for i in range(W+1)] for _ in range(n+1)]  
    
    for i in range(1, n+1):
        for w in range(W+1):
            if wi[i-1] <= w:
                dp[i][w] = max(
                    dp[i-1][w],
                    vi[i-1] + dp[i-1][w-wi[i-1]]
                )
            else:
                dp[i][w] = dp[i-1][w]
    return dp[i][W]

# Optimal
"""
    Time complexity     : (n*W)
    Space complexity    : (W)
"""

def knapsack(n, wi, vi, W):
    prev = [0 for i in range(W+1)]

    for i in range(wi[0], W+1):
        prev[i] = vi[0]
    
    for ind in range(1, n):
        for cap in range(W, -1, -1):
            not_taken = 0 + prev[cap]

            taken = float('-inf')
            if wi[ind] <= cap:
               taken = vi[ind] + prev[cap- wi[ind]]
            
            prev[cap] = max(taken, not_taken)
    
    return prev[W]