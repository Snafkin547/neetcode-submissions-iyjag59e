class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minV, maxV = 1, max(piles)
        while minV < maxV:
            mid = minV + (maxV - minV)//2
            temp = 0
            for p in piles:
                temp -= (-p//mid)
            
            if temp <= h:
                maxV = mid
            else:
                minV = mid + 1
        return minV