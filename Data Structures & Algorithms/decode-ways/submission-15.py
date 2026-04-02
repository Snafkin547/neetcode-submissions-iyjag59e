class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        prev, curr = 0, 1
        for i in range(n - 1, -1, -1):
            temp = 0
            if s[i] == '0':
                temp = 0
            elif i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                temp = curr + prev
            else:
                temp = curr
            prev, curr = curr, temp
        return curr