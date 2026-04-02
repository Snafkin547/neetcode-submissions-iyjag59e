class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        for c in t:
            mp[c] -=1
            if not mp[c]:
                del mp[c]
        return len(mp) == 0