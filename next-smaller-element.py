"""
Next Smaller Element

https://www.codingninjas.com/studio/problems/1112581?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
"""

#####  Brute Force  #####

def nextSmallerElement(arr,n):
    nse = [-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                nse[i] = arr[j]
                break
    return nse
    
##### Optimal #####

def nextSmallerElement(arr,n):
    nse = [-1] * n
    stk = []
    stk.append(-1)
    for i in range(n-1, -1, -1):
        while(stk[-1] >= arr[i]):
            stk.pop()
        nse[i] = stk[-1]
        stk.append(arr[i])
    return nse