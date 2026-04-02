class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # State: index, amount
        # Ops: continue or move to next coin
        n = len(coins)
        prev_dp = [float('inf')] * (amount + 1)
        prev_dp[0] = 0

        for i in range(1, n + 1):
            c = coins[i - 1]
            dp = [float('inf')] * (amount + 1)
            dp[0] = 0
            for a in range(1, amount + 1):
                dp[a] = prev_dp[a]
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
            dp, prev_dp = prev_dp, dp

        return prev_dp[amount] if prev_dp[amount] != float('inf') else -1