class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.mp[key]
        n = len(vals)
        l, r = 0, n - 1
        res = ""
        while l <= r:
            m = l + (r - l)//2
            if vals[m][0] <= timestamp:
                l = m + 1
                res = vals[m][1]
            else:
                r = m - 1
        return res