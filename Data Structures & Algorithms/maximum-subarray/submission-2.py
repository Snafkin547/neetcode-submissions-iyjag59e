class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[None] * 2 for _ in range(n)]
        def dfs(idx, flag):
            if idx == n:
                return 0 if flag else -1e6
            if flag: # Subarray started
                memo[idx][flag] = max(nums[idx] + dfs(idx + 1, flag), nums[idx])
                
            else: # Subarray yet to start
                memo[idx][flag] = max(nums[idx] + dfs(idx + 1, True), dfs(idx + 1, False))
            return memo[idx][flag]
        return max(dfs(0, True),dfs(0, False))