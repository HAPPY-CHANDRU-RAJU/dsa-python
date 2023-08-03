"""
Activity Selection

Given N activities with their start and finish day given in array start[ ] and end[ ]. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a given day.
Note : Duration of the activity includes both starting and ending day.

Example :

Input:
N = 2
start[] = {2, 1}
end[] = {2, 2}

Output: 1

Explanation: A person can perform only one of the given activities.
"""

##### Optimal #####
def activitySelection(self,n,start,end):
    schedules = []
    for i in range(n):
        schedules.append([start[i], end[i], i+1])
    
    schedules.sort(key = lambda x : x[1])
    
    max_ = -sys.maxsize
    cnt = 0
    
    for schedule in schedules:
        if max_ < schedule[0]:
            max_ = schedule[1]
            i += 1
            cnt += 1
    return cnt
    # code here
