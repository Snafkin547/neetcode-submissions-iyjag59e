class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        mp = defaultdict(list)
        for a, b in edges:
            mp[a].append(b)
            mp[b].append(a)
            count[a] += 1
            count[b] += 1
            
        q = deque()
        for i in range(1, len(edges) + 1):
            if count[i] == 1:
                q.append(i)

        while q:
            node = q.popleft()
            for nei in mp[node]:
                count[nei] -= 1
                if count[nei] == 1:
                    q.append(nei)
        
        for a, b in reversed(edges):
            if count[a] > 1 and count[b] > 1:
                return [a, b]
        return []
        
            
