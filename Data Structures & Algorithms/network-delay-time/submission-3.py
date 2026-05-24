class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        mp = defaultdict(list)
        for ui, vi, ti in times:
            mp[ui].append((vi, ti))

        dist = [float('inf')] * (n + 1)
        
        def calc_dist(curr, time):
            if time >= dist[curr]:
                return

            dist[curr] = time
            
            for nei, dt in mp[curr]:
                calc_dist(nei, time + dt)
            return

        calc_dist(k, 0)
        res = max(dist[1:])
        return -1 if res == float('inf') else res