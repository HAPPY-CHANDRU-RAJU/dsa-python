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

# Optimal 2
class Solution:
    def myPow(x,n):
        ans = 1
        while n > 0:
            if n%2 == 1:
                ans = ans *x
                n -= 1
            else:
                x = x*x
                n = n//2
        return ans