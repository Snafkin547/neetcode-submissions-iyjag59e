class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # State index, prev
        # Ops, include this or not
        n = len(nums)
        dp = defaultdict(int)

        def findLIS(i, prev):
            if i >= n:
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            
            if nums[i] <= prev:
                dp[(i, prev)] = findLIS(i + 1, prev)
            else:
                dp[(i, prev)] = max(1 + findLIS(i + 1, nums[i]), findLIS(i + 1, prev))
            return dp[(i, prev)]
        return findLIS(0, float('-inf'))