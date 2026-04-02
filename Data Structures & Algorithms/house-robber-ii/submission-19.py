class Solution:
    def rob(self, nums: List[int]) -> int:
        # State: How much so far
        # Ops: If this one + prev vs curr
        # Catch: if n <= 2: return max of nums
        n = len(nums)
        if n <= 2:
            return max(nums)

        def smart_robber(i, end, dp):
            if i >= end:
                return 0
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(nums[i] + smart_robber(i + 2, end, dp), smart_robber(i + 1, end, dp))
            return dp[i]

        dp = [-1] * n
        start =smart_robber(0, n - 1, dp)
        dp = [-1] * n
        last =  smart_robber(1, n, dp)
        return max(start, last)

