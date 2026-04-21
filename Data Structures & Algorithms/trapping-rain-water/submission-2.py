class Solution:
    def trap(self, height: List[int]) -> int:
        # Two pointers
        n = len(height)
        res = 0
        for i in range(n):
            left = right = height[i]
            for j in range(i):
                left = max(left, height[j])

            for j in range(i+1, n):
                right = max(right, height[j])
            res += min(left, right) - height[i]
        return res