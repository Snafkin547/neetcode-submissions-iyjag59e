class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        start = None
        cycle = set()
        visiting = [False] * (len(edges) + 1)
        def dfs(curr, prev):
            nonlocal start
            if visiting[curr]:
                start = curr
                return True

            visiting[curr] = True

            for d in mp[curr]:
                if d != prev and dfs(d, curr):
                    if start:
                        cycle.add(curr)
                    if curr == start:
                        start = None
                    return True
            return False

        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)

        dfs(1, -1)

        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []
