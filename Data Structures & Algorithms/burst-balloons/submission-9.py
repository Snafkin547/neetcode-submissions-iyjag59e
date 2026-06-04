class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        mp = defaultdict(int)
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in mp:
                return mp[(l, r)]
            
            for i in range(l, r + 1):
                
                mult = nums[l - 1] * nums[i] * nums[r + 1]
                left = dfs(l, i - 1)
                right = dfs(i + 1, r)
                mp[(l, r)] = max(mp[(l, r)], mult + left + right)
                
            return mp[(l, r)]
        return dfs(1, len(nums)-2)
