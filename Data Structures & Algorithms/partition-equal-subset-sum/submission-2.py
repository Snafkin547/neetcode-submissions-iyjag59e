class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res % 2 != 0:
            return False
        res >>= 1
        dp = [[False] * (res + 1) for _ in range(len(nums))] 

        def dfs(target, idx):
            if target == 0:
                return True
            elif target < 0 or idx == len(nums):
                return False
            else:
                have = dfs(target - nums[idx], idx + 1)
                havenot = dfs(target, idx + 1)
            dp[idx][target] = have | havenot
            return dp[idx][target]

        return dfs(res, 0)