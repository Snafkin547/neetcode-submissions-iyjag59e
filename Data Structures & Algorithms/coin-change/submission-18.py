class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # State: index, amount
        # Ops: continue or move to next coin
        dp = defaultdict(int)
        def helper(i, balance):
            if balance == 0:
                return 0
            if balance < 0 or i == len(coins):
                return float('inf')
            
            if (i, balance) in dp:
                return dp[(i, balance)]
            
            dp[(i, balance)] = min(1 + helper(i, balance - coins[i]), helper(i + 1, balance))
            return dp[(i, balance)]
        res = helper(0, amount)
        return res if res!= float('inf') else -1
