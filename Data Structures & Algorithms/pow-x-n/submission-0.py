class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        # if x neg: ocsilate
        sign = -1 if (n % 2 and x < 0) else 1
        # if n neg: denom
        denom = n < 0
        x, n = abs(x), abs(n)
        res = 1
        for i in range(n):
            res *= x
        res *= sign
        return 1/res if denom else res

        