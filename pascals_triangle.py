"""
Program to generate Pascal's Triangle

Problem Statement: Given the row number n. Print the n-th row of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown in the figure below:

"""

# Better
class Solution:
    def ncr(self,n,r):
        res = 1
        for i in range(r):
            res *= (n-i)
            res /= (i+1)
        return int(res)
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(self.ncr(i, j))
            res.append(temp)
        return(res)
