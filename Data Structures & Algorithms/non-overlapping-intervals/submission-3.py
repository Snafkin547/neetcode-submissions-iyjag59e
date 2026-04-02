#DP Top Down
#DP Bottom Up
#DP Binary Search
# Greedy Sort By start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        memo = [0] * (n + 1)
        intervals.sort(key=lambda x:x[1])

        def dfs(idx):
            if idx == len(intervals):
                return 0
            if memo[idx] != 0:
                return memo[idx]

            res = 1 # This is one as you're definitely adding intervals[idx], because it has met the if condition in the idx - 1 stage
            for i in range(idx + 1, n):
                if intervals[idx][1] <= intervals[i][0]:
                    res = max(res, 1 + dfs(i))
            memo[idx] = res
            return res

        return n - dfs(0)
            
            