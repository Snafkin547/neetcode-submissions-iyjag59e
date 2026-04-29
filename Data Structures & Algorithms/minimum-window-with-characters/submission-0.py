class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Explore till all t-char is gone
        # Count every char in t within s
        # Find a valid substring and record resL and resR
        # Move l till invalid
        # Move r till valid again
        # cnt = count : when map[] changes from 0 increment and to 0 decrement
        n = len(s)
        mp = defaultdict(int)
        for c in t:
            mp[c] += 1
        count = len(mp)

        resL, resR = 0, float('inf')
        l = r = 0
        cmap = defaultdict(int)
        cnt = 0
        while r < n or l < n:
            if cnt < count: # invalid substring
                if r == n:
                    break
                c = s[r]
                if c in mp:
                    if cmap[c] == mp[c] - 1:
                        cnt += 1
                    cmap[c] += 1
                r += 1
            else: # valid substring
                if resR - resL > r - l:
                    resL, resR = l, r

                c = s[l]
                if c in mp:
                    if cmap[c] == mp[c]:
                        cnt -= 1
                    cmap[c] -= 1
                l += 1
        #if cnt == count and resR - resL > r - l:
        #   resL, resR = l, r

        return s[resL:resR] if resR!= float('inf') else ""