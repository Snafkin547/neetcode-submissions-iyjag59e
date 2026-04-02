class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev, curr = 0, 1
        for i in range(n-1, -1,-1):
            temp = 0
            if s[i] == '0':
                temp = 0
            else:
                temp = curr

            if i < n - 1 and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                temp += prev
                
            prev = curr
            curr = temp
            
        return curr
