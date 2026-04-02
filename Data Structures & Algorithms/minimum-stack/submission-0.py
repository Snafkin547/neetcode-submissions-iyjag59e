class MinStack:

    def __init__(self):
        self.stack = []
        self.minTracker = []

    def push(self, val: int) -> None:
        if not self.minTracker:
            self.minTracker.append(val)
        else:
            self.minTracker.append(min(val, self.minTracker[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.minTracker.pop()
            self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.minTracker[-1]    
