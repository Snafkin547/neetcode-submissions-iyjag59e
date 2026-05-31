class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        prev = [False] * (n + 1)
        prev[-1] = True
        # State: if j can make i
        for i in range(m, -1, -1): # Handles empty s
            curr = [False] * (n + 1)
            curr[-1] = (i == m)
            for j in range(n - 1, -1, -1):
                match = i < m and (s[i] == p[j] or p[j] == '.') # Normal match
                if j + 1 < n and p[j + 1] == "*":
                    curr[j] = curr[j + 2]
                    if match: # for nnn vs n*, current n relies on previous n's result when * involved
                        curr[j] |= prev[j]
                elif match: # Simple match
                    curr[j] |= prev[j + 1]
            prev = curr
        return prev[0]
