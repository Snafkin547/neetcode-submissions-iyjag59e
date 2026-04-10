# DP(TD, BU)
# Greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp ={}
        n = len(s)
        
        def helper(i, o):
            if o < 0:
                return False
            if i == n:
                return not o

            if (i, o) in dp:
                return dp[(i, o)]
        
            res = False
            if s[i] == '(':
                res |= helper(i + 1, o + 1)
            elif s[i] == ')':
                res |= helper(i + 1, o - 1)
            else:
                res |= helper(i + 1, o) or helper(i + 1, o + 1) or helper(i + 1, o - 1)
            
            dp[(i, o)] = res
            return res
        
        return helper(0, 0)
