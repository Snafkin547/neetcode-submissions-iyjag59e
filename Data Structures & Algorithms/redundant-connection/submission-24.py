class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        start = None
        cycle = set()
        def dfs(curr, prev):
            nonlocal start
            if curr in visiting:
                start = curr
                cycle.add(curr)
                return True
            visiting.add(curr)

            for d in mp[curr]:
                if d != prev and dfs(d, curr):
                    if curr == start:
                        start = None
                    else:
                        cycle.add(d)
                    return True
            return False

        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
            visiting = set()
            if dfs(a, b):
                for u, v in reversed(edges):
                    if u in cycle and v in cycle:
                        return [u, v]
        return []
