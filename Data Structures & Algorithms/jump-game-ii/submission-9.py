class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        furthest = 0
        curr_end = 0
        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            if i == curr_end:
                res += 1
                curr_end = furthest
                if curr_end >= n - 1:
                    break
        return res