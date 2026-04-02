#DP Bottom Up/Top down
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def dfs(idx):
            if idx >= n - 1:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            res = 1e6
            for i in range(1, nums[idx] + 1):
                res = min(res, 1 + dfs(idx + i))
            dp[idx] = res
            return res
        return dfs(0)

        