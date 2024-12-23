"""
Egg Dropping Puzzle

You are given n identical eggs and you have access to a k-floored building from 1 to k.

There exists a floor f where 0 <= f <= k such that any egg dropped from a floor higher than f will break, and any egg dropped from or below floor f will not break.
There are few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the egg breaks on a certain floor, it will break on any floor above.
Return the minimum number of moves you need to determine the value of f with certainty.

Input: n = 1, k = 2
Output: 2

Explanation: Drop the egg from floor 1. If it breaks, we know that f = 0. Otherwise, drop the egg from floor 2.If it breaks, we know that f = 1.  If it does not break, then we know f = 2. Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Input: n = 10, k = 5
Output: 3

Explanation: Drop the egg from floor 2. If it breaks, test floor 1 with a remaining egg.If it doesn’t break, drop from floor 4. If it breaks, test floor 3. If it still doesn’t break, we know the critical floor is 5.Hence, with a minimum of 3 moves, we can find the critical floor.

Input: n = 2, k = 10
Output: 4

Explanation: Drop the egg from floor 4. If it breaks, we only need to test floors 1 to 3 with the remaining egg.If it doesn't break, drop the egg from floor 7. If it breaks, we only need to test floors 5 and 6. If it doesn't break again, drop the egg from floor 9. If it breaks, test floor 8. If it still doesn’t break, we know the critical floor is 10.Hence, with a minimum of 4 moves, we can determine the critical floor.

Constraints:
1<= n <=100
1<= k <=100

LINK : https://www.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1
"""

# Brute Force
"""
    Time complexity     : (2^k)
    Space complexity    : (k)
"""

class Solution:
    def eggDrop(self,n, k):
        # floor is 0, 1 then return k trials
        if k ==1 or k ==0:
            return k
            
        # only one egg return k trials
        if n == 1:
            return k
        
        min_result = float('inf')
        for x in range(1, k+1):
            # if egg breaks eggDrop(n-1, x-1) try below floors 
            # if egg not breaks eeggDrop(n, k-x) try above floors
            min_result = min(min_result, max(self.eggDrop(n-1, x-1), self.eggDrop(n, k-x)))
        
        return min_result + 1

# Medium Effort
"""
    Time complexity     : (n*k*k)
    Space complexity    : (n*k)
"""

class Solution:
    memo = {}
    def eggDrop(self,n, k):
        
        # floor is 0, 1 then return k trials
        if k ==1 or k ==0:
            return k
            
        # only one egg return k trials
        if n == 1:
            return k
        
        if (n, k) in self.memo:
            return self.memo[(n, k)]
        
        min_result = float('inf')
        for x in range(1, k+1):
            # if egg breaks eggDrop(n-1, x-1) try below floors 
            # if egg not breaks eeggDrop(n, k-x) try above floors
            min_result = min(min_result, max(self.eggDrop(n-1, x-1), self.eggDrop(n, k-x)))
        
        self.memo[(n, k)] = min_result + 1
        return self.memo[(n, k)]


# Optimal
"""
    Time complexity     : (n* (k log k))
    Space complexity    : (n*k)
"""

class Solution:
    memo = {}
    def eggDrop(self,n, k):
        
        # floor is 0, 1 then return k trials
        if k ==1 or k ==0:
            return k
            
        # only one egg return k trials
        if n == 1:
            return k
        
        if (n, k) in self.memo:
            return self.memo[(n, k)]
        
        min_result = float('inf')
        low, high = 1, k
        
        while low <= high:
            mid = (low+high)//2
            
            break_case = self.eggDrop(n-1, mid-1)         # break
            non_break_case = self.eggDrop(n, k-mid)       # non break
            
            worst_case = max(non_break_case, break_case)
            min_result = min(min_result, worst_case+1 )
            
            if break_case > non_break_case:
                high = mid -1
            else:
                low = mid + 1
            
        self.memo[(n, k)] = min_result
        return self.memo[(n, k)]