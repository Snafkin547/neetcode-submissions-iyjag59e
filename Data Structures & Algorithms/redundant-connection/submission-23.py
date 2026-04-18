class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        def dfs(curr, prev, target):
            if curr == target:
                return True
            elif curr in visiting:
                return False
            else:
                visiting.add(curr)

            for d in mp[curr]:
                if d != prev and dfs(d, curr, target):
                    return True
            return False

        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
            visiting = set()
            if dfs(a, b, b):
                return [a, b]
        return []

                    
