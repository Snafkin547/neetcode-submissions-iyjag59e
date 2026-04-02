class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.mp[key]
        if not vals or vals[0][0] > timestamp:
            return ""
        n = len(vals)
        l, r = 0, n - 1
        
        while l < r:
            m = l + (r - l + 1)//2
            if vals[m][0] > timestamp:
                r = m - 1
            else:
                l = m
        return vals[l][1]