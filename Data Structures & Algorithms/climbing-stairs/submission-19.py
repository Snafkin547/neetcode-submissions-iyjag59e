class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n <= 2:
            return n
            
        cache = [0] * (n + 1)
        cache[-1] = cache[-2] = 1
        for i in range(n-2, -1, -1):
            cache[i] = cache[i + 1] + cache[i + 2]

        return cache[0]
        