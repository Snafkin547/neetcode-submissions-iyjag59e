class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Build up from None. Add an element at a time
        nums = [1] + nums + [1]
        n = len(nums)
        mp = defaultdict(int)
        # Sub Prob: 
        def dfs(l, r):
            if l > r:
                return 0

            if (l, r) in mp:
                return mp[(l, r)]

            mp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                mp[(l, r)] = max(mp[(l, r)] , coins)
            return mp[(l, r)]
        
        return dfs(1, n - 2)
