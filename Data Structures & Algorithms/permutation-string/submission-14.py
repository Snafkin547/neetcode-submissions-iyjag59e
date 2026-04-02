class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s1:
            return True

        mp1, mp2 = [0] * 26, [0] * 26
        
        n = len(s1)
        for i in range(n):
            mp1[ord(s1[i]) - ord('a')] += 1
            mp2[ord(s2[i]) - ord('a')] += 1
        
        match = 0

        for i in range(26):
            match += 1 if mp1[i] == mp2[i] else 0
        
        # If two arrays match exactly, then True
        l = 0
        for r in range(n, len(s2)):
            if match == 26:
                return True

            head = ord(s2[l]) - ord('a')
            match -= 1 if mp1[head] == mp2[head] else 0
            mp2[head] -= 1
            match += 1 if mp1[head] == mp2[head] else 0
            l += 1

            tail = ord(s2[r]) - ord('a')
            match -= 1 if mp1[tail] == mp2[tail] else 0
            mp2[tail] += 1
            match += 1 if mp1[tail] == mp2[tail] else 0

        return match == 26