class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 1
        res = []
        for i in range(n - 1, -1, -1):
            digits[i] = digits[i] + carry
            if digits[i] <= 9:
                return digits
            carry = digits[i] // 10
            digits[i] = digits[i] % 10
        
        return [1] + digits