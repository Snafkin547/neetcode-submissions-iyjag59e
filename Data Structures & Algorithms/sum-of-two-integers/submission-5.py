class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = carry = 0
        mask = 0xFFFFFFFF # 2**32 - 1 : Smallest 32 bit negative int = all 1s
        limit = 0x7FFFFFFF # 2**31 - 1 : Largest 32 bit positive int = all 1s except MSB
        
        for i in range(32):
            _a = (a >> i) & 1
            _b = (b >> i) & 1
            curr = _a ^ _b ^ carry # Returns 1 when 1 or 3 one(s)
            carry = (_a & _b) | (_a & carry) | (_b & carry) # Returns 1 when 2 or 3 ones
            if curr:
                res |= (1 << i)
        if res > limit:
            res = ~(res ^ mask)
            # mask flips all including MSB(supposed to indicate Negs)
            # Then NOT/~ flips them all back again and prepend infinite 1s so Py recognise it as Neg val
        return res
    # 3 Ones -> curr = 1, carry = 1 
    # 2 Ones -> curr = 0, carry = 1
    # 1 Ones -> curr = 1, carry = 0
    # 0 Ones -> curr = 0, carry = 0