class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(curr, sofar):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if not sofar[i]:
                    curr.append(nums[i])
                    sofar[i] = True
                    dfs(curr, sofar)
                    sofar[i] = False
                    curr.pop()
        visited = [False] * len(nums)
        dfs([], visited)
        return res