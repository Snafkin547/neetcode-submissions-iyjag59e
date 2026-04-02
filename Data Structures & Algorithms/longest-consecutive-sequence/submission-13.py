class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        res = 0

        for n in nums:
            mp[n] = True
        
        for n in mp.keys():
            if not mp[n]:
                continue

            val = n
            while val - 1 in mp:
                val -= 1
            
            count = 0
            while val in mp:
                mp[val] = False
                val += 1
                count += 1
            res = max(res, count)
        return res