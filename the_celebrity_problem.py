"""
The Celebrity Problem

Problem statement
There are ‘N’ people at a party. Each person has been assigned a unique id between 0 to 'N' - 1(both inclusive). A celebrity is a person who is known to everyone but does not know anyone at the party.

Given a helper function ‘knows(A, B)’, It will returns "true" if the person having id ‘A’ know the person having id ‘B’ in the party, "false" otherwise. Your task is to find out the celebrity at the party. Print the id of the celebrity, if there is no celebrity at the party then print -1.

Note:
1. The helper function ‘knows’ is already implemented for you.
2. ‘knows(A, B)’ returns "false", if A doesn't know B.
3. You should not implement helper function ‘knows’, or speculate about its implementation.
4. You should minimize the number of calls to function ‘knows(A, B)’.
5. There are at least 2 people at the party.
6. At most one celebrity will exist.

Sample Input 1:
1
2
Call function ‘knows(0, 1)’ // returns false
Call function ‘knows(1, 0)’ // returns true

Sample Output 1:
0

Explanation For Sample Input 1:
In the first test case, there are 2 people at the party. When we call function knows(0,1), it returns false. That means the person having id ‘0’ does not know a person having id ‘1'. Similarly, the person having id ‘1’  knows a person having id ‘0’ as knows(1,0) returns true. Thus a person having id ‘0’ is a celebrity because he is known to everyone at the party but doesn't know anyone.

Sample Input 2:
1
2
Call ‘knows(0, 1)’ // returns true
Call ‘knows(1, 0)’ // returns true
2
Call ‘knows(0, 1)’ // returns false
Call ‘knows(1, 0)’ // returns false

Sample Output 2:
-1
-1

Explanation For Sample Input 2:
In first test case, there are 2 people at the party. The person having id ‘0’  knows a person having id ‘1’. The person having id ‘1’  knows a person having id ‘0’. Thus there is no celebrity at the party, because both know each other. 
In second test case, there are 2 people at the party. The person having id ‘0’ does not knows a person having id ‘1’. The person having id ‘1’  also does not knows a person having id ‘0’. Thus there is no celebrity at the party, because both does not know each other. 

Constraints:
1 <= T <= 50
2 <= N <= 10^4

Where ‘T’ is the total number of test cases, ‘N’ is the number of people at the party.

Time Limit: 1sec

LINK : https://www.naukri.com/code360/problems/the-celebrity-problem_982769
"""


# Medium 
"""
    Time complexity     : (n^2)
    Space complexity    : (1)
"""

def findCelebrity(n, knows):
    celebrity = []
    for j in range(n):
        flag = True
        for i in range(n):
            if i != j:
                if not knows(i, j) or knows(j, i):
                    flag = False
                    break
        if flag:
            celebrity.append(j)
    return celebrity[0] if celebrity else -1

# Optimal
"""
    Time complexity     : (n)
    Space complexity    : (1)
"""

def findCelebrity(n, knows):
    celebrity = 0
    for i in range(n):
        if knows(celebrity, i):
            celebrity = i
    
    for i in range(n):
        if i != celebrity:
            if not knows(i, celebrity) or knows(celebrity, i):
                return -1
    return celebrity