class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res =[0] * n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                prev_idx, _ = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((i, t))
        
        return res
