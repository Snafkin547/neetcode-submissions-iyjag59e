class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        
        while n and n != 1:
            curr = n
            temp = 0
            while curr:
                temp += (curr % 10) ** 2
                curr //= 10
            
            n = temp
            if temp in s:
                break
            s.add(temp)
            temp = 0
        return n == 1