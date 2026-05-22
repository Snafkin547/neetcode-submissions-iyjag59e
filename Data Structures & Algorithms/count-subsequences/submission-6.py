class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # Preparatory processing 
        for i in range(m + 1):
            dp[-1][i] = 1

        # if found: diagonal + prev
        for i in range(n - 1, -1, -1):
            curr = False
            offset = n - 1 - i
            for j in range(m - offset - 1, -1, -1):
                dp[i][j] = dp[i][j + 1]
                if t[i] == s[j]:
                    dp[i][j] += dp[i + 1][j + 1]
                    curr = True
            if not curr:
                return 0
        print(dp)
        return dp[0][0]
    
        # abb
        # babb
        # [0,0,0,0,0]
        # [1,1,1,1,0]
        # [2,1,1,0,0]
        # [1,1,0,0,0]
        