class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for ui, vi, ti in times:
            mp[ui].append((vi, ti))

        minH = [(0, k)]
        res = 0
        visited = set()

        while minH:
            d, node = heapq.heappop(minH)
            if node in visited:
                continue
            visited.add(node)
            res = d
            for nei, t in mp[node]:
                heapq.heappush(minH, (d + t, nei))
        return res if len(visited) == n else -1