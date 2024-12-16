"""
Maximum Sum Increasing Subsequence

Ninja has recently joined the gym. He decides to lift dumbbells to build muscles. The rack contains dumbbells with varying weights. His strategy is to pick a dumbbell randomly from the rack and after exercising place it back to its original position. Now for the next exercise he can only pick dumbbells that are heavier and positioned right to the previously used. After completing all the exercises he has to tell the sum of weights of all dumbbells he picked to his trainer.

In order to impress his trainer he wants this sum to be as maximum as possible. As Ninja is saving energy for exercises, he asks you to help him choose dumbbells. Can you help Ninja to impress his trainer?

For example:
If the ‘RACK’ contains dumbbells with weights [5, 1,  2, 8], then the possible ways to choose dumbbells according to the given conditions are: [ 5 ], [ 1 ], [ 2 ], [ 8 ], [ 5, 8 ], [ 1, 2 ], [ 1, 2, 8 ], [ 2, 8 ].  Lifting dumbbells with weights [ 5, 8 ] gives the maximum sum of 13.

Sample Input 1 :
2
4
9 1 2 8 
1
8

Sample Output 1:
11
8

Explanation For Sample Output 1:
For the first test case:
[ 9 ], [ 1 ], [ 2 ], [ 8 ], [ 2, 8 ], [ 1, 2, 8 ], [ 1, 2  ], [ 1, 8 ]  these are the possible increasing dumbbell weights in which there is only one way i.e  [  1 , 2 , 8 ] to have a maximum sum of 11.

For the second test case:
There is only one dumbbell so the maximum weight that can be lifted is 8.

Sample Input 2 :
2
6
1 2 3 4 5 6
3
3 2 1

Sample Output 2 :
21
3

Constraints:
1 <= T <= 5
1 <= N <= 1000
1 <= RACK[i] <= 10^5

Time Limit: 1 sec

LINK : https://www.naukri.com/code360/problems/1112624?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTabValue=PROBLEM
"""

# Brute Force
"""
    Time complexity     : (n^2)
    Space complexity    : (n)
"""

def maxIncreasingDumbbellsSum(rack, n):
    dp = rack.copy()

    for i in range(1,n):
        for j in range(i):
            if rack[i] > rack[j]:
                dp[i] = max(dp[i], rack[i]+dp[j])
    return max(dp)


# Optimal
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""
class BIT:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, idx, value):
        while idx <= self.size:
            self.tree[idx] = max(self.tree[idx], value)
            idx += idx & -idx
    
    def query(self, idx):
        max_value = 0
        while idx > 0:
            max_value = max(max_value, self.tree[idx])
            idx -= idx & -idx
        return max_value

def maxSumIS(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Coordinate compression
    sorted_arr = sorted(set(arr))
    value_to_index = {val: idx+1 for idx, val in enumerate(sorted_arr)}
    
    # Initialize BIT
    bit = BIT(len(sorted_arr))
    
    max_sum = 0
    
    for val in arr:
        idx = value_to_index[val]
        current_sum = bit.query(idx - 1) + val
        bit.update(idx, current_sum)
        max_sum = max(max_sum, current_sum)
    
    return max_sum
