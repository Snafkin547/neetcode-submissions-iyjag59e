class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def checker(val):
            piles.sort()
            count = 0
            for pile in piles:
                count += -round(-pile//val)
                if count > h:
                    return False
            return True

        if len(piles) > h: 
            return None
        small, large = 1, max(piles)
        res = large
        while small <= large:
            mid = round((small+large)/2)
            if checker(mid):
                res = mid
                large = mid - 1
            else:
                small = mid + 1
        return res
