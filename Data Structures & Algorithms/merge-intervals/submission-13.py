class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for s, e in intervals:
            mp[s] += 1
            mp[e] -= 1
        
        interval = []
        res = []
        have = 0

        for i in sorted(mp):
            if not interval:
                interval.append(i)
            have += mp[i]
            if not have:
                interval.append(i)
                res.append(interval)
                interval = []
        return res

        