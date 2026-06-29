class MyCircularQueue:

    def __init__(self, k: int):
        self.l = k
        self.queue = [-1] * k 
        self.last = 0   
        self.first = 0  
        

        self.count = 0  

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.last] = value
        
        self.last = (self.last + 1) % self.l
        self.count += 1
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
            
        self.queue[self.first] = -1

        self.first = (self.first + 1) % self.l
        self.count -= 1
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.first]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.last - 1) % self.l]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.l