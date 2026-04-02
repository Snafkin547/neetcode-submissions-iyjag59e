class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res =[]
        nums.sort()
        def dfs(idx, curList, curSum):
            
            if curSum == target:
                res.append(curList[:])
                return

            for j in range(idx, len(nums)):
                if curSum + nums[j] > target:
                    return
                curList.append(nums[j])
                dfs(j, curList, curSum + nums[j])
                curList.pop()

        dfs(0, [], 0)
        return res