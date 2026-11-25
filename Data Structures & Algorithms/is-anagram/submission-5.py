class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # same number of each char
        charsS = [0] * 26
        charsT = [0] * 26
        for c in s:
            charsS[ord(c) - ord('a')] += 1
        
        for c in t:
            charsT[ord(c) - ord('a')] += 1
        
        for i in range(26):
            if charsS[i] != charsT[i]:
                return False
        
        return True
        

