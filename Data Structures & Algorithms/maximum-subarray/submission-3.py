class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[None] * 2 for _ in range(n)]
        def dfs(idx, flag):
            if idx == n:
                return 0 if flag else -1e6
            if memo[idx][flag]:
                return memo[idx][flag]
            if flag: # Subarray started
                memo[idx][flag] = max(nums[idx] + dfs(idx + 1, flag), 0)
                
            else: # Subarray yet to start
                memo[idx][flag] = max(nums[idx] + dfs(idx + 1, True), dfs(idx + 1, False))
            return memo[idx][flag]
        return dfs(0, False)