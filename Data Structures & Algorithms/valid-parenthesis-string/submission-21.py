# DP(TD, BU)
# Greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True        
        # state: i and o
        n = len(s)
        prev = [False] * (n + 1)
        prev[0] = True

        for i in range(1, n + 1):
            temp = [False] * (n + 1)
            for o in range(n):
                if s[i - 1] == '(':
                    if o > 0: temp[o] = prev[o - 1]
                elif s[i - 1] == ')':
                    if o < n: temp[o] = prev[o + 1]
                else:
                    if o > 0: temp[o] = prev[o - 1]
                    if o < n: temp[o] |= prev[o + 1]
                    temp[o] |= prev[o]
            prev = temp
        return prev[0]