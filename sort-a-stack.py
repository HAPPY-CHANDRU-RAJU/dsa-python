"""
Sort a Stack

https://www.codingninjas.com/studio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
"""

#####  Brute Force  #####
from os import *
from sys import *
from collections import *
from math import *

def sortStackInsert(stack, element):
    if len(stack) == 0 or element > stack[-1]:
        stack.append(element)
        return 
    else:
        temp = stack.pop()
        sortStackInsert(stack, element)
        stack.append(temp)

def sortStack(stack):
    if len(stack) != 0:
        s = stack.pop()
        sortStack(stack)
        sortStackInsert(stack, s)


##### Optimal #####

