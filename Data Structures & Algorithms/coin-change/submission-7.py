class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        
        def dfs(a):
            if a == 0:
                return 0
            if a in memo:
                return memo[a]

            curr = float('inf')

            for c in coins:
                if a - c >= 0:
                    curr = min(curr, 1 + dfs(a - c))
            memo[a] = curr
            return curr
        res = dfs(amount)
        return -1 if res >= float('inf') else res