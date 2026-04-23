class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # You wanna know width : How far can this height apply left/right

        n = len(heights)
        res = 0
        for i in range(n):
            height = heights[i]
            
            right = i + 1
            while right < n and heights[right] >= height:
                right += 1
            
            left = i
            while left >= 0 and heights[left] >= height:
                left -= 1

            right -= 1
            left += 1
            res = max(res, (right - left + 1) * height)
        return res
                        
