"""
Flattening a Linked List

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

Note: The flattened list will be printed using the bottom pointer instead of the next pointer.
For more clarity have a look at the printList() function in the driver code.

 

Example 1:

Input:
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30               45

Output:  5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.

Explanation:
The resultant linked lists has every 
node in a single level.
(Note: | represents the bottom pointer.)

"""

##### Optimal #####

'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def mergeTwo(a,b):
    temp = Node(-1)
    res = temp
    
    while a and b:
        if a.data < b.data:
            temp.bottom = a
            a = a.bottom 
            temp = temp.bottom
        else:
            temp.bottom = b
            b = b.bottom
            temp = temp.bottom
            
    if a:
        temp.bottom = a
    else:
        temp.bottom = b
        
    return res.bottom
    

def flatten(root):
    if root is None or root.next is None:
        return root
        
    root.next = flatten(root.next)
    root = mergeTwo(root, root.next)
    return root
        