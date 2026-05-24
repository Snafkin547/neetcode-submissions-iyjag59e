class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ''' Success Criteria
            1) Visit All Nodes
            2) Reach them by minimum path
            
            Required Mechanism
            Sub prob = Optimize anything below the current node
        '''
        mp = defaultdict(list)
        for ui, vi, ti in times:
            mp[ui].append((vi, ti))
        
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            dist[node] = time
            for nei, t in mp[node]:
                dfs(nei, time + t)
        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1