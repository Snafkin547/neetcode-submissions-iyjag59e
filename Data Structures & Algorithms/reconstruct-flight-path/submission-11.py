class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # visit smallest first
        tickets.sort()
        mp = defaultdict(list)
        for fm, to in tickets:
            mp[fm].append(to)

        res = ["JFK"]
        n = len(tickets)
        def dfs(node):
            if len(res) == n + 1:
                return True
            
            arr = mp[node].copy()
            for i, v in enumerate(arr):
                mp[node].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                mp[node].insert(i, v)
                res.pop()
            return False
        
        dfs("JFK")
        return res
            