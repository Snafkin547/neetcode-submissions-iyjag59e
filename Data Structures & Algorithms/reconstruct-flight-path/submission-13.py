class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # visit smallest first
        tickets.sort(reverse = True)
        mp = defaultdict(list)
        for fm, to in tickets:
            mp[fm].append(to)

        res = []
        stack = ['JFK']
        
        while stack:
            node = stack[-1]
            if mp[node]:
                stack.append(mp[node].pop())
            else:
                res.append(stack.pop())

        return res[::-1]
            