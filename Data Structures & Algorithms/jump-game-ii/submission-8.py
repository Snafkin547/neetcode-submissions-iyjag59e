class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        i = 0
        while i < n - 1:
            next_i = i
            end = min(i + nums[i] + 1, n)
            for j in range(i + 1, end):
                if next_i < j + nums[j] or j + nums[j] >= n - 1:
                   next_i = j + nums[j]
                   i = j
            res += 1
        return res