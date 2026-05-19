class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        res = 0
        start = 1
        for i in range(l1 - 1, -1, -1):
            mlt = int(num1[i])
            digit = start
            for j in range(l2 - 1, -1, -1):
                res+= mlt * int(num2[j]) * digit
                digit *= 10
            start *= 10
        return str(res)
