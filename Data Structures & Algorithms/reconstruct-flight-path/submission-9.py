class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # visit smallest first
        tickets.sort(reverse=True)
        mp = defaultdict(list)
        for fm, to in tickets:
            mp[fm].append(to)

        n = len(tickets) + 1
        res = []
        def dfs(node):
            
            while mp[node]:
                to = mp[node].pop()
                dfs(to)
                res.append(to)
        
        dfs("JFK")
        res.append("JFK")
        return res[::-1]
            