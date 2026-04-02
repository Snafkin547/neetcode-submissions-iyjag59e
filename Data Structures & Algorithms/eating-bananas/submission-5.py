class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minV, maxV = 1, max(piles)
        res = 1e10
        while minV <= maxV:
            mid = minV + (maxV - minV)//2
            temp = 0
            for p in piles:
                temp -= (-p//mid)
            
            if temp <= h:
                res = min(res, mid)
                maxV = mid - 1
            else:
                minV = mid + 1
        return res