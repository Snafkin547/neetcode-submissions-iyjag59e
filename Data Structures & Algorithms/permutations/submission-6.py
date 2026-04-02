class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(idx, nums):
            if idx == n:
                res.append(nums[:])
                return
            st = idx
            for i in range(idx, n):
                nums[st], nums[i] = nums[i], nums[st]
                dfs(idx + 1, nums)
                nums[st], nums[i] = nums[i], nums[st]
        dfs(0, nums)
        return res