class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = [0] * 30
        for c in s:
            mp[ord(c) - ord('a')] += 1
        for c in t:
            mp[ord(c) - ord('a')] -=1
        for i in mp:
            if i!= 0:
                return False
        return True