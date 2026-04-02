class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def binary(ss):
            res = 0
            for s in ss:
                mask = 1<<(ord(s) - 96)
                res^=mask
            return res
        charNum = binary(s1)
        l, r = 0, len(s1)
        curr = binary(s2[l:r-1])
        while l + r <= len(s2):
            curr ^= (1 <<ord(s2[l+r-1])-96)
            if curr == charNum:
                return True
            curr ^= (1<<ord(s2[l]) - 96)
            l+=1

        return False
        