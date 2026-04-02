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
            
            res = -1
            for c in coins:
                if balance - c >= 0: # Defensive
                    temp = dfs(balance - c)
                    if temp == -1: # Not posssible (If all fail, res will be -1 all time)
                        continue
                    # Take as is for first val, as nothing to compare
                    res = min(res, 1 + temp) if res != -1 else 1 + temp
            # Keep record of min for this balance
            dp[balance] = res
            return dp[balance]
        
        return dfs(amount)