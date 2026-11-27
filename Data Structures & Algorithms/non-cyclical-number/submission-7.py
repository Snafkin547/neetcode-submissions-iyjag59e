class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1 and n not in s:
            s.add(n)
            curr = 0
            while n:
                d = n % 10
                n //= 10
                curr += d**2
            n = curr
        return n == 1
