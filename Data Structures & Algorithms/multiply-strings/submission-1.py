class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        res = 0
        start = 1
        for i in range(l1 - 1, -1, -1):
            mlt = ord(num1[i]) - ord('0')
            digit = start
            for j in range(l2 - 1, -1, -1):
                res+= mlt * (ord(num2[j]) - ord('0')) * digit
                digit *= 10
            start *= 10
        return str(res)
