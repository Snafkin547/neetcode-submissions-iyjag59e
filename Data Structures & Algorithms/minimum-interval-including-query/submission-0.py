class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Build a data structure, mp, that records the smallest interval
        # if intervals[i] = [2, 3] of length 2(3-2+1), mp[2] = 2, mp[3] = 2
        mp = {}
        for l, r in intervals:
            length = r - l + 1
            for i in range(l, r + 1):
                mp[i] = mp.get(i, float('inf'))
                mp[i] = min(mp[i], length)

        res = [-1] * len(queries)
        for i, val in enumerate(queries):
            if val in mp:
                res[i] = mp[val]
        return res