class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res =[[]]
        for n in nums:
            copy = res.copy()
            for r in copy:
                c = r.copy()
                c.append(n)
                res.append(c)
        return res