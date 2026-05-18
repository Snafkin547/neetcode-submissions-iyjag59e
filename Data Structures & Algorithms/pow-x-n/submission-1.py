class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        # if n neg: denom
        res = 1
        for i in range(abs(n)):
            res *= x
        return 1/res if n < 0 else res

        