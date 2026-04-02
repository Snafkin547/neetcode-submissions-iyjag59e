from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(balance):
            if balance == 0: # Success
                return 0
            
            res = float('inf')
            for c in coins:
                if balance - c >= 0: # Defensive
                    res = min(res, 1 + dfs(balance - c))
            return res
        res = dfs(amount)
        return res if res != float('inf') else -1