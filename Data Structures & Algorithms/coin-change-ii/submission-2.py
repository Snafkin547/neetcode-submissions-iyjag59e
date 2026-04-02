class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = defaultdict(int)
        def dfs(i, balance):
            if balance == 0:
                return 1
            if i >= len(coins) or balance < 0:
                return 0

            if (i, balance) in dp:
                return dp[(i, balance)]

            res = dfs(i, balance - coins[i]) 
            res += dfs(i + 1, balance)
            dp[(i, balance)] = res
            return dp[(i, balance)]
        return dfs(0, amount)
