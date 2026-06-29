class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []
    def push_to_back(self, x):
        self.q1.append(x)

    def blast(self):
        return self.q1.pop(0)

    def peek(self):
        return self.q1[0] 

    def size(self):
        return len(self.q1)

    def push(self, x: int) -> None:
        self.push_to_back(x)

    def pop(self) -> int:
        while self.size() > 1:
            self.q2.append(self.blast())
            
        target = self.blast()
        
        self.q1 = self.q2
        self.q2 = []
        
        return target

    def top(self) -> int:
        while self.size() > 1:
            self.q2.append(self.blast())
            
        target = self.blast()
        
        self.q2.append(target)
        
        self.q1 = self.q2
        self.q2 = []
        
        return target

    def empty(self) -> bool:
        return self.size() == 0