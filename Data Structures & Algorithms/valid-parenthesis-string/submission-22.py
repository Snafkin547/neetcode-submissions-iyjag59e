# DP(TD, BU)
# Greedy
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True        
        n = len(s)
        minO = maxO = 0
        
        for i in range(n):
            if s[i] == '(':
                minO += 1
                maxO += 1
            elif s[i] == ')':
                minO = max(0, minO - 1)
                maxO -= 1
                if maxO < 0:
                    return False
            else:
                minO = max(0, minO - 1)
                maxO += 1
        return not minO