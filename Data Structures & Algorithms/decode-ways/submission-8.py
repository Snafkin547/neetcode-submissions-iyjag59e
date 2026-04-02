class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev, curr = 0, 1
        for i in range(n-1, -1,-1):
            if s[i] == '0':
                prev = curr
                curr = 0

            elif i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                temp = curr
                curr += prev
                prev = temp
            else:
                prev = curr
            
        return curr
