class Solution:
    def isHappy(self, n: int) -> bool:
        s = [0] * 1000
        
        while n and n != 1:
            curr = n
            temp = 0
            while curr:
                temp += (curr % 10) ** 2
                curr //= 10
            
            n = temp
            if s[temp]:
                break
            s[temp] = 1
            temp = 0
        return n == 1