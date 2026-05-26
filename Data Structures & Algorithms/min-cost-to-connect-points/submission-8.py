class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = res = 0
        visited = set()
        dists = [10000000] * n
        while len(visited) < n - 1:
            nxt = -1
            visited.add(node)
            for i in range(n):
                if i in visited:
                    continue
                
                curr = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                dists[i] = min(dists[i], curr) # neatly keep the absolute minimum
                if nxt == -1 or dists[i] < dists[nxt]:
                    nxt = i
            node = nxt
            res += dists[nxt]
        return res