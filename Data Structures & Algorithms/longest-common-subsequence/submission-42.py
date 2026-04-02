class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # state: i, j => how many commonalities after here
        # Ops: if same increment and move both, else move either
        m, n = len(text1), len(text2)
        dp = [[-1] * n for _ in range(m)]
        def helper(i, j):
            if i == m or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = max(helper(i + 1, j), helper(i, j + 1))
            if text1[i] == text2[j]:
                dp[i][j] = max(dp[i][j], 1 + helper(i + 1, j + 1))
            return dp[i][j]
        return helper(0, 0)
                