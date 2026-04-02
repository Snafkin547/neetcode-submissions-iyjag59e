class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, arr = [], []

        def isPali(st):
            l, r = 0, len(st) - 1
            while l <= r:
                if st[l]!=st[r]:
                    return False
                l, r = l+1, r-1
            return True

        def bt(piv):
            if piv >= len(s):
                res.append(arr[:])
                return
            
            for i in range(piv, len(s)):
                if isPali(s[piv:i+1]):
                    arr.append(s[piv:i+1])
                    bt(i+1)
                    arr.pop()
        bt(0)
        return res