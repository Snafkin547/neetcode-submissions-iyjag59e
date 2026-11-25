class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        elif n <= 2:
            return n

        one = two = 1
        
        for i in range(n-2, -1, -1):
            curr = one + two
            two, one = curr, two


        return curr
        