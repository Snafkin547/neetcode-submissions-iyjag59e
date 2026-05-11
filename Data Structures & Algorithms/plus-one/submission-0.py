class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        res = []
        for i in range(n - 1, -1, -1):
            val = digits[i] + carry
            carry = val // 10
            digits[i] = val % 10
        if carry:
            return [carry] + digits
       
        return digits