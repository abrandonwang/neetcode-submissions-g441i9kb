class MinStack:

    def __init__(self):
        self.stack = []
        self.minst = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        x = val
        if self.minst:
            x = min(val, self.minst[-1])
        self.minst.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minst[-1]
