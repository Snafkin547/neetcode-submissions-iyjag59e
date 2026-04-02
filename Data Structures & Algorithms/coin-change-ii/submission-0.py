class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = defaultdict(int)
        def dfs(i, balance):
            if balance == 0:
                return 1

            if (i, balance) in dp:
                return dp[(i, balance)]
            
            for idx in range(i, n):
                new_balance = balance - coins[idx]
                if new_balance >= 0:
                    dp[(i, balance)] += dfs(idx, new_balance)

            return dp[(i, balance)]
        return dfs(0, amount)
