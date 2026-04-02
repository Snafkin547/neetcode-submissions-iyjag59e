class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        l, r = 0, len(s1)
        cnt1 = [0]*26
        for c in s1:
            v =ord(c)-ord('a')
            cnt1[v]+=1

        cnt2=[0]*26
        for c in s2[l:r-1]:
            cnt2[ord(c)-ord('a')]+=1

        while l+r<=len(s2):
            cnt2[ord(s2[l+r-1])-ord('a')]+=1
            if cnt1==cnt2:
                return True
            cnt2[ord(s2[l])-ord('a')]-=1
            l+= 1
        return False


        