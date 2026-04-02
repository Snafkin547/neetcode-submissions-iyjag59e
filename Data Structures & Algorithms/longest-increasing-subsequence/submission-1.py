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

            # With
            this = None
            if not curr or (curr and curr < nums[idx]):
                this = dfs(idx + 1, nums[idx]) + 1
            
            # Without
            noThis = dfs(idx + 1, curr)
            res = max(this, noThis) if this else noThis
            dp[(idx, curr)] = res
            return res
        return dfs(0, None)