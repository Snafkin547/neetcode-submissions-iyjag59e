class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def bt(i, curr):
            if i == n:
                res.append(curr[::])
                return

            curr.append(nums[i])
            bt(i + 1, curr)
            curr.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            bt(i + 1, curr)
        bt(0, [])
        return res



