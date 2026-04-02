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

        curr = nums[0]
        res = dfs(1, curr) + 1
        for idx in range(1, n):
            print(curr, res)
            if curr > nums[idx]:
                res = max(res, dfs(idx + 1, nums[idx]) + 1)
                curr = min(curr, nums[idx])
                print(curr)
        return res