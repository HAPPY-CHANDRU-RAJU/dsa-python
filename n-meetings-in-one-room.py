"""
N meetings in one room

There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

"""

##### Optimal #####

class Solution:
    def maximumMeetings(self,n,start,end):
        list_ = []
        pos = 1
        cnt = 0
        for i, j in zip(start, end):
            list_.append([i,j,pos])
            pos += 1
        
        list_.sort(key = lambda x : x[1])
        
        maxTime = -9999
        for i in list_:
            if maxTime < i[0]:
                maxTime = i[1]
                cnt += 1
        return cnt
        