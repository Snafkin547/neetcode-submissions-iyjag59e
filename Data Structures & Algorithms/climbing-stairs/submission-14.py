class Solution:
    def climbStairs(self, n: int) -> int:
        dp = defaultdict(int)
        def dfs(k):
            if k < 0:
                return 0
            if k == 0:
                return 1
            if dp[k]:
                return dp[k]
            
            res = dfs(k -1) + dfs(k -2)
            dp[k] = res
            return res
        return dfs(n)
            
        