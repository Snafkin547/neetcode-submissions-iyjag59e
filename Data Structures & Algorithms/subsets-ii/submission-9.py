class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        def bt(i, subset):
            res.append(subset[::])
            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                subset.append(nums[j])
                bt(j + 1, subset)
                subset.pop()
            
        bt(0, [])
        return res