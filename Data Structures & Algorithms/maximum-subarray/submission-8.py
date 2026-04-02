class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return -1e6

            m = l + (r - l)//2
            left = right = curr = 0
            for i in range(m-1, l - 1, -1):
                curr += nums[i]
                left = max(left, curr)
            curr = 0
            for i in range(m + 1, r + 1):
                curr += nums[i]
                right = max(right, curr)
            res = left + right + nums[m]
            return max(res, dfs(l, m -1), dfs(m + 1, r))
        return dfs(0, len(nums) - 1)
