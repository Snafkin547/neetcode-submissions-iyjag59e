class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [None] * len(nums)
        def dfs(idx):
            if idx >= len(nums) - 1:
                return True
            if memo[idx]:
                return memo[idx]
            if nums[idx] == 0:
                memo[idx] = False
                return False
            end = min(len(nums), idx + nums[idx] + 1)
            for i in range(idx + 1, end):
                if dfs(i):
                    memo[idx] = True
                    return True
            memo[idx] = False
            return False
        return dfs(0)