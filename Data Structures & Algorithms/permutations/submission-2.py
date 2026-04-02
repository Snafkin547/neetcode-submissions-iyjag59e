class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Use Remainig list and Curr list
        # append if remaining is empty
        res = []
        def dfs(remaining, curr):
            if not remaining:
                res.append(curr.copy())
            
            for i in range(len(remaining)):
                r = remaining[i]
                curr.append(r)
                dfs(remaining[:i] + remaining[i+1:], curr)
                curr.pop()
        dfs(nums, [])
        return res