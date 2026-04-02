class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1 # 0 can be achieved 1 way by any coins
        prev = [0] * (amount + 1)
        prev[0] = 1

        for i in range(1, n + 1):
            c = coins[i-1]
            for a in range(1, amount + 1):
                dp[a] = prev[a] # Take the so far amount achieved by other coins
                if a - c >= 0:
                    dp[a] += dp[a - c] # Including the current coin
            prev, dp = dp, prev
        
        return prev[amount]
