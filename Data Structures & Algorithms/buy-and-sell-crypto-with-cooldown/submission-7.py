class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for buying in [True, False]:
                if buying:
                    action = dp[i + 1][not buying] - prices[i] if i < n - 1 else -prices[i]
                    cooldown = dp[i + 1][buying] if i < n - 1 else 0
                    dp[i][buying] = max(action, cooldown)
                else:
                    action = dp[i + 2][not buying] + prices[i] if i < n - 2 else prices[i]
                    cooldown = dp[i + 1][buying] if i < n - 1 else 0
                    dp[i][buying] = max(action, cooldown)
                    
        return dp[0][1]
