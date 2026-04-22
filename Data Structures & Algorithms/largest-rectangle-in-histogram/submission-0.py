class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brute Force: l and r keep minimum x r - l + 1

        n = len(heights)
        res = 0
        for l in range(n):
            minH = heights[l]
            for r in range(l, n):
                minH = min(minH, heights[r])
                res = max(res, minH * (r - l + 1))
        return res
