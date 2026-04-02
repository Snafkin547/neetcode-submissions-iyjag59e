# Bottom Up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        coins.sort() # Enables pruning
        
        for i in range(amount + 1):
            for c in coins:
                if c > i:
                    break
                if dp[i - c] != float('inf'):
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1