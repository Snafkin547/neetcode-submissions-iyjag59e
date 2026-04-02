class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        # state: i, buying
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[1][True] = - prices[0]

        for i in range(2, n + 1):
            # Buy After Cooldown or keep holding (No need to consider dp[i - 1][False] as it shall be sa me as dp[i - 2][False] if stayed square)
            dp[i][True] = max(dp[i - 2][False] - prices[i - 1], dp[i - 1][True])
            dp[i][False] = max(dp[i - 1][True] + prices[i - 1], dp[i - 1][False])
        print(dp)
        return dp[-1][False]
        # price:1  3  4 0 4
        # Buy :-1 -1 -1 2 -1
        # Sell: 0  2  3 3 6
