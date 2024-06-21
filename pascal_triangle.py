"""
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 

Constraints:
1 <= numRows <= 30

LINK : https://leetcode.com/problems/pascals-triangle/description/
"""

# Brute Force
"""
    Time complexity     : (n^2) 
    Space complexity    : (n^2) 
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            temp = []
            for j in range(0, i+1):
                val = 1
                if j != 0 and j != i:
                    val = result[-1][j-1] + result[-1][j]
                temp.append(val)
            result.append(temp)
        return result
                    
# Using Pascal Formula
"""
    Time complexity     : (n^2) 
    Space complexity    : (n^2) 
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append((temp[-1]* (i-j+1)) // j) # ( ( arr[-1] * (i-j+1)) // j )
            yield temp
        