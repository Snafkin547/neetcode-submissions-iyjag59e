class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # State: index, amount
        # Ops: continue or move to next coin
        n = len(coins)
        dp = [[float('inf')] * (n + 1) for _ in range(amount + 1)]
        for i in range(n + 1):
            dp[0][i] = 0

        for i in range(1, n + 1):
            c = coins[i - 1]
            for a in range(1, amount + 1):
                dp[a][i] = dp[a][i - 1]
                if a - c >= 0:
                    dp[a][i] = min(dp[a][i], 1 + dp[a - c][i])

        return dp[amount][-1] if dp[amount][-1] != float('inf') else -1