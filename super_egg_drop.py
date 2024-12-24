"""
Super Egg Drop

You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.
You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example 1:

Input: k = 1, n = 2
Output: 2

Explanation: 
Drop the egg from floor 1. If it breaks, we know that f = 0.
Otherwise, drop the egg from floor 2. If it breaks, we know that f = 1.
If it does not break, then we know f = 2.
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Example 2:

Input: k = 2, n = 6
Output: 3

Example 3:

Input: k = 3, n = 14
Output: 4
 

Constraints:

1 <= k <= 100
1 <= n <= 104

LINK : https://leetcode.com/problems/super-egg-drop/description/
"""

# Brute Force
"""
    Time complexity     : (k * n * n)
    Space complexity    : (n * k)
"""
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        if  n == 1 or n == 0 :
            return n

        if k == 1:
            return n

        min_result = float('inf')
        for x in range(1, n+1):
            break_case = self.superEggDrop(k-1, x-1)      # break case 
            non_break_case = self.superEggDrop(k, n-x)    # non break case

            # Maximum Floors
            worst_case = max(non_break_case, break_case)+1
            min_result = min(min_result, worst_case)

        return min_result
 
# Medium Effort
"""
    Time complexity     : (n * k * k)
    Space complexity    : (n * k)
"""
class Solution:
    def __init__(self):
        self.memo = {}
    
    def superEggDrop(self, k: int, n: int) -> int:
        if  n == 1 or n == 0 :
            return n

        if k == 1:
            return n

        if (k,n) in self.memo:
            return self.memo[(k, n)]

        min_result = float('inf')
        for x in range(1, n+1):
            break_case = self.superEggDrop(k-1, x-1)      # break case 
            non_break_case = self.superEggDrop(k, n-x)    # non break case
            worst_case = max(non_break_case, break_case)+1

            min_result = min(min_result, worst_case)

        self.memo[(k,n)] = min_result
        return self.memo[(k,n)]


# Optimal
"""
    Time complexity     : O(k * n * log(n))
    Space complexity    : O(k * n)
"""
class Solution:
    def __init__(self):
        self.memo = {}
    
    def superEggDrop(self, k: int, n: int) -> int:
        if  n == 1 or n == 0 :
            return n

        if k == 1:
            return n

        if (k,n) in self.memo:
            return self.memo[(k, n)]

        min_result = float('inf')
        low, high = 1, n
        while low <= high:
            mid = (low+high)//2

            break_case = self.superEggDrop(k-1, mid-1)
            non_break_case = self.superEggDrop(k, n-mid)

            worst_case = max(non_break_case, break_case)+1

            min_result = min(min_result, worst_case)

            if break_case > non_break_case:
                high = mid - 1
            else:
                low = mid + 1

        self.memo[(k,n)] = min_result
        return self.memo[(k,n)]

# Optimal - Mathematical solution
"""
    Time complexity     : O(k * log(n))
    Space complexity    : O(k)
"""
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        """
            Calculates the minimum number of moves required to determine the critical floor
            in a building with 'n' floors and 'k' eggs, using an optimized approach.

            The function uses a dynamic programming approach where the number of floors
            that can be tested is tracked for each number of eggs and moves. The goal is
            to find the minimum number of moves required such that the maximum testable 
            floors with 'k' eggs is at least 'n'.

            Args:
            k (int): Number of eggs available.
            n (int): Number of floors in the building.

            Returns:
            int: Minimum number of moves required to determine the critical floor.

            Explanation:
            - 'floor[i]' represents the maximum number of floors that can be tested with 'i' eggs
            and the current number of moves.
            - Initialize 'floor' to represent testing 0 floors with 0 eggs and 1 floor with each egg
            in the first move.
            - Incrementally calculate the maximum number of floors that can be tested as more moves
            are made:
                - If the egg does not break, add the floors testable with the same number of eggs.
                - If the egg breaks, add the floors testable with one less egg.
                - Add 1 for the current floor being tested.
            - Continue this process until the maximum testable floors with 'k' eggs is at least 'n'.

            Example:
            Input: k = 2, n = 6
            Output: 3
            Explanation:
                - With 2 eggs and 3 moves:
                    - First drop from floor 2. If it breaks, test floor 1. If it doesn't, test floors 3-6.
                    - This guarantees determining the critical floor within 3 moves.

            Time Complexity:
            O(k * log(n)) - Iterates for moves and updates for each egg.

            Space Complexity:
            O(k) - Uses a single list to track floors testable for each egg.
        """
        floor = [0] + [1]*k
        move = 1
        while floor[-1] < n:
            move += 1
            for i in range(k, 0, -1):
                floor[i] = floor[i]+floor[i-1]+1
        return move

