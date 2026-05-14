class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = carry = 0
        mask = 0xFFFFFFFF # 2**32 - 1 : Smallest 32 bit negative int = all 1s
        limit = 0x7FFFFFFF # 2**31 - 1 : Largest 32 bit positive int = all 1s except MSB
        
        while b != 0:
            carry = (a & b) << 1 # Move it to next
            a = (a ^ b) & mask # Limiting to 32 bits
            b = carry & mask # Limiting to 32 bits
        if a > limit:
            a = ~(a ^ mask)
            # mask flips all including MSB(supposed to indicate Negs)
            # Then NOT/~ flips them all back again and prepend infinite 1s so Py recognise it as Neg val
        return a
    # 3 Ones -> curr = 1, carry = 1 
    # 2 Ones -> curr = 0, carry = 1
    # 1 Ones -> curr = 1, carry = 0
    # 0 Ones -> curr = 0, carry = 0