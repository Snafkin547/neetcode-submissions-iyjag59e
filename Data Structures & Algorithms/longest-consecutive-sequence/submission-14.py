class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        mp = defaultdict(int)
        for n in nums:
            if not mp[n]:
                mp[n] = 1 + mp[n - 1] + mp[n + 1]
                mp[n - mp[n - 1]] = mp[n]
                mp[n + mp[n + 1]] = mp[n]
                res = max(res, mp[n])
        return res