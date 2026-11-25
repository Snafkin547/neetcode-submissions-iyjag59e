class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # with and without
        res = [[]]
        for n in nums:
            res += [r + [n] for r in res]
        return res
            