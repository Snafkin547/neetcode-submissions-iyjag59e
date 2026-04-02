class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # State: i, balance
        # Ops: repeate or move
        n = len(nums)
        res = []
        nums.sort()

        def helper(i, balance, progress):
            if balance == 0:
                res.append(progress[::])
                return 

            for j in range(i, n):
                if nums[j] > balance:
                    return
                progress.append(nums[j])
                helper(j, balance - nums[j], progress)
                progress.pop()
            return
        helper(0, target, [])
        return res


