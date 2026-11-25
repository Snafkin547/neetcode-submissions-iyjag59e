class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        n = len(nums)
        def bt(i):
            if i >= n:
                res.append(curr[::])
                return
            bt(i + 1)
            curr.append(nums[i])
            bt(i + 1)
            curr.pop()

        bt(0)
        return res
            