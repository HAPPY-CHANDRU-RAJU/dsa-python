"""
Rod cutting problem

Given a rod of length ‘N’ units. The rod can be cut into different sizes and each size has a cost associated with it. Determine the maximum cost obtained by cutting the rod and selling its pieces.

Note:
1. The sizes will range from 1 to ‘N’ and will be integers.
2. The sum of the pieces cut should be equal to ‘N’.
3. Consider 1-based indexing.

Sample Input 1:
2
5
2 5 7 8 10
8
3 5 8 9 10 17 17 20

Sample Output 1:
12
24

Explanation of sample input 1:
Test case 1:
All possible partitions are:
1,1,1,1,1           max_cost=(2+2+2+2+2)=10
1,1,1,2             max_cost=(2+2+2+5)=11
1,1,3               max_cost=(2+2+7)=11
1,4                 max_cost=(2+8)=10
5                   max_cost=(10)=10
2,3                 max_cost=(5+7)=12
1,2,2               max _cost=(1+5+5)=12    

Clearly, if we cut the rod into lengths 1,2,2, or 2,3, we get the maximum cost which is 12.


Test case 2:
Possible partitions are:
1,1,1,1,1,1,1,1         max_cost=(3+3+3+3+3+3+3+3)=24
1,1,1,1,1,1,2           max_cost=(3+3+3+3+3+3+5)=23
1,1,1,1,2,2             max_cost=(3+3+3+3+5+5)=22
and so on….

If we cut the rod into 8 pieces of length 1, for each piece 3 adds up to the cost. Hence for 8 pieces, we get 8*3 = 24.

Sample Input 2:
1
6
3 5 6 7 10 12

Sample Output 2:
18

Constraints:
1 <= T <= 50
1 <= N <= 100
1 <= A[i] <= 100

Where ‘T’ is the total number of test cases, ‘N’ denotes the length of the rod, and A[i] is the cost of sub-length.

Time limit: 1 sec.

LINK : https://www.naukri.com/code360/problems/rod-cutting-problem_800284?leftPanelTabValue=PROBLEM
"""


# Medium Effort
"""
    Time complexity     : (n^2)
    Space complexity    : (n^2)
"""
def cutRod(price, n):
    memo = {}
    def subset(indx, current_sum):
        nonlocal memo
        if indx < 0 or current_sum <= 0:
            return 0
        
        if (indx, current_sum) in memo:
            return memo[(indx, current_sum)]

        exclude = subset(indx-1, current_sum)
    
        include = 0
        if indx+1 <= current_sum:
            include = price[indx] + subset(indx, current_sum-(indx+1))
        
        memo[(indx, current_sum)] = max(include, exclude)
        return memo[(indx, current_sum)] 
    
    result = subset(n-1, n)
    return result

# Optimal
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""
def cutRod(price, n):
    dp = [0]*(n+1)

    # Iterate over all rod lengths
    for i in range(1, n+1):
        # Iterate over possible cuts
        for j in range(1, i+1):
            dp[i] = max(dp[i], price[j-1]+dp[i-j])

    return dp[i]

#  Greedy ( fractional knapsack ) - Not For All Cases but still its optimal way to solve this problem
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
def cutRod(price, n):
    # Sort the prices by price-to-length ratio in descending order
    prices = sorted([(i+1, p) for i, p in enumerate(price)], key=lambda x: x[1]/x[0], reverse=True)
    
    amount = 0
    indx = 0

    # Try to cut the rod in pieces
    while n > 0 and indx < len(prices):
        length, price = prices[indx]
        max_cut = n // length
        
        amount += (max_cut * price)
        n -= (max_cut * length)
        
        indx += 1
        
    return amount
