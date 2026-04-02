class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        idx = prev = 0
        for i in range(len(nums)):
            idx = prev if i >= 1 and nums[i] == nums[i -1] else 0
            prev = len(res)
            # if duplicate, only executes for the new ones with same number so anything that has skipped the number does not apply
            for r in range(idx, prev):
                dummy = res[r].copy()
                dummy.append(nums[i])
                res.append(dummy)
            
        return res