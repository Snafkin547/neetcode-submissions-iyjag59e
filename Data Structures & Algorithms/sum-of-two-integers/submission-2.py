class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = carry = 0
        mask = 0xFFFFFFFF
        limit = 0x7FFFFFFF
        
        for i in range(32):
            _a = (a >> i) & 1
            _b = (b >> i) & 1
            curr = _a ^ _b ^ carry # Returns 1 when 1 or 3 one(s)
            carry = (_a & _b) | (_a & carry) | (_b & carry) # Returns 1 when 2 or 3 ones
            if curr:
                res |= (1 << i)
        if res > limit:
            res = ~(res ^ mask)
        return res
    # 3 Ones -> curr = 1, carry = 1 
    # 2 Ones -> curr = 0, carry = 1
    # 1 Ones -> curr = 1, carry = 0
    # 0 Ones -> curr = 0, carry = 0