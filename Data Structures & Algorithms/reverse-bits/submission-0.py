class Solution:
    def reverseBits(self, n: int) -> int:
        res = ''
        count = 0
        while n:
            res += str(n & 1)
            count += 1
            n = n >> 1
        zeros = '0' * (32-count)
        return int(res + zeros, 2)
        