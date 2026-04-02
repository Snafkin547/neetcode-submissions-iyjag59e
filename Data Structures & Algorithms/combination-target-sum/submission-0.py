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
                dfs(idx + 1, curList[:], curSum) # Without curNum
                while curSum < target:
                    curSum += nums[idx]
                    curList.append(nums[idx])
                    dfs(idx + 1, curList[:], curSum)

        dfs(0, [], 0)
        return res