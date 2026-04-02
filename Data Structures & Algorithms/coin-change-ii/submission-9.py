class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # State: i, amount
        # Ops: stay or move next
        n = len(coins)
        dp = {}
        def helper(i, balance):
            if balance == 0:
                return 1
            if i == n:
                return 0
            if (i, balance) in dp:
                return dp[(i, balance)]
            
            dp[(i, balance)] = helper(i + 1, balance)
            if balance - coins[i] >= 0: 
                dp[(i, balance)] += helper(i, balance - coins[i])
            return dp[(i, balance)]
        return helper(0, amount)