class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOf(val):
            output = 0
            while val:
                output += (val % 10) ** 2
                val //= 10
            return output
        power = lam = 1
        slow, fast = n, sumOf(n)
        while slow != fast:
            if power == lam:
                slow = fast
                power *= 2
                lam = 0
            fast = sumOf(fast)
            lam += 1
        return fast == 1
    