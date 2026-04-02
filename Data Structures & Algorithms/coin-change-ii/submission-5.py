class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (n + 1) for _ in range(amount + 1)]
        
        for i in range(n + 1):
            dp[0][i] = 1 # 0 can be achieved 1 way by any coins

        for i in range(1, n + 1):
            c = coins[i-1]
            for a in range(1, amount + 1):
                dp[a][i] = dp[a][i - 1] # Take the so far amount achieved by other coins
                if a - c >= 0:
                    dp[a][i] += dp[a - c][i] # Including the current coin
        return dp[amount][n]
