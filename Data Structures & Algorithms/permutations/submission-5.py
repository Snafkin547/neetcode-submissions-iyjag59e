class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(curr, mask):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for i in range(n):
                if 1 << i & mask:
                    continue
                curr.append(nums[i])
                dfs(curr, mask|1<<i)
                curr.pop()
        dfs([], 0)
        return res