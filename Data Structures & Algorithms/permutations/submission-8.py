class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(subset, visited):
            if len(subset) == n:
                res.append(subset[::])
                return
            
            for i in range(n):
                if 1 << i & visited:
                    continue
                subset.append(nums[i])
                visited |= 1 << i
                helper(subset, visited)
                subset.pop()
                visited ^= 1 << i
        helper([], 0)
        return res
            