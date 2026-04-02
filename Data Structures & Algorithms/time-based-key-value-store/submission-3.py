class TimeMap:

    def __init__(self):
        self.keyMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        currArr = self.keyMap[key]
        l, r = 0, len(currArr) - 1
        res = ""
        while l<=r:
            m = (l + r)//2
            if timestamp < currArr[m][0]:
                r = m - 1
            else:
                res = currArr[m][1]
                l = m + 1
        return res