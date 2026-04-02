class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charSet = [0] * 26
        for c in s:
            charSet[ord(c)-ord('a')] += 1
            
        for c in t:
            charSet[ord(c)-ord('a')] -= 1
            if charSet[ord(c)-ord('a')] < 0:
                return False
        return True
