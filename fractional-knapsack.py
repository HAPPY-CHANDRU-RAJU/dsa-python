"""
Fractional Knapsack


Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item. 

Example 1:

Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}

Output:
240.00

Explanation:Total maximum value of item we can have is 240.00 from the given capacity of sack. 
"""

# Intution
"""
Step 1 : Find ratio of  values/weight of list
Step 2 : Sort the list based on ration
Step 3 : loop through list
Step 4 : if Weight - curr_weight >= 0 then add the profit otherwise check Weight > 0 then ( Weight * ration ) add the profit
"""

##### Optimal #####
        
class Solution:    
    def fractionalknapsack(self, W,arr,n):
        items = [ (arr[i], arr[i].value/arr[i].weight) for i in range(n) ]
        items.sort(key=lambda x: x[1], reverse=True)  # Highest ratio first
        
        profit = 0
        for item in items:
            if W - item[0].weight >= 0:
                profit += item[0].value
                W -= item[0].weight
            
            elif W > 0 :
                profit += W * item[1]
                W = 0
        
        return profit
        
