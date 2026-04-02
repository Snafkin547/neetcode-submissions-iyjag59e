class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        agg = sum(nums)
        tgt = agg>>1
        if (tgt)<<1!=agg:
            return False
        dp = [[False]*(len(nums)+1) for _ in range(tgt+1)]

        def dfs(idx, target):
            if target == 0 or dp[target][idx]:
                return True
            elif target < 0 or idx == len(nums):
                return False
            else:
                dp[target][idx] = dfs(idx+1, target-nums[idx]) | dfs(idx+1, target)
                return dp[target][idx]

        return dfs(0,tgt)
        