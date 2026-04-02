# Bottom Up
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(amount + 1):
            for c in coins:
                comp = i - c
                if comp >= 0:
                    dp[i] = min(dp[i], dp[comp] + 1)
        print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1