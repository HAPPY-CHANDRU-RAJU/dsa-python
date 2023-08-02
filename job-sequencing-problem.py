"""
Job Sequencing Problem

Given a set of N jobs where each jobi has a deadline and profit associated with it.
Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.
Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.

Example 1:

Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}

Output:
2 60

Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).

"""

##### Optimal #####

def JobScheduling(self,Jobs,n):
    Jobs.sort(key= lambda x: x.profit, reverse=True)
    max_ = -999
    for i in Jobs:
        if i.deadline > max_:
            max_ = i.deadline

    list_ = [-1]*max_
    profit = 0
    for i in Jobs:
        for j in reversed(range(i.deadline)):
            if j < max_ and list_[j] == -1:
                list_[j] = i.id
                profit += i.profit
                break
        
    return len(list(filter(lambda x: x != -1, list_))),profit
    