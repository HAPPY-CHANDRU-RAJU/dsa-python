"""
Pow(x,n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

#Better
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

# Optimal
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = -n
        
        res = self.myPow(x, n//2)
        if n%2 == 0:
            return res* res
        else:
            return x* res*res
