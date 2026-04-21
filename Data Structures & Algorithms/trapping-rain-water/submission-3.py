class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        premax = 0
        for i in range(n):
            prefix[i] = premax
            premax = max(premax, height[i])
            
        suffix = [0] * n
        suffmax = 0
        for i in range(n - 1, -1, -1):
            suffix[i] = suffmax
            suffmax = max(suffmax, height[i])

        res = 0
        for i in range(n):
            res += max(min(suffix[i], prefix[i]) - height[i], 0)
        return res