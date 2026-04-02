class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, curr):
            if idx == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[idx])
            dfs(idx + 1, curr)
            curr.pop()
            i = idx + 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
            dfs(i, curr)
        dfs(0, [])
        return res