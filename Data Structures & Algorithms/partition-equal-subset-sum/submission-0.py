class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        res = sum(nums)
        if res % 2 != 0:
            return False
        res >>= 1

        def dfs(target1, target2, idx):
            if target1 == 0 or target2 == 0:
                return True
            elif target1 < 0 or target2 < 0:
                return False
            else:
                p1 = dfs(target1 - nums[idx], target2, idx + 1)
                p2 = dfs(target1, target2 - nums[idx], idx + 1)
            return p1 | p2

        return dfs(res, res, 0)