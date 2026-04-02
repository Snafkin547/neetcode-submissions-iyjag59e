class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeft = maxLeft = 0
        star = 0
        for c in s:
            if c == '(':
                minLeft += 1 
                maxLeft += 1
            elif c == ')':
                minLeft -= 1 
                maxLeft -= 1
            else:
                minLeft -= 1
                maxLeft += 1
            
            if maxLeft < 0:
                return False
            if minLeft < 0:
                minLeft = 0
        return minLeft == 0