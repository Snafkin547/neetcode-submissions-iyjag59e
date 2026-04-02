class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        agg = sum(nums)
        tgt = agg>>1
        if (tgt)<<1!=agg:
            return False
        dp = [[None]*(len(nums)+1) for _ in range(tgt+1)]

        def dfs(idx, target):
            if target == 0:
                return True
            elif dp[target][idx]:
                return dp[target][idx]
            elif target < 0 or idx == len(nums):
                return False
            else:
                yes = dfs(idx + 1, target - nums[idx]) if target - nums[idx] >= 0 else False
                dp[target][idx] = yes | dfs(idx+1, target)
                return dp[target][idx]

        return dfs(0,tgt)
        