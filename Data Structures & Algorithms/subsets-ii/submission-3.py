class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        def bt(idx, curr):
            if idx == n:
                res.append(curr.copy())
                return
            curr.append(nums[idx])
            bt(idx + 1, curr)
            curr.pop()

            while idx + 1 < n and nums[idx] == nums[idx + 1]:
                idx += 1
            bt(idx + 1, curr)
        bt(0, [])
        return res