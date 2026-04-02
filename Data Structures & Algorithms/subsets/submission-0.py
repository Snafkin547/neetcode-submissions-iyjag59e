class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            new_subsets = [r + [n] for r in res]
            res.extend(new_subsets)
        return res