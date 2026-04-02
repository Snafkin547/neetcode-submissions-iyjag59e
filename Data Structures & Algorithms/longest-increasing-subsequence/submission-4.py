class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Make a binary decision
        # Memoization
        n = len(nums)
        dp = {}
        def dfs(idx, curr):
            if idx == n:
                return 0
                
            s = (idx, curr)
            if s in dp:
                return dp[(idx, curr)]

            LIS = dfs(idx + 1, curr)
            if not curr or (curr and curr < nums[idx]):
                LIS = max(dfs(idx + 1, nums[idx]) + 1, LIS)
            return LIS

        curr = nums[0]
        res = dfs(1, curr) + 1
        for idx in range(1, n):
            if curr > nums[idx]:
                res = max(res, dfs(idx + 1, nums[idx]) + 1)
                curr = min(curr, nums[idx])
        return res