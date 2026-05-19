class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'

        l1, l2 = len(num1), len(num2)
        n = l1 + l2
        res = [0] * n

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                idx = i + j + 1
                val = int(num1[i]) * int(num2[j]) + int(res[idx])
                res[idx] = str(val % 10)
                res[idx - 1] = str(int(res[idx - 1]) + val // 10)
            
        return "".join(res) if res[0] != "0" else "".join(res[1:])
