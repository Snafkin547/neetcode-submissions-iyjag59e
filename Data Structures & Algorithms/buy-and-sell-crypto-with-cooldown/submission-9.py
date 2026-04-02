class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 2 for _ in range(n)]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            # Not holding
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            
            # Holding
            prev = dp[i - 2][0] if i > 1 else 0
            dp[i][1] = max(dp[i - 1][1], prev - prices[i])
        return dp[n-1][0]
