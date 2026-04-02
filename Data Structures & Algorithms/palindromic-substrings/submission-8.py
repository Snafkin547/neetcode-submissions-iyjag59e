class Solution:
    def countSubstrings(self, s: str) -> int:
        t = "^#" + "#".join(s) + "#&"
        n = len(t)
        c = r = 0
        dp = [0] * n
        for i in range(1, n - 1):
            if i < r:
                mirror = 2*c - i
                dp[i] = min(r - i, dp[mirror])
            while t[i + dp[i] + 1] == t[i - dp[i] - 1]:
                dp[i] += 1
            if i + dp[i] > r:
                c = i
                r = i + dp[i]
        res = 0
        for i in dp:
            res += (i + 1) >> 1
        return res
    