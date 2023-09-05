"""
Stack Implementation Using Array
"""

##### Optimal #####

class Stack:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0]* capacity
        self.stackSize = -1

    def push(self, num: int) -> None:
        if self.stackSize != self.capacity-1:
            self.stackSize += 1
            self.arr[self.stackSize] = num

    def pop(self) -> int:
        if self.stackSize != -1:
            self.stackSize -= 1
            return self.arr[self.stackSize+1]
        return -1
    
    def top(self) -> int:
        if self.stackSize != -1:
            return self.arr[self.stackSize]
        return -1
    
    def isEmpty(self) -> int:
        if self.stackSize == -1:
            return 1
        return 0
        
    
    def isFull(self) -> int:
        if self.stackSize == self.capacity -1 :
            return 1
        return 0
