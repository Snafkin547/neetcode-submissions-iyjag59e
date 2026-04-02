class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i, temp, balance):
            if balance == 0:
                res.append(temp.copy())
                return
            
            if i >= len(nums) or balance < 0:
                return
            
            k = 0
            for j in range(i, len(nums)):
                if balance - nums[j] < 0:
                    break
                temp.append(nums[j])
                dfs(j, temp, balance - nums[j])
                temp.pop()
        dfs(0, [], target)
        return res