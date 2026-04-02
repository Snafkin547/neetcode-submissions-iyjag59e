class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        cnt1 = [0]*26
        cnt2 = [0]*26
        
        for i in range(len(s1)):
            cnt1[ord(s1[i]) - ord('a')] += 1
            cnt2[ord(s2[i]) - ord('a')] += 1
        
        match = 0
        for i in range(len(cnt1)):
            match += 1 if cnt1[i] == cnt2[i] else 0
        
        l, r = 0, len(s1)
        while l + r < len(s2):
            if match == 26:
                return True

            v1 = ord(s2[l + r]) - ord('a')
            cnt2[v1] += 1
            if cnt1[v1] == cnt2[v1]:
                match += 1
            elif cnt1[v1] + 1 == cnt2[v1]:
                match -= 1

            v2 = ord(s2[l]) - ord('a')
            cnt2[v2] -= 1
            if cnt1[v2] == cnt2[v2]:
                match += 1
            elif cnt1[v2] - 1 == cnt2[v2]:
                match -= 1
            l+=1
        return match == 26
