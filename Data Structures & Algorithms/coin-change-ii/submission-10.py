class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # State: i, amount
        # Ops: stay or move next
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1 # val 0 can be made by any coin
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
        return dp[-1]