class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res != (res >> 1)<<1:
            return False
        res >>= 1
        dp = [[False] * (res + 1) for _ in range(len(nums) + 1)] 

        def dfs(target, idx):
            if target == 0 or dp[idx][target]:
                return True
            elif target < 0 or idx == len(nums):
                return False
            else:
                res = dfs(target - nums[idx], idx + 1)|dfs(target, idx + 1)
                dp[idx][target] = res
                return res
        return dfs(res, 0)