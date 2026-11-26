class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find best interval
        # update so-far best
        # when to move r and l: 
        # memorise min so far
        minimum = None
        res = 0
        for p in prices:
            if minimum is not None:
                minimum = min(minimum, p)
            else:
                minimum = p

            res = max(p - minimum, res)
        return res
