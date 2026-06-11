class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[-1] = True
        for i in range(m, -1, -1):
            nxt = [False] * (n + 1)
            nxt[-1] = (i == m)
            for j in range(n - 1, -1, -1):
                match = i!=m and s[i] == p[j] or p[j] == '.'
                if j + 1 < n and p[j + 1] == '*':
                    nxt[j] = nxt[j + 2] # in case * acts as empty
                    if match:
                        nxt[j] |= dp[j] # see if s[i + 1] = p[j]
                elif match:
                    nxt[j] = dp[j + 1] # if [i+1][j+1] was True
            dp = nxt
        return dp[0]
