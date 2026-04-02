class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Skip after sell
        # State: buying or not
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        def buy_sell(i, buying):
            if i >= n:
                return 0
            if dp[i][buying] != -1:
                return dp[i][buying]
            if buying:
                dp[i][buying] = max(buy_sell(i + 1, buying), buy_sell(i + 2, False) + prices[i])
            else:
                dp[i][buying] = max(buy_sell(i + 1, buying), buy_sell(i + 1, True) - prices[i])
            return dp[i][buying]
        return buy_sell(0, False)

