"""
Rat In A Maze

You are given a starting position for a rat which is stuck in a maze at an initial point (0, 0) (the maze can be thought of as a 2-dimensional plane). 
The maze would be given in the form of a square matrix of order 'N' * 'N' where the cells with value 0 represent the maze’s blocked locations while value 1 is the open/available path that the rat can take to reach its destination. 
The rat's destination is at ('N' - 1, 'N' - 1). Your task is to find all the possible paths that the rat can take to reach from source to destination in the maze. 
The possible directions that it can take to move in the maze are 'U'(up) i.e. (x, y - 1) , 'D'(down) i.e. (x, y + 1) , 'L' (left) i.e. (x - 1, y), 'R' (right) i.e. (x + 1, y).

Note:
Here, sorted paths mean that the expected output should be in alphabetical order.

For Example:

Given a square matrix of size 4*4 (i.e. here 'N' = 4):
1 0 0 0
1 1 0 0
1 1 0 0
0 1 1 1 

Expected Output:
DDRDRR DRDDRR 

i.e. Path-1: DDRDRR and Path-2: DRDDRR

The rat can reach the destination at (3, 3) from (0, 0) by two paths, i.e. DRDDRR and DDRDRR when printed in sorted order, we get DDRDRR DRDDRR.
Detailed explanation ( Input/output format, Notes, Images )

Constraints:
2 <= N <= 5
0 <= MATRIX[i][j] <= 1

Where N is the size of the square matrix.

Sample Input 1:
4
1 0 0 0 
1 1 0 1
1 1 0 0
0 1 1 1

Sample Output 1:
DDRDRR DRDDRR

Explanation For Sample Input 1:
The rat can reach the destination at (3, 3) from (0, 0) by two paths, i.e. DRDDRR and DDRDRR when printed in sorted order, we get DDRDRR DRDDRR.

Sample Input 2:
2
1 0
1 0

Sample Output 2:
[]

Explanation For Sample Input 2:
As no valid path exists in Sample input 2 so we return an empty list.

LINK 1 : https://www.naukri.com/code360/problems/rat-in-a-maze
LINK 2 : https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/ 
"""


# Optimal
"""
    Time complexity     : 
    Space complexity    : 
"""

from os import *
from sys import *
from collections import *
from math import *

def isSafe(x, y, n, visited, arr):
    return (0 <= x < n) and  (0 <= y < n) and (arr[x][y] == 1) and (not visited[x][y])

def solver(x, y, n, arr, path, visited, ans):
    if x == n-1 and y == n-1 and arr[x][y] == 1:
        ans.append(path)
        return 
    
    direction = ['D', 'L', 'R', 'U']
    dx = [1, 0, 0, -1]    
    dy = [0, -1, 1, 0]

    for i in range(4):
        new_x = x + dx[i]       
        new_y = y + dy[i]

        if isSafe(new_x, new_y, n, visited, arr):
            visited[new_x][new_y] = True
            solver(new_x, new_y, n, arr, path+direction[i], visited, ans)
            visited[new_x][new_y] = False

def searchMaze(arr, n):
    ans = []
    visited = [[False]*n for _ in range(n)]

    if arr[0][0] == 1:
        visited[0][0] = True
        solver(0, 0, n, arr, '', visited, ans)

    return ans