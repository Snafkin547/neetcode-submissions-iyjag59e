class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Pick same n as many times as possible
        # all Positive
        # If 0, append, over target stop
        # every index chose stay or move
        res = []

        def dfs(i, curr, balance):
            # Valid Combination
            if balance == 0:
                res.append(curr[::])
                return

            # No more 
            if i >= len(nums) or balance < 0:
                return

            # move
            dfs(i + 1, curr, balance)

            n = nums[i]
            curr.append(n)
            dfs(i, curr, balance - n)
            curr.pop()
        
        dfs(0, [], target)
        return res
