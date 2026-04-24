class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Maintain stack increasing order
        # If shorter encountered, process tallers
        # Because elm - 1 is its boundary due to its increasing nature, this retrospective approach works 
        # By n + 1, it ensures everything is processed at the end
        n = len(heights)
        stack = []
        res = 0
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)        
        return res