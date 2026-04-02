class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res =[]
        def dfs(idx, curList, curSum):
            
            if curSum == target:
                res.append(curList[:])
                return

            elif idx > len(nums) - 1 or curSum > target:
                return

            else:
                curList.append(nums[idx])
                dfs(idx, curList, curSum + nums[idx])
                curList.pop()
                dfs(idx+ 1, curList, curSum)

        dfs(0, [], 0)
        return res