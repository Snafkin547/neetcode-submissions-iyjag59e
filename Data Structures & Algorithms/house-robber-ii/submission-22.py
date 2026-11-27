class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        res = 0
        prev, curr = 0, 0
        for n in nums[:-1]:
            temp = max(curr, prev + n)
            prev = curr
            curr = temp
        res = max(res, curr)

        prev, curr = 0, 0
        for n in nums[1:]:
            temp = max(curr, prev + n)
            prev = curr
            curr = temp
        res = max(res, curr)
        return res
