class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = len(nums)
        nums.sort()
        prev = 0
        for i in range(n):
            idx = prev if i > 0 and nums[i-1] == nums[i] else 0
            prev = len(res)
            for r in range(idx, prev):
                tmp = res[r].copy()
                tmp.append(nums[i])
                res.append(tmp)
        return res