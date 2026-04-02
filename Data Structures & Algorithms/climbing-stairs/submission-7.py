class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        def dfs(balance):
            if balance >= n:
                return balance == n
            if cache[balance] != -1:
                return cache[balance]
            cache[balance] = dfs(balance + 1) + dfs(balance + 2)
            return cache[balance]
        return dfs(0)