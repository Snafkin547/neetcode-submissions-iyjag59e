class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        next1, next2 = 1, 0
        for i in range(n - 1, -1, -1):
            curr = 0
            if s[i] != '0':
                curr = next1
                
            if i < n - 1 and (s[i] =='1' or (s[i] == '2' and s[i + 1] in '0123456')):
                curr += next2
            next1, next2 = curr, next1
        return next1