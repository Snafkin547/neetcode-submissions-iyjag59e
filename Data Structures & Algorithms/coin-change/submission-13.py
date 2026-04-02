# Topdown
# Try every pattern
# For each balance value, we can avoid duplicated work by dp
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        dp = defaultdict(int)      
        
        def dfs(balance):
            if balance == 0: # Success
                return 0
            
            if dp[balance]: # Visited already
                return dp[balance]
            
            res = float('inf')
            for c in coins:
                if balance - c >= 0: # Defensive
                    res = min(res, 1 + dfs(balance - c))
            # Keep record of min for this balance
            dp[balance] = res
            return dp[balance]
        res = dfs(amount)
        return res if res != float('inf') else -1