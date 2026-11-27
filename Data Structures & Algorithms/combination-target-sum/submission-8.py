class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Pick same n as many times as possible
        # all Positive
        # If 0, append, over target stop
        # every index chose stay or move
        res = []
        nums.sort()

        def dfs(i, curr, balance):
            # Valid Combination
            if balance == 0:
                res.append(curr[::])
                return

            for j in range(i, len(nums)):
                if balance - nums[j] < 0:
                    return
                n = nums[j]
                curr.append(n)
                dfs(j, curr, balance - n)
                curr.pop()
        
        dfs(0, [], target)
        return res
