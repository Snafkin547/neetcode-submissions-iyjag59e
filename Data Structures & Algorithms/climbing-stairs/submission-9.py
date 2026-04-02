class Solution:
    def climbStairs(self, n: int) -> int:
        prev = curr = 1
        for i in range(n - 1):
            t = curr
            curr += prev
            prev = t
        return curr