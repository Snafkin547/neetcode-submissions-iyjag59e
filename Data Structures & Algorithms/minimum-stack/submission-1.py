# Maintain two arrays/stacks
# One for all nodes
# Another for maintaining a minimum at a time
# For the minStack/arr:
#   Push if smaller or equal to the current minimum
#   Pop if equal to the value to be popped from the main

class MinStack:

    def __init__(self):
        self.minS = []
        self.allS = []

    def push(self, val: int) -> None:
        if not self.minS or self.minS[-1] >= val:
            self.minS.append(val)
        self.allS.append(val)

    def pop(self) -> None:
        if not self.allS:
            return 

        curr = self.allS.pop()
        if self.minS[-1] == curr:
            self.minS.pop()

    def top(self) -> int:
        return self.allS[-1] if self.allS else None

    def getMin(self) -> int:
        return self.minS[-1] if self.minS else None        
