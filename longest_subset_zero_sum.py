"""
Longest subset zero sum

Ninja loves playing with numbers. So his friend gives him an array on his birthday. The array consists of positive and negative integers. Now Ninja is interested in finding the length of the longest subarray whose sum is zero.

Constraints:
1 <= T <= 10
1 <= N <= 10^4
-10^5 <= arr[i] <= 10^5

LINK : https://www.naukri.com/code360/problems/longest-subset-zero-sum
"""

# Brute Force
"""
    Time complexity     : (n^3)
    Space complexity    : (1)
"""
def LongestSubsetWithZeroSum(arr):
    n = len(arr)
    max_size = 0
    for i in range(n):
        for j in range(i, n):
            sum_ = sum(arr[i:j+1])
            if sum_ == 0:
                max_size = max(max_size, ((j+1)-i))
    return max_size


# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""

def LongestSubsetWithZeroSum(arr):
    n = len(arr)
    max_size = 0
    for i in range(n):
        sum_ = 0
        for j in range(i, n):
            sum_ += arr[j]
            if sum_ == 0:
                max_size = max(max_size, ((j+1)-i))
    return max_size


# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (n)
"""

def LongestSubsetWithZeroSum(arr):
    sum_index_map = {}

    max_length = 0
    cumulative_sum = 0
    for i, n in enumerate(arr):
        cumulative_sum += arr[i]
        
        if cumulative_sum == 0:
            max_length = i+1
        
        if cumulative_sum in sum_index_map:
            max_length = max(max_length,  i - sum_index_map[cumulative_sum])
        else:
            sum_index_map[cumulative_sum] = i
     
    return max_length