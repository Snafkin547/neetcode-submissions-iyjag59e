class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dfs(idx, buying):
            if idx >= len(prices):
                return 0
            if memo[(idx, buying)]:
                return memo[(idx, buying)]
            # Hold
            res = dfs(idx + 1, buying)
            # Buying
            if not buying:
                res = max(res, - prices[idx] + dfs(idx + 1, True))
            # Selling
            else:
                res = max(res, prices[idx] + dfs(idx + 2, False))
            memo[(idx, buying)] = res
            return res
        return dfs(0, False)