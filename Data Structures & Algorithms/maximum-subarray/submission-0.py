class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cnt = 0
        for n in nums:
            cnt += n
            res = max(res, cnt)
            cnt = max(0, cnt)
        return res