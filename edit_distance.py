"""
Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character 

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3

Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.

LINK : https://leetcode.com/problems/edit-distance/
"""

# Brute Force
"""
    Time complexity     : O(3^(m+n))  # Exponential due to 3 possible operations per character comparison.
    Space complexity    : O(m + n)   # Maximum depth of the recursion stack.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        def compute(i, j):
            if i == m:
                return n-j      # Insert characters from word1
            
            if j == n:
                return m-i      # Delete characters from word2  
            
            if word1[i] == word2[j]:
                return compute(i+1, j+1) 
            
            insert_op = 1 + compute(i, j+1)       # Insert
            delete_op = 1 + compute(i+1, j)       # Delete
            replace_op = 1 + compute(i+1, j+1)    # Replace

            return min(insert_op, delete_op, replace_op)

        return compute(0, 0)

# Medium Effort
"""
    Time complexity     : (m*n)
    Space complexity    : (m*n)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0 for _ in range(n+1)] for i in range(m+1)] 

        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    dp[i][j] = j                     # Insert all charcters of word2
                elif j == 0:
                    dp[i][j] = i                     # Delete all characters of word1
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(
                        dp[i][j-1],                  # Delete
                        dp[i-1][j],                  # Insert
                        dp[i-1][j-1]                 # replace
                    )
        return dp[m][n]

# Optimal
"""
    Time complexity     : (m*n)
    Space complexity    : (n)
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Initialize the previous and current rows
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr[0] = i                              # Delete all characters from word1 up to i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    curr[j] = prev[j - 1]            # Characters match
                else:
                    curr[j] = 1 + min(
                        prev[j],                    # Delete from word1
                        curr[j - 1],                # Insert into word1
                        prev[j - 1]                 # Replace in word1
                    )
            prev, curr = curr, prev                 # Swap the rows

        return prev[n]
