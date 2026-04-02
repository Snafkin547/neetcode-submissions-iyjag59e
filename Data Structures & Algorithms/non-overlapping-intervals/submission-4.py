#DP Bottom Up
#DP Binary Search
# Greedy Sort By start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        memo = [0] * (n + 1)
        intervals.sort(key=lambda x:x[1])
        memo[0] = 1
        for i in range(n):
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    memo[i] = max(memo[i], 1 + memo[j])
        return n - max(memo)
            
            