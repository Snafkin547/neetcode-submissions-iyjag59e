class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(idx):
            if idx == n:
                res.append(nums[::])
                return
            
            for i in range(idx, n):
                nums[idx], nums[i] = nums[i], nums[idx]
                helper(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]
        helper(0)
        return res