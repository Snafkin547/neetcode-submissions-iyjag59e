class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = [] # index, height
        res = 0
        for i, h in enumerate(heights):
            leftmost = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                res = max(res, height * (i - index))
                leftmost = index
            stack.append((leftmost, h)) # leftmost index this height accepted
        
        for i, h in stack:
            res = max(res, h * (n - i))
        return res