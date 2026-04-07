class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(subset, visited):
            if len(visited) == len(nums):
                res.append(subset[::])
                return
            
            for val in nums:
                if val in visited:
                    continue
                subset.append(val)
                visited.add(val)
                helper(subset, visited)
                subset.pop()
                visited.discard(val)
        helper([], set())
        return res
            