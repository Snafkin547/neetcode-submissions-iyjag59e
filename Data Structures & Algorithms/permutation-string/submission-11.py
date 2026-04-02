class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if not s1:
            return True

        mp1 = [0] * 26
        mp2 = [0] * 26
        
        for i in range(len(s1)):
            c1 = ord(s1[i]) - ord('a')
            mp1[c1] += 1
            c2 = ord(s2[i]) - ord('a')
            mp2[c2] += 1
        
        if mp1 == mp2:
            return True
        
        # If two arrays match exactly, then True
        # Todo: Optimize by counting how many matches at the beg and at each ops/
        l = 0
        for r in range(len(s1), len(s2)):
            head = ord(s2[l]) - ord('a')
            mp2[head] -= 1
            l += 1

            tail = ord(s2[r]) - ord('a')
            mp2[tail] += 1
            if mp1 == mp2:
                return True

        return False