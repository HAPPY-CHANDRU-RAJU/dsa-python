"""
Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
 
Constraints:
0 <= rowIndex <= 33
 
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

LINK : https://leetcode.com/problems/pascals-triangle-ii/description/
"""

# Optimal
"""
    Time complexity     : (rowIndex)
    Space complexity    : (rowIndex)
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex+1
        temp = []
        for i in range(n):
            if i == 0 or i == n:
                temp.append(1)
            else:
                temp.append((temp[-1]*(rowIndex-i+1) // i))
        return temp