class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not
        n = len(nums)
        dp = [-1] * n

        def findLIS(i):
            if dp[i]!=-1:
                return dp[i]

            LIS = 1
            for k in range(i + 1, n):
                if nums[i] < nums[k]:
                    LIS = max(LIS, 1 + findLIS(k))
            dp[i] = LIS
            return dp[i]
        return max(findLIS(i) for i in range(n))