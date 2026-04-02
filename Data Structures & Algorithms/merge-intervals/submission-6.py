class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Make a map of int, which increment and decrement for start and end
        intMap = defaultdict(int)
        for s, e in intervals:
            intMap[s] += 1
            intMap[e] -= 1
        # Iterate over the Map in sorted order
        # count balance (if 0, append and reset interval)
        res = []
        interval = []
        balance = 0 # This keeps track of how many overlaps at a time
        for idx in sorted(intMap):
            if not interval:
                interval.append(idx)
            balance += intMap[idx]
            if balance == 0:
                interval.append(idx)
                res.append(interval)
                interval = []
        return res



