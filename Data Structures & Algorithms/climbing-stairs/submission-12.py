class Solution:
    def climbStairs(self, n: int) -> int:
        # State: i-th step
        # Ops: + 1 or + 2
        if n <= 3:
            return n

        prev = curr = 1
        for i in range(2, n + 1):
            temp = prev + curr
            prev, curr = curr, temp
        return curr
