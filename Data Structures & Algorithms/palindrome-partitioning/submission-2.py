class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPali(st):
            l, r = 0, len(st) - 1
            while l <= r:
                if st[l]!=st[r]:
                    return False
                l, r = l + 1, r -1
            return True

        res, curr = [], []

        def bt(pivot):
            if pivot >= len(s):
                res.append(curr.copy())
                return 
            for i in range(pivot, len(s)):
                if isPali(s[pivot:i + 1]):
                    curr.append(s[pivot:i + 1])
                    bt(i + 1)
                    curr.pop()
        bt(0)
        return res
