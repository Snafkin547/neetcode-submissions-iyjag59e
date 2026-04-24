class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # You wanna know width : How far can this height apply left/right

        n = len(heights)
        res = 0
        stack = []
        lefty = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack: # Else 0
                lefty[i] = stack[-1]
            stack.append(i)
        
        stack = []
        righty = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack: # Else 0
                righty[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            lefty[i] += 1 
            righty[i] -= 1
            res = max(res, (righty[i] - lefty[i] + 1) * heights[i])
        return res
                        
