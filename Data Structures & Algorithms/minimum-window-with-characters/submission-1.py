class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def index(c):
            return ord(c) - ord('A')

        n = len(s)
        mp = [0] * 58
        count = 0
        for char in t:
            c = index(char)
            if mp[c] == 0:
                count += 1
            mp[c] += 1

        resL, resR = 0, float('inf')
        l = r = 0
        cmap = [0] * 58
        cnt = 0
        while r < n or l < n:
            if cnt < count: # invalid substring
                if r == n:
                    break
                c = index(s[r])
                if mp[c]:
                    if cmap[c] == mp[c] - 1:
                        cnt += 1
                    cmap[c] += 1
                r += 1
            else: # valid substring
                if resR - resL > r - l:
                    resL, resR = l, r

                c = index(s[l])
                if mp[c]:
                    if cmap[c] == mp[c]:
                        cnt -= 1
                    cmap[c] -= 1
                l += 1

        return s[resL:resR] if resR!= float('inf') else ""