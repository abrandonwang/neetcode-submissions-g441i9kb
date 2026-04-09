class MinStack:

    def __init__(self):
        self.stack = [] # regular stack 
        self.mini = [] # min stack that keeps the minimum value at that point in the stack 
        return 

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini: # checks for a value in the stack
            val = min(val, self.mini[-1]) # takes the minimum between val and the top of mini
        self.mini.append(val) # appends new min to the top
        return 

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()
        return 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
