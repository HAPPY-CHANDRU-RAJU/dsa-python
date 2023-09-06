"""
Implement a Queue
"""

#####  Optimal  #####

class Queue :
    def __init__(self):
        self.rear = 0
        self.qfront = 0
        self.size = 0
        self.qsize = 100010
        self.arr = [0]* self.qsize
   
    def isEmpty(self) :
        return self.qfront == self.rear

    def enqueue(self, data) :
        self.arr[self.rear] = data
        self.rear += 1
        self.size += 1 

    def dequeue(self) :
        if self.isEmpty():
            return -1
        
        ans = self.arr[self.qfront]
        self.qfront += 1
        self.size -= 1

        if self.qfront == self.rear:
            self.qfront , self.rear == -1, -1
        
        return ans
        
    def front(self) :
        if self.isEmpty():
            return -1

        return self.arr[self.qfront]
        