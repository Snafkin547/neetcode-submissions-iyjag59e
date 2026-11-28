class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        one, two = 1, 0
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                one, two = 0, one
                continue
            curr = one
            if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] < '7')):
                curr += two
            one, two = curr, one
        return one