"""
Aggressive Cows


"""

#####  Brute Force  #####

##### Better  #####
def isPos(stalls, gap, k):
    cowCnt, currGap = 1, stalls[0]
    for i in range(1, len(stalls)):
        if  stalls[i] - currGap  >= gap:
            cowCnt += 1
            currGap = stalls[i]
    return cowCnt >= k 


def aggressiveCows(stalls, k):
    low = 1
    high = max(stalls) - min(stalls)
    stalls.sort()
    for gap in range(low, high+1):
        if isPos(stalls, gap, k) == True :
            continue
        else:
            return gap-1
    return gap

##### Optimal #####

def isPos(stalls, gap, k):
    cowCnt, currGap = 1, stalls[0]
    for i in range(1, len(stalls)):
        if  stalls[i] - currGap  >= gap:
            cowCnt += 1
            currGap = stalls[i]
    return cowCnt >= k 


def aggressiveCows(stalls, k):
    n = len(stalls)
    stalls.sort()
    low = 0
    high = stalls[n-1] - stalls[0]
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if isPos(stalls, mid, k) == False :
            high = mid-1
        else:
            low = mid+1
            ans = mid
    return ans
