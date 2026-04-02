class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Make a binary decision
        # Memoization
        n = len(nums)
        def dfs(idx, curr):
            if idx == n:
                return 0
            # With
            this = None
            if not curr or (curr and curr < nums[idx]):
                this = dfs(idx + 1, nums[idx]) + 1
            
            # Without
            noThis = dfs(idx + 1, curr)
            return max(this, noThis) if this else noThis
        return dfs(0, None)