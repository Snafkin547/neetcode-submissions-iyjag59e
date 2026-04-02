class Solution:
    def climbStairs(self, n: int) -> int:
        # State: i-th step
        # Ops: + 1 or + 2
        if n <= 3:
            return n

        dp = [-1] * n

        def climb_helper(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            # Ops
            dp[i] = climb_helper(i + 1) + climb_helper(i + 2)
            return dp[i]

        return climb_helper(0)