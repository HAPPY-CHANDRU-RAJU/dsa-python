"""
Find Nth Root Of M

"""

#####  Brute Force  #####
def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    for i in range(1, m+1):
        pow_ = i**n
        if pow_ == m:
            return i
        elif pow_ > m:
            return -1
    return -1


##### Better  #####
def NthRoot(n: int, m: int) -> int:
    low, high = 0, m
    while low <= high:
        mid = (low+high)//2
        pow_ = mid**n
        if pow_ == m:
            return mid
        elif pow_ > m:
            high = mid-1
        else:
            low = mid+1
    return -1


##### Optimal #####
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
        

def NthRoot(n: int, m: int) -> int:
    low, high = 0, m
    while low <= high:
        mid = (low+high)//2
        pow_ = myPow(mid,n)
        if pow_ == m:
            return mid
        elif pow_ > m:
            high = mid-1
        else:
            low = mid+1
    return -1





