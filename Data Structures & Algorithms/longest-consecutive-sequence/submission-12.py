class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            curr = n
            cnt = 0
            if curr - 1 not in s:
               while curr in s:
                   curr += 1
                   cnt += 1
               res = max(res, cnt)
        return res