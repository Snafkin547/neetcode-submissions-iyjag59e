class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.mp[key] or timestamp < self.mp[key][0][0]:
            return ""

        arr = self.mp[key]
        l, r = 0, len(arr)
        while l < r:
            m = l + (r - l)//2
            # if timestamp is on its right
            if arr[m][0] > timestamp:
                r = m
            else:
                l = m + 1
        return arr[l - 1][1]
       
