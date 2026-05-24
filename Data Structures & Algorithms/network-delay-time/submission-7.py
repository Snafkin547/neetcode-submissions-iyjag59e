class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for ui, vi, ti in times:
            mp[ui].append((vi, ti))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        q = deque([(k, 0)])
        while q:
            node, d = q.popleft()
            for nei, t in mp[node]:
                if dist[node] + t < dist[nei]:
                    q.append((nei, dist[node] + t))
                    dist[nei] = dist[node] + t
            
        res = max(dist[1:])
        return res if res != float('inf') else -1