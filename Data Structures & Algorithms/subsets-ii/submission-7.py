class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        def bt(i, subset):
            if i == n:
                res.append(subset[::])
                return
            
            subset.append(nums[i])
            bt(i + 1, subset)
            subset.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            bt(i + 1, subset)
            return
        bt(0, [])
        return res