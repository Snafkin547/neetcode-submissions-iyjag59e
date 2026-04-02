class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # State: i, balance
        # Ops: repeate or move
        n = len(nums)
        res = []

        def helper(i, balance, progress):
            if balance == 0:
                res.append(progress[::])
                return 
            if i == n or balance < 0:
                return
            
            # Use this value
            progress.append(nums[i])
            helper(i, balance - nums[i], progress)
            progress.pop()

            # Skip this value
            helper(i + 1, balance, progress)
            return
        helper(0, target, [])
        return res


