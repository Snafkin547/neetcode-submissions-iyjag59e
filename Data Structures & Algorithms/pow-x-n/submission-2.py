class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        # if n neg: denom
        res = 1
        power = abs(n)
        while power:
            if power & 1: # only multiply when 1
                res *= x
            x *= x
            power >>= 1
        return 1/res if n < 0 else res

        