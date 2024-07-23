"""
N meetings in one room

There is one meeting room in a firm. There are n meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? Return the maximum number of meetings that can be held in the meeting room.

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Examples :
Input: n = 6, start[] = {1,3,0,5,8,5}, end[] =  {2,4,6,7,9,9}
Output: 4

Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

Input: n = 3, start[] = {10, 12, 20}, end[] = {20, 25, 30}
Output: 1
Explanation: Only one meetings can be held with given start and end timings.

Expected Time Complexity : O(n*Logn)
Expected Auxilliary Space : O(n)

Constraints:
1 ≤ n ≤ 105
0 ≤ start[i] < end[i] ≤ 105

LINK : https://www.geeksforgeeks.org/problems/n-meetings-in-one-room/
"""

# Brute Force
"""
    Time complexity     : (2^n ⋅ n^2 )
    Space complexity    : (2^n)
"""
from itertools import combinations

def is_non_overlapping(meetings):
    for i in range(len(meetings)):
        for j in range(i + 1, len(meetings)):
            if not (meetings[i][1] <= meetings[j][0] or meetings[j][1] <= meetings[i][0]):
                return False
    return True

def maximumMeetings(start: List[int], end: List[int]) -> int:
    meetings = list(zip(start, end))
    max_count = 0

    for r in range(1, len(meetings) + 1):
        for subset in combinations(meetings, r):    # Combination of meetings 
            if is_non_overlapping(subset):          # if no overlapping then its single room
                max_count = max(max_count, len(subset))
    return max_count



# Optimal
"""
    Time complexity     : (n log n)
    Space complexity    : (n)
"""

######## Steps of the Greedy Approach
"""
1. Sort Meetings by End Time:
    First, sort all the meetings by their end times. This way, you always consider meetings that finish earlier, leaving more room for subsequent meetings.

2. Iterate and Select Meetings:
    Initialize a variable to keep track of the end time of the last selected meeting.
    Iterate through the sorted meetings and select a meeting if its start time is greater than or equal to the end time of the last selected meeting.
"""

def maximumMeetings(start: List[int], end: List[int]) -> int:
    n = len(start)

    paired_list = []
    for indx in range(n):
        paired_list.append([start[indx], end[indx], indx])

    paired_list.sort(key=lambda x: x[1])
    
    curr = paired_list[0]
    count = 1
    for paired in paired_list[1:]:
        if curr[1] < paired[0]:
            count += 1
            curr = paired

    return count 