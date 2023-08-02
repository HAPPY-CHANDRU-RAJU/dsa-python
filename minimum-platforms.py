"""
Minimum Platforms

Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.


Example 1:

Input: n = 6 
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}

Output: 3

Explanation: 
Minimum 3 platforms are required to 
safely arrive and depart all trains.

"""


#####  Brute Force  #####

def findPlatform(arr, dep, n):
    plat_needed = 1
    result = 1
    for i in range(n):
        plat_needed = 1
        for j in range(n):
            if i != j:
                if (arr[i] >= arr[j] and dep[j] >= arr[i]):
                    plat_needed += 1
        result = max(result, plat_needed)
    return result
 
##### Optimal #####

class Solution:
    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
        i,j = 0,0
        res, platform = 0,0
        while i < n and j < n:
            if arr[i] <=dep[j]:
                platform += 1
                i += 1
            else:
                platform -= 1
                j += 1
            res = max(res, platform)
        return res
        
