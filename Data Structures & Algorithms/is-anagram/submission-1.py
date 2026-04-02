class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alpha = [0] * 26
        for ss in s:
            alpha[ord(ss)-ord('a')]+= 1
        for tt in t:
            if alpha[ord(tt)-ord('a')] == 0:
                return False
            else:
                alpha[ord(tt)-ord('a')] -= 1
        return True

