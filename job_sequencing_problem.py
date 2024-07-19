"""
Job Sequencing Problem

Problem statement
You are given a 'Nx3' 2-D array 'Jobs' describing 'N' jobs where 'Jobs[i][0]' denotes the id of 'i-th' job, 'Jobs[i][1]' denotes the deadline of 'i-th' job, and 'Jobs[i][2]' denotes the profit associated with 'i-th job'.
You will make a particular profit if you complete the job within the deadline associated with it. Each job takes 1 unit of time to be completed, and you can schedule only one job at a particular time.
Return the number of jobs to be done to get maximum profit.

Note :
If a particular job has a deadline 'x', it means that it needs to be completed at any time before 'x'.
Assume that the start time is 0.

For Example :
'N' = 3, Jobs = [[1, 1, 30], [2, 3, 40], [3, 2, 10]].

All the jobs have different deadlines. So we can complete all the jobs.

At time 0-1, Job 1 will complete.
At time 1-2, Job 3 will complete.
At time 2-3, Job 2 will complete.

So our answer is [3 80].

LINK : https://www.naukri.com/code360/problems/job-sequencing-problem
"""

# Optimal
"""
    Time complexity     :  (nlogn+n⋅d) - Sorting the jobs takes  O(nlogn). For each job, finding a free slot takes O(d) in the worst case where  d is the maximum deadline.
    Space complexity    :  (d) - time slot
"""

"""
Explanation
1. Sorting: The jobs are sorted in decreasing order of profit to prioritize jobs with higher profits.
2. Finding Maximum Deadline: Determine the maximum deadline to allocate the appropriate number of time slots.
3. Time Slots Initialization: Initialize an array of time slots with -1 indicating they are free.
4. Scheduling Jobs: For each job, starting from its latest possible time slot, check if the slot is free. If it is, assign the job to that slot, increment the profit and the job count, and move to the next job.
5. Return: Finally, return the count of jobs that can be scheduled and the maximum profit.
"""
def jobScheduling(jobs):
    jobs.sort(key=lambda x: x[-1], reverse=True)
    
    n = 0
    for job in jobs:
        n = max(n, job[1])
    
    time_slots = [False]*(n)

    max_profit = 0
    count = 0
    for job in jobs:
        job_id, deadline, profit = job
        
        for slot in range(min(deadline, n) - 1, -1, -1):
            if time_slots[slot] == -1:
                time_slots[slot] = job_id
                max_profit += profit
                count += 1
                break

    return count, max_profit