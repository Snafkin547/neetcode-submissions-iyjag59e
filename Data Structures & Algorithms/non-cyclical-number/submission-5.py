class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOf(val):
            output = 0
            while val:
                output += (val % 10) ** 2
                val //= 10
            return output

        slow, fast = n, sumOf(n)
        while slow != fast:
            fast = sumOf(sumOf(fast))
            slow = sumOf(slow)
        return fast == 1
    