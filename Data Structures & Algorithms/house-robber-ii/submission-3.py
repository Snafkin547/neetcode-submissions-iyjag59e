class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        prev, curr = nums[0], max(nums[0:2])
        for i in range(2,n - 1):
            temp = curr
            curr = max(curr, prev + nums[i])
            prev = temp
        res = curr

        prev, curr = nums[1], max(nums[1:3])
        for i in range(3, n):
            temp = curr
            curr = max(curr, prev + nums[i])
            prev = temp
        return max(res, curr)
