class Solution:
    def rob(self, nums: List[int]) -> int:
        # State: How much so far
        # Ops: If this one + prev vs curr
        # Catch: if n <= 2: return max of nums
        n = len(nums)
        if n <= 2:
            return max(nums)

        def smart_robber(start, end):
            dp = [0] * (end - start)
            dp[0] = nums[start]
            dp[1] = max(nums[start], nums[start + 1])
            for i in range(start + 2, end):
                dp[i - start] = max(dp[i - start - 1], dp[i - start - 2] + nums[i])
            return dp[-1]

        return max(smart_robber(0, n - 1), smart_robber(1, n))

