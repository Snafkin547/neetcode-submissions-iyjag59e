class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, curr):
            res.append(curr.copy())
            for j in range(idx, len(nums)):
                if j > idx and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j])
                dfs(j + 1, curr)
                curr.pop()
        dfs(0, [])
        return res